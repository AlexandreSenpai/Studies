from dataclasses import dataclass


@dataclass
class DTO[V]:
    data: V