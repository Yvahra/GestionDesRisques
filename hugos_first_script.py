import json
import matplotlib.pyplot as plt
import collections

with open('Ressources/APT.json', encoding="utf8") as user_file:
    file_contents = user_file.read()

# print(file_contents)

parsed_json = json.loads(file_contents)
values = parsed_json['values']

# Affiche les acteurs, les pays ainsi que la date de dernière modif
print("===== PART 1 =====")
for elem in values:
    print(elem['actor'] + ' ' + ','.join(elem['country']) + ' ' + elem['last-card-change'], end=' | ')
print()

# Permet d'avoir une liste du nombre d'occurence des pays
print("===== PART 2 =====")
country_count = {}
for elem in values:
    for value in elem['country']:
        if value in country_count:
            country_count[value] += 1
        else:
            country_count[value] = 1
print(dict(sorted(country_count.items(), key=lambda item: item[1], reverse=True)))

print("===== PART 3 =====")
date_count = {}
for elem in values:
    date_count[elem['actor']] = elem['last-card-change']
print(dict(sorted(date_count.items(), key=lambda item: item[1], reverse=True)))

print("===== PART 4 =====")
myDictMonths = {}
myDictYears = {}
for _, value in date_count.items():
    # Split année
    dateA = value.split('-')[0]
    # Split mois
    dateM = value.split('-')[0] + '-' + value.split('-')[1]
    if dateM in myDictMonths and dateA in myDictYears:
        myDictMonths[dateM] += 1
        myDictYears[dateA] += 1
    else:
        myDictMonths[dateM] = 1
        myDictYears[dateA] = 1

myDictMonths = collections.OrderedDict(sorted(myDictMonths.items()))
myDictYears = collections.OrderedDict(sorted(myDictYears.items()))
print(myDictMonths)
print(myDictYears)

# plt.scatter(myDictMonths.keys(), myDictMonths.values())
# plt.xlabel('Date')
# plt.xticks(["2020-07", "2021-01", "2021-07", "2022-01", "2022-07", "2023-01"])
# plt.ylabel('Nombre d\'APT recensées')
# plt.savefig("Images/nbAPTperMonths.png")

plt.scatter(myDictYears.keys(), myDictYears.values())
plt.xlabel('Date')
plt.ylabel('Nombre d\'APT recensées')
plt.savefig("Images/nbAPTperYears.png")
