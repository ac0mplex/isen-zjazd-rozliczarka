from decimal import Decimal

class Dłużnicy:
    def __init__(self, uczestnicy):
        self.dłużnicy = {}

        for u1 in uczestnicy:
            self.dłużnicy[u1] = {}

            for u2 in uczestnicy:
                self.dłużnicy[u1][u2] = Decimal(0)

    def transfer(self, od, do, ile):
        self.dłużnicy[od][do] -= ile
        self.dłużnicy[do][od] += ile

    def dług(self, kto, komu, ile):
        self.dłużnicy[kto][komu] += ile
        self.dłużnicy[komu][kto] -= ile

    def __str__(self):
        string = ""

        for uczestnik in self.dłużnicy.keys():
            string += f"{uczestnik}:"

            wierzyciele = self.dłużnicy[uczestnik]
            wierzyciele = {
                    wierzyciel: dług
                    for wierzyciel, dług in wierzyciele.items()
                    if dług > 0
            }

            if not wierzyciele:
                string += " jesteś wolny"
            else:
                for wierzyciel, dług in wierzyciele.items():
                    string += f"\n\t{wierzyciel} <- {round(dług, 2)}"

            string += "\n"

        return string.strip()


