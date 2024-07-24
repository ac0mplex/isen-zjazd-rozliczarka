#!/bin/python

from dłużnicy import Dłużnicy
from decimal import Decimal
from dane.zjazd2024 import uczestnicy, transfery, opłaty


dłużnicy = Dłużnicy(uczestnicy)

for transfer in transfery:
    dłużnicy.transfer(transfer.od, transfer.do, transfer.ile)

for opłata in opłaty:
    if type(opłata.od) == list:
        if opłata.proporcjonalnie:
            prop = opłata.proporcjonalnie
            suma_prop = Decimal(sum([prop[uczestnik] for uczestnik in opłata.od]))

            for uczestnik in opłata.od:
                suma = (prop[uczestnik] / suma_prop) * opłata.ile
                dłużnicy.dług(uczestnik, opłata.do, suma)
        else:
            na_każdego = opłata.ile / len(opłata.od)

            for uczestnik in opłata.od:
                dłużnicy.dług(uczestnik, opłata.do, na_każdego)
    elif type(opłata.od) == str:
        dłużnicy.dług(opłata.od, opłata.do, opłata.ile)
    else:
        raise Exception("Opłata może tylko obejmować jednego uczestnika lub listę uczestników")

print(dłużnicy)
