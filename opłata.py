from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

@dataclass
class Opłata:
    do: str
    ile: Decimal
    od: list
    proporcjonalnie: Optional[dict]

    def __init__(self, do, ile, od, proporcjonalnie=None):
        self.do = do
        self.ile = Decimal(ile)
        self.od = od
        self.proporcjonalnie = proporcjonalnie
