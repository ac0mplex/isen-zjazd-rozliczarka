from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Opłata:
    do: str
    ile: Decimal
    od: list
    proporcjonalnie: bool

    def __init__(self, do, ile, od, proporcjonalnie=False):
        self.do = do
        self.ile = Decimal(ile)
        self.od = od
        self.proporcjonalnie = proporcjonalnie
