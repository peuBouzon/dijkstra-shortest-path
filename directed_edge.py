from dataclasses import dataclass

@dataclass
class DirectedEdge:
    source: int 
    target: int 
    weight: float