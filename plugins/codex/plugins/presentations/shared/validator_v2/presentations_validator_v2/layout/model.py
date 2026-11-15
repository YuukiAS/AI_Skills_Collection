from dataclasses import dataclass
from math import isfinite

from ..io import EvidenceMissing, InputError, records
from ..render import union
from ..schemas import Finding

MM = 72 / 25.4
TEX = 72 / 72.27
EPS = 1e-6


def number(value, label):
    if type(value) not in (int, float) or not isfinite(value):
        raise InputError(f"Invalid number: {label}")
    return value


def check(code, ok, target, reason, **evidence):
    return Finding(code, "PASS" if ok else "FAIL", target, reason, evidence=evidence)


def route(code, status, target, reason, **evidence):
    return Finding(code, status, target, reason, evidence=evidence)


@dataclass
class Object:
    spec: dict
    lines: list
    drawings: list
    images: list

    @property
    def role(self):
        return self.spec["role"]

    @property
    def box(self):
        return union([*(line.box for line in self.lines),
                      *(drawing.box for drawing in self.drawings), *self.images])

    @property
    def texts(self):
        return ["".join(span["text"] for span in line.spans) for line in self.lines]


class Page:
    def __init__(self, spec, render):
        self.id = spec["id"]
        self.spec = spec
        self.render = render
        self.objects = {}
        inventories = {key: set() for key in ("lines", "drawings", "images")}
        for name, row in records(spec["objects"]).items():
            content = []
            for key, used in inventories.items():
                source = getattr(render, key)
                indexes = row.get(key, [])
                if (not isinstance(indexes, list)
                        or any(type(index) is not int or index < 0 or index >= len(source)
                               for index in indexes)
                        or len(indexes) != len(set(indexes))):
                    raise InputError(f"Invalid {key} references for {name}")
                if key == "lines" and used.intersection(indexes):
                    raise InputError(f"Rendered text already has a semantic owner: {name}")
                used.update(indexes)
                content.append([source[index] for index in indexes])
            self.objects[name] = Object(row, *content)
            _ = self.objects[name].box
        self.unbound_lines = sorted(set(range(len(render.lines))) - inventories["lines"])
        self.unbound_images = sorted(set(range(len(render.images))) - inventories["images"])
        self.unbound_drawings = sorted(set(range(len(render.drawings))) - inventories["drawings"])
        self.px = render.bounds.width / 1920

    def by_role(self, *roles):
        return [obj for obj in self.objects.values() if obj.role in roles]

    def one(self, role):
        items = self.by_role(role)
        if len(items) != 1:
            raise EvidenceMissing(f"{self.id} requires one {role}")
        return items[0]

    def get(self, name):
        if name not in self.objects:
            raise EvidenceMissing(f"No rendered object for {name} on {self.id}")
        return self.objects[name]
