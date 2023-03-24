import json
import time

import requests
import re
from bs4 import BeautifulSoup

with open("Ressources/APT.json", "r", encoding="utf-8") as f:
    data = json.load(f)

links = []

for value in data["values"]:
    if "information" in value and "last-card-change" in value:
        year = int(value["last-card-change"][:4])
        if year in [2018, 2019, 2020, 2021, 2022, 2023]:
            links.extend(value["information"])

for link in links:
    try:
        tab = []
        # Envoyer une requête GET à la page
        response = requests.get(link)

        # Vérifier si le contenu de la réponse est du type "text/html"
        if "text/html" in response.headers["content-type"]:
            # Extraire les codes CVE de la page HTML
            soup = BeautifulSoup(response.content, "html.parser")
            cve_tags = soup.find_all(string=lambda text: "CVE-" in text)

            # Utiliser une expression régulière pour extraire le code CVE
            cve_pattern = r'CVE-\d{4}-\d{4,7}'
            for cve_tag in cve_tags:
                cve_match = re.search(cve_pattern, cve_tag)
                if cve_match:

                    cve_code = cve_match.group()
                    if not tab.__contains__(cve_code):
                        print(f"{cve_code}")
                        tab.insert(cve_code)

        time.sleep(1)
    except:
        continue