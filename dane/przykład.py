from transfer import Transfer
from opłata import Opłata

uczestnicy = [
    "Solniczek",
    "Traveler",
    "Gambrynista",
]

dni = {
    "Solniczek": 7,
    "Traveler": 7,
    "Gambrynista": 2,
}

transfery = [
    # od, do, ile
    Transfer("Solniczek", "Traveler", 200),
]

opłaty = [
    # do, ile, od
    Opłata("Gambrynista", 2330, uczestnicy, proporcjonalnie=True), # za domek
    Opłata("Gambrynista", 500, ["Solniczek", "Traveler"]), # alkohol
    Opłata("Gambrynista", 50, "Solniczek"), # pamiątki
]
