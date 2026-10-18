# Candidate-availability isolation

- check_type: read-only capability inspection before candidate creation
- Web_plugin_inventory_control: `NOT_EXPOSED`
- private_candidate_create_control: `NOT_EXPOSED`
- Project_scoped_attachment_control: `NOT_EXPOSED`
- arm_scoped_availability_control: `NOT_EXPOSED`
- candidate_consumption_observation: `NOT_EXPOSED`
- result: `UNPROVEN`

The available tools do not provide a current-surface mechanism that can make
one exact private candidate available and consumable in Treatment while making
it unavailable and non-consumable in Control. Consequently, the candidate
cannot be established as W2's only substantive arm difference without assuming
unobserved product behavior or using a forbidden global install/uninstall path.

No plugin inventory, candidate, release, or permission was mutated.
