.. _feature_hashing:

Feature hashing
===============

.. currentmodule:: sklearn.feature_extraction

The class :class:`FeatureHasher` is a high-speed, low-memory vectorizer that
uses a technique known as
`feature hashing <https://en.wikipedia.org/wiki/Feature_hashing>`_,
or the "hashing trick".
Instead of building a hash table of the features encountered in training,
as the vectorizers do, instances of :class:`FeatureHasher`
apply a hash function to the features
to determine their column index in sample matrices directly.
The result is increased speed and reduced memory usage,
at the expense of inspectability;
the hasher does not remember what the input features looked like
and has no ``inverse_transform`` method.

Since the hash function might cause collisions between (unrelated) features,
a signed hash function is used and the sign of the hash value
determines the sign of the value stored in the output matrix for a feature.
This way, collisions are likely to cancel out rather than accumulate error,
and the expected mean of any output feature's value is zero. This mechanism
is enabled by default with ``alternate_sign=True`` and is particularly useful
for small hash table sizes (``n_features < 10000``). For large hash table
sizes, it can be disabled, to allow the output to be passed to estimators like
:class:`~sklearn.naive_bayes.MultinomialNB` or
:class:`~sklearn.feature_selection.chi2`
feature selectors that expect non-negative inputs.

:class:`FeatureHasher` accepts either mappings
(like Python's ``dict`` and its variants in the ``collections`` module),
``(feature, value)`` pairs, or strings,
depending on the constructor parameter ``input_type``.
Mappings are treated as lists of ``(feature, value)`` pairs,
while single strings have an implicit value of 1,
so ``['feat1', 'feat2', 'feat3']`` is interpreted as
``[('feat1', 1), ('feat2', 1), ('feat3', 1)]``.
If a single feature occurs multiple times in a sample,
the associated values will be summed
(so ``('feat', 2)`` and ``('feat', 3.5)`` become ``('feat', 5.5)``).
The output from :class:`FeatureHasher` is always a ``scipy.sparse`` matrix
in the CSR format.

Feature hashing can be employed in document classification,
but unlike :class:`~text.CountVectorizer`,
:class:`FeatureHasher` does not do word
splitting or any other preprocessing except Unicode-to-UTF-8 encoding;
see :ref:`hashing_vectorizer`, below, for a combined tokenizer/hasher.

As an example, consider a word-level natural language processing task
that needs features extracted from ``(token, part_of_speech)`` pairs.
One could use a Python generator function to extract features::

  def token_features(token, part_of_speech):
      if token.isdigit():
          yield "numeric"
      else:
          yield "token={}".format(token.lower())
          yield "token,pos={},{}".format(token, part_of_speech)
      if token[0].isupper():
          yield "uppercase_initial"
      if token.isupper():
          yield "all_uppercase"
      yield "pos={}".format(part_of_speech)

Then, the ``raw_X`` to be fed to ``FeatureHasher.transform``
can be constructed using::

  raw_X = (token_features(tok, pos_tagger(tok)) for tok in corpus)

and fed to a hasher with::

  hasher = FeatureHasher(input_type='string')
  X = hasher.transform(raw_X)

to get a ``scipy.sparse`` matrix ``X``.

Note the use of a generator comprehension,
which introduces laziness into the feature extraction:
tokens are only processed on demand from the hasher.

.. dropdown:: Implementation details

  :class:`FeatureHasher` uses the signed 32-bit variant of MurmurHash3.
  As a result (and because of limitations in ``scipy.sparse``),
  the maximum number of features supported is currently :math:`2^{31} - 1`.

  The original formulation of the hashing trick by Weinberger et al.
  used two separate hash functions :math:`h` and :math:`\xi`
  to determine the column index and sign of a feature, respectively.
  The present implementation works under the assumption
  that the sign bit of MurmurHash3 is independent of its other bits.

  Since a simple modulo is used to transform the hash function to a column index,
  it is advisable to use a power of two as the ``n_features`` parameter;
  otherwise the features will not be mapped evenly to the columns.

  .. rubric:: References

  * `MurmurHash3 <https://github.com/aappleby/smhasher>`_.


.. rubric:: References

* Kilian Weinberger, Anirban Dasgupta, John Langford, Alex Smola and
  Josh Attenberg (2009). `Feature hashing for large scale multitask learning
  <https://alex.smola.org/papers/2009/Weinbergeretal09.pdf>`_. Proc. ICML.

.. _text_feature_extraction:
