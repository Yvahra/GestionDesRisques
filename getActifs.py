FILE_PATH = 'Ressources/APT.json'
RES_PATH = 'Ressources/APT_actifs.txt'
NB_JOUR_RECENT = 6*30


import json
from datetime import datetime as dt, timedelta

data = json.load(open(FILE_PATH, encoding='utf8'))

values = data["values"]

apt_actifs = {}

for elem in values:
    actor = elem['actor']
    last_card_change = elem['last-card-change']
    if dt.strptime(last_card_change, "%Y-%m-%d") > dt.now() - timedelta(NB_JOUR_RECENT):
        apt_actifs[actor] = last_card_change

f = open(RES_PATH, 'w')
for elem in apt_actifs:
    f.write(elem+':'+apt_actifs[elem]+'\n')

print('Nombre d\'APT actifs récemment :',len(apt_actifs.keys()))