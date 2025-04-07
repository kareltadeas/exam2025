

uchazeci = [
    {"Name": "Jan Novák", "Mat": 85, "Cj": 78, "Aj": 90},
    {"Name": "Petra Svobodová", "Mat": 92, "Cj": 88, "Aj": 85},
    {"Name": "Karel Dvořák", "Mat": 50, "Cj": 95, "Aj": 80},
]

def vyber_prijate(uchazeci):
    vhodni = []
    for u in uchazeci:
        if u["Mat"] >= 60 and u["Cj"] >= 60 and u["Aj"] >= 60:
            u["celkem"] = u["Mat"] + u["Cj"] + u["Aj"]
            vhodni.append(u)

    vhodni.sort(key=lambda x: (x["celkem"], x["Mat"]), reverse=True)

    return vhodni[:15]

prijati = vyber_prijate(uchazeci)

for poradi, uchazec in enumerate(prijati, start=1):
    print(f"{poradi}. {uchazec['Name']} – {uchazec['Mat']} (M), {uchazec['Cj']} (ČJ), {uchazec['Aj']} (AJ) – Celkem: {uchazec['celkem']}")

