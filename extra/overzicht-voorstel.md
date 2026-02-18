# Overzicht onderzoeksvoorstel

## Titel: De automatisatiestack van de toekomst op z/OS met Rexx en Python

## Inleiding

**De hoofdvraag: Hoe ziet de automatisatie stack van de toekomst eruit op z/OS(, en welke obstakels liggen in de weg voor Python)?**

De deelvragen:

- Waarom is er nood aan modernisatie van mainframe?
- Wat doet automatisatie op mainframes?
- Wat zijn de voor- en nadelen van Rexx?
- Wat zijn de voor- en nadelen van Python?
- Kan Python Rexx vervangen op een performante manier, specifiek binnen de scope van JCL genereren?
- ...

Dan 1.1 uit literatuurstudie, aanbrengen van rexx en python. we gaan doen:

- Vergelijking van rexx en python (hoe diep is nog onzeker)
- Risico-analyse qua onderhoudbaarheid van python
- PoC van JCL genereren met file tailoring en jinja
- Blik op de toekomst met ansible

## 1. Literatuurstudie: De Evolutie van Mainframe Scripting -> moet doorlopende tekst zijn

1.1 De huidige status van Mainframe. De "Skills Gap": De uitstroom van COBOL/REXX-experts (pensioengolf) en de noodzaak om jong talent aan te trekken met moderne talen -> Overgang naar de modernisatiegolf.

1.2 Evolutie van Programmeer- en Scriptingtalen. Geschiedenis van het platform: Ponskaarten & Assembler -> High-Level Languages: De opkomst van FORTRAN, PL/I, COBOL en CLIST -> Specifiek scripting: De overgang van CLIST naar REXX en waarom.

1.3 Introductie van Python: Modern, simpel, veel packages,...

## 2. Methodologie: ( Benchmark ) & casus

### 2.1 Vergelijkende Studie: REXX vs. Python/ZOAU

#### Fase 1

 2.1.1 Rexx commandos (EXECIO, MVSVAR, STACK, STEM, ADDRESS ...) vergelijken met equivalent in Python. Mogelijkheid om oppervlakkig of heel diep te gaan. Keuze uit quantity of quality

( Kwantitatieve Benchmark: Vergelijk specifieke commando's op basis van:

- Aantal parameters: Hoe complex is de syntax?
- Regels code: Hoe compact is de oplossing?
- Leercurve: Hoe snel begrijpt een "non-mainframer" de code?
- Afhankelijkheden: Wat moet er geïnstalleerd zijn om dit te laten werken? )
-> dit is te subjectief

#### Fase 2

 2.1.2 Onderhoudbaarheid en continuïteit: backward compatibility die rexx heeft vs Python heeft externe packages, maar dit brengt conflicten met zich mee. -> concluderen dat python niet perfect is

### 2.2 Case Study: File Tailoring (JCL Genereren)

#### Fase 3

- REXX: Gebruik van ISPF Skeletons. Complexiteit toevoegen met ISPF Tabellen en de '(DOT' iteratie.
- Python: Gebruik van de Jinja2. Vertalen van ISPF Skeleton naar een Jinja-template.

#### Planning

Gantt diagram

## 3. Conclusie: De Toekomst van z/OS Automatisatie

3.1 Besluit: Voor- en Nadelen. Is Python een volwaardige vervanger van REXX?

3.2 Verder onderzoek: Ansible -> eventueel al te verwerken in BP, maar ambitieus, zeker zonder eigen z/OS omgeving (z Xplore?)
