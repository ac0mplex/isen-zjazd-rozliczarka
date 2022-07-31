from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Transfer:
    od: str
    do: str
    ile: Decimal
