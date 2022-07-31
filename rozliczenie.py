#!/bin/python

from dłużnicy import Dłużnicy
from decimal import Decimal
from dane.zjazd2022 import uczestnicy, dni, transfery, opłaty


dłużnicy = Dłużnicy(uczestnicy)

for transfer in transfery:
    dłużnicy.transfer(transfer.od, transfer.do, transfer.ile)

for opłata in opłaty:
    if type(opłata.od) == list:
        if opłata.proporcjonalnie:
            suma_dni = Decimal(sum([dni[uczestnik] for uczestnik in opłata.od]))

            for uczestnik in opłata.od:
                suma = (dni[uczestnik] / suma_dni) * opłata.ile
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
