# Interview with Emma

## Objective

### Technologies

- Learn more about how Python and/or Rexx are used in the context of Mainframe
  - About the role of both in automation in the workplace
- Why Python, and not Rexx, should be used in RACF
- Get Emma's perspective on how she sees the future of Mainframe
  - Broad perspective
  - Specifically when it comes to automation
- Emma's insights/opinions/experience/...(e.g. SEAR)

### Requirements

- Ask opinion about use cases:
  - IPL of LPAR (favoring Rexx)
  - Using API's (favoring Python)
  - Generating JCL (Python jinja2 vs Rexx File Tailoring)
  - TBD Using RACF (Rexx is most used, Python has more use?)

- Ask about how to measure success of a use case
  - Examples of requirements: Lines of code, dependencies on external libraries

- Ask feedback about form: <https://forms.office.com/Pages/ResponsePage.aspx?id=DjH3XBoJxUus1ybHIdTMzZet1FziglVLkCoi473pS5tUOVdBRVM1UjZQWjhSQVFCQ0dXTzU5TU1DNi4u>

### Notes

Rexx is used for security only bc it's mandatory in that use. in defined custom fields for data validation. you have to program rexx for that.
python for automation, for access to the user environment. one off rexx scripts are used by some, same with python. emma does that with python.
benefit of python is access to argparse, while rexx is hard coded.
rexx isn't very good RACF. python has so many built in utilities.
dependencies problem: having access to more tools isn't a bad thing. if you don't know how to use, you shouldn't touch it. try to avoid unneceasary depndencies. check python standard library. then build it yourself, except if there is a well established package. If there is a big community, it's probably fine. even if there is no 3rd party languages, core python is still great.
in 20y we won't see rexx or clist go away. If somebody wants to build something new, it will be python. maintaining new languages is easier. not as much code, so not like cobol, which will stay. but building infrastructure (automation) will be new languages.
data science/analysis, one off financial reports. those people know python, not older languages.
python is more fully featured. all sorts of stuff built in that rexx doesn't have. even converting is way easier in python. rexx is so much tougher, defeats the purpose of scripting. python used to be slower, it has gotten faster

invoking stuff in a different way with python. api thing is a real problem for python. zoau is constantly adding more further. it's growing. the good thing about being early is you won't have to do a lot when it turns big

### Conclusie

#### De Rol van REXX vs. Python

- REXX als noodzaak: REXX blijft vooral in gebruik voor specifieke beveiligingstaken (zoals custom fields voor datavalidatie) omdat het daar simpelweg verplicht is.

- Python voor modernisering: Voor automatisering en toegang tot de gebruikersomgeving is Python de standaard aan het worden. Waar REXX vaak met hardcoded waarden werkt, biedt Python krachtige tools zoals argparse voor flexibele input.

- Beheer en Onderhoud: Python-code is vaak korter en makkelijker te onderhouden dan oudere talen. Voor nieuwe infrastructuur en automatisering wordt dan ook steevast voor Python gekozen.

#### Functionaliteit en Ecosystemen

- Ingebouwde kracht: Python beschikt over een enorme "Standard Library" en talloze ingebouwde utilities die REXX mist. Zelfs dataconversie, wat in REXX moeizaam gaat, is in Python eenvoudig.

- Afhankelijkheden: Het devies is: gebruik eerst de standaardbibliotheek, bouw het anders zelf, en gebruik alleen externe pakketten als ze een grote community hebben. Meer tools zijn een voordeel, mits de gebruiker over de juiste kennis beschikt.

- Data Science: Voor data-analyse en financiële rapportages is Python de enige logische keuze, simpelweg omdat de nieuwe generatie professionals deze taal al beheerst.

#### Integratie en Toekomstvisie

- De rol van ZOAU: De IBM Z Open Automation Utilities (ZOAU) zijn cruciaal. Hoewel het aanroepen van API's in Python soms nog een uitdaging is, groeit dit ecosysteem snel. Vroeg instappen betekent een voorsprong zodra dit de nieuwe standaard is.

- Snelheid: Waar Python vroeger als traag werd gezien ten opzichte van scriptingtalen op de mainframe, is de performance inmiddels aanzienlijk verbeterd.

- Blijvers versus Nieuwkomers:
  - COBOL: Blijft bestaan vanwege de enorme hoeveelheid bestaande code.
  - REXX/CLIST: Zullen de komende 20 jaar niet verdwijnen uit legacy-systemen.
  - Nieuwe bouw: Alles wat nieuw wordt ontwikkeld, zal in moderne talen zoals Python gebeuren.

Kortom: REXX wordt een specialistische taal voor specifieke systeemtaken, terwijl Python de brede motor wordt voor automatisering en innovatie op het platform.
