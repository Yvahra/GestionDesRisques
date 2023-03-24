FILE_PATH = 'Ressources/APT.json'
RES_PATH = 'Ressources/APT_actifs.txt'
PLOT1_PATH = 'Images/evol_nbAPT_sansUpdate.png'
PLOT2_PATH = 'Images/nbAPTbyCountry.png'
NB_JOUR_RECENT = 6*30


import json
from datetime import datetime as dt, timedelta
import matplotlib.pyplot as plt

data = json.load(open(FILE_PATH, encoding='utf8'))
values = data["values"]
apt_actifs = {}
nbAPTbyDate={}
date_min = None
maxAPT = 0

for elem in values:
    maxAPT += 1
    actor = elem['actor']
    last_card_change = elem['last-card-change']
    if date_min is None: date_min = dt.strptime(last_card_change, "%Y-%m-%d")
    elif date_min > dt.strptime(last_card_change, "%Y-%m-%d") : date_min = dt.strptime(last_card_change, "%Y-%m-%d")

    if dt.strptime(last_card_change, "%Y-%m-%d") > dt.today() - timedelta(NB_JOUR_RECENT):
        apt_actifs[actor] = last_card_change

    if last_card_change in nbAPTbyDate: nbAPTbyDate[last_card_change] += 1
    else: nbAPTbyDate[last_card_change] = 1

f = open(RES_PATH, 'w')
for elem in apt_actifs:
    f.write(elem+':'+apt_actifs[elem]+'\n')

nbAPTbyDate = dict(sorted(nbAPTbyDate.items()))
dates = list(nbAPTbyDate.keys())
print(dates)
for i in range(len(dates)):
    dates[i] = dt.strftime(dt.strptime(dates[i], "%Y-%m-%d"),"%d/%m")

cumule = {}
last_number = 0
for k in nbAPTbyDate:
    if dt.strptime(k, "%Y-%m-%d") < dt.today() - timedelta(NB_JOUR_RECENT):
        cumule[dt.strftime(dt.strptime(k, "%Y-%m-%d") + timedelta(NB_JOUR_RECENT), "%d/%m/%y")] = last_number + nbAPTbyDate[k]
        last_number += nbAPTbyDate[k]

plt.plot(cumule.keys(), cumule.values(), label="Évolution du nombre d'APT sans update depus au moins six mois.")
plt.plot(cumule.keys(), [maxAPT for i in range(len(cumule.values()))], label="Maximum d'APT recensés")
plt.xlabel('Date (6 dernier mois avant le '+dt.strftime(dt.today(), "%d/%m/%Y")+")")
plt.xticks([1, len(cumule.keys())//4, len(cumule.keys())//2, 3*len(cumule.keys())//4, len(cumule.keys())-1])
plt.ylabel('Nombre d\'APT sans update')
plt.legend()
plt.title("Nombre d\'APT sans update depuis plus de six mois")
plt.savefig(PLOT1_PATH)

plt.cla()

plt.plot(cumule.keys(), cumule.values(), label="Évolution du nombre d'APT sans update depus au moins six mois.")
plt.plot(cumule.keys(), [maxAPT for i in range(len(cumule.values()))], label="Maximum d'APT recensés")
plt.xlabel('Date (6 dernier mois avant le '+dt.strftime(dt.today(), "%d/%m/%Y")+")")
plt.xticks([1, len(cumule.keys())//4, len(cumule.keys())//2, 3*len(cumule.keys())//4, len(cumule.keys())-1])
plt.ylabel('Nombre d\'APT sans update')
plt.legend()
plt.title("Nombre d\'APT sans update depuis plus de six mois")
plt.savefig(PLOT2_PATH)




print('Nombre d\'APT actifs récemment :',len(apt_actifs.keys()))
