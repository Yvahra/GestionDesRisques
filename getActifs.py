FILE_PATH = 'Ressources/APT.json'
RES_PATH = 'Ressources/APT_actifs.txt'
PLOT1_PATH = 'Images/plot1.png'
NB_JOUR_RECENT = 6*30


import json
from datetime import datetime as dt, timedelta
import matplotlib.pyplot as plt

data = json.load(open(FILE_PATH, encoding='utf8'))
values = data["values"]
apt_actifs = {}
nbAPTbyDate={}

for elem in values:
    actor = elem['actor']
    last_card_change = elem['last-card-change']
    if dt.strptime(last_card_change, "%Y-%m-%d") > dt.today() - timedelta(NB_JOUR_RECENT):
        apt_actifs[actor] = last_card_change
        if dt.strftime(dt.strptime(last_card_change, "%Y-%m-%d"), "%m-%d") in nbAPTbyDate : nbAPTbyDate[dt.strftime(dt.strptime(last_card_change, "%Y-%m-%d"), "%m-%d")] += 1
        else: nbAPTbyDate[dt.strftime(dt.strptime(last_card_change, "%Y-%m-%d"), "%m-%d")] = 1

f = open(RES_PATH, 'w')
for elem in apt_actifs:
    f.write(elem+':'+apt_actifs[elem]+'\n')

plt.scatter(nbAPTbyDate.keys(), nbAPTbyDate.values())
plt.xlabel('Date')
plt.ylabel('Nombre d\'APT sans nouvelle depuis la date')
plt.savefig(PLOT1_PATH)

print('Nombre d\'APT actifs récemment :',len(apt_actifs.keys()))