# Shortlist requirements en use cases

## Requirements

### Requirements voor PoC

1. Moet kunnen integreren met tools van Mainframe 6
2. Moet kunnen integreren met tools buiten Mainframe 3
3. Ondersteuning van de taal (vendors, community, documentatie, developer tooling) 4
4. Security vulnerabilities 3
5. Robuustheid (hoe lang gaat de code mee) 6
6. Herbruikbaarheid van code (libraries, GIT, ) 7

## Use cases

1. Het werken met z/OS datasets en USS files 2
2. Gebruik van API's 4
3. Genereren van JCL m.b.v. ISPF REXX File Tailoring services of Python Jinja templating 3
4. ISPF support 5
5. Interfacing met MasterConsoles 1
6. Equivalent van PARSE en ADDRESS in Python 3
7. Oproepen van services zoals DFSMS, RACF, ZOS, ISPF, SDSF, WLM, DB2, USS, TSO etc. 4
8. Rexx stems vs lists of dict of objects in Python 2
9. Informatie uit SDSF halen 1
10. Job submitten en output rapporteren 1
11. RACF cleanups 2
12. Opstarten van LPARs 1
13. Genereren van rapporten 1

## Wat we niet doen

1. Performance en CPU gebruik 3
2. AI/LLM support 1
3. Rexx EBCDIC vs Python Unicode 2
4. Voorganger CLIST vs REXX 1
5. Structuur van de code 1
6. Object georiënteerd programmeren 1
7. Steun voor AI/LLM's 1
8. Lijnen code 2

## Verwerken van de antwoorden uit de form voor literatuur

- Hoeveelheid mensen die nu en in de toekomst de taal kennen 7
- Python is gratis op zIIP, maar niet zo'n hoog volume dat het een groot prijsverschil kan maken 2
- Geen support voor Rexx 2
  - Rexx script data te verwerken. Wil herschrijven in Python, maar bedrijf heeft ZOAU nog niet geimplementeerd. 1
  - Wil read/write doen naar USS met Rexx, moest add-on libraries installeren. 1
- Gebruik van de taal hangt af van de use case. 5
- REXX en Python zijn allebei niet het meest geschikt voor zware ladingen of performance kritische toepassingen. 1
- Rexx wordt gebruikt voor kleine scripts 2
- Python wordt voornamelijk gebruikt als er intercatie met de buitenwereld nodig is 2
- Een extreme blik: Python is andermans packages, Rexx is alles zelf schrijven. 1
- Mainframe heeft nog problemen met USS support 2
