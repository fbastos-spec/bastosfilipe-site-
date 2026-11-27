#!/usr/bin/env python3
"""Contrôle des plans du site et des fichiers llms.

À lancer depuis la racine du dépôt AVANT tout commit qui touche une page,
un document, une carte, un plan ou un llms :

    python3 _travail/controle_plans.py

Il sort en erreur (code 1) si l'un des cinq fichiers est vide ou trop petit,
si un plan n'est pas du XML valide, s'il contient un doublon, ou si une
adresse de bastosfilipe.com citée dans un plan ou un llms ne mène à aucun
fichier du dépôt.

Raison d'être : le 21 novembre 2026, un commit a publié ces cinq fichiers
vides (0 octet) et personne ne l'a vu pendant cinq jours.
"""
import os
import re
import sys
import xml.etree.ElementTree as ET

SITE = "https://bastosfilipe.com/"
# fichier -> (taille minimale en octets, nombre minimal d'adresses du site)
FICHIERS = {
    "sitemap.xml": (40000, 400),
    "arc/sitemap.xml": (20000, 300),
    "llms.txt": (10000, 40),
    "arc/llms.txt": (10000, 40),
    "arc/llms-fr.txt": (10000, 40),
}


def cible(loc):
    p = loc[len(SITE):].split("#")[0].split("?")[0]
    if p == "" or p.endswith("/"):
        c = p + "index.html"
        return c if os.path.isfile(c) else None
    if os.path.isfile(p):
        return p
    for c in (p + ".html", p + "/index.html"):
        if os.path.isfile(c):
            return c
    return None


def main():
    erreurs = []
    for f, (taille_min, n_min) in FICHIERS.items():
        if not os.path.isfile(f):
            erreurs.append(f"{f} : fichier absent")
            continue
        taille = os.path.getsize(f)
        if taille < taille_min:
            erreurs.append(f"{f} : {taille} octets, moins que le minimum de {taille_min}")
            continue
        texte = open(f, encoding="utf-8").read()
        if f.endswith(".xml"):
            try:
                racine = ET.fromstring(texte)
            except ET.ParseError as e:
                erreurs.append(f"{f} : XML invalide ({e})")
                continue
            locs = [e.text.strip() for e in racine.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
            doublons = sorted({l for l in locs if locs.count(l) > 1})
            for d in doublons:
                erreurs.append(f"{f} : adresse en double {d}")
        else:
            locs = [u.rstrip(".,;") for u in re.findall(r"https://bastosfilipe\.com/[^\s)\]>\"']*", texte)]
            # une adresse modèle, écrite avec <slug>, n'est pas une vraie adresse
            locs = [u for u in locs if "<" not in u]
        internes = [l for l in locs if l.startswith(SITE)]
        if len(internes) < n_min:
            erreurs.append(f"{f} : {len(internes)} adresses du site, moins que le minimum de {n_min}")
        mortes = sorted({l for l in internes if cible(l) is None})
        for m in mortes:
            erreurs.append(f"{f} : adresse sans fichier {m}")
        print(f"{f} : {taille} octets, {len(internes)} adresses du site, {len(mortes)} sans fichier")
    if erreurs:
        print("\nÉCHEC :")
        for e in erreurs:
            print("  -", e)
        return 1
    print("\nContrôle des plans : tout est bon.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
