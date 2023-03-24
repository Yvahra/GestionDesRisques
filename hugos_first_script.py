import json
import collections

with open('APT.json', encoding="utf8") as user_file:
    file_contents = user_file.read()

# print(file_contents)

parsed_json = json.loads(file_contents)
values = parsed_json['values']

# Affiche les acteurs, les pays ainsi que la date de dernière modif
for elem in values:
    print(elem['actor'] + ' ' + ','.join(elem['country']) + ' ' + elem['last-card-change'], end=' | ')
print()

# Permet d'avoir une liste du nombre d'occurence des pays
country_count = {}
for elem in values:
    for value in elem['country']:
        if value in country_count:
            country_count[value] += 1
        else:
            country_count[value] = 1
print(dict(sorted(country_count.items(), key=lambda item: item[1], reverse=True)))

date_count = {}
for elem in values:
    date_count[elem['actor']] = elem['last-card-change']
print(dict(sorted(date_count.items(), key=lambda item: item[1], reverse=True)))