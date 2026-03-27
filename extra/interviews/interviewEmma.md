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

## Interview uitgeschreven

- What are Rexx and Python used for on Mainframe in your point of view?

Rexx is used for z/OS Security because it's sometimes the only language available in those environments. Python is primarily used for automation, and for access to the USS environment. One-off Rexx scripts are popular, but you could do that with Python as well, like I do.
A huge benefit of scripting in Python is access to the "argparse" command, which is incredibly powerful for handling command line arguments. In Rexx, you would have to hardcode those, which is a lot less flexible.

- Since security (RACF) is your field of expertise, how do you see the use of both languages?

In my opinion Rexx isn't very good in RACF. Python has so many more built-in utilities that make it a lot easier to work with.
I use Python for RACF clean ups and security automation, it's fairly good at handling large amounts of data.
I was given the task of deleting 17000 RACF profiles at work and created a Python script with SEAR to delete them. This would not be possible with Rexx.

- Many people are worried about the dependency problem with Python. So many external libraries can cause security issues, as well as the possibility for different teams using different versions of a package.

Having access to more tools isn't a bad thing. To put it bluntly: If you don't know how to use it, you shouldn't touch it. It's always best to avoid unnecessary dependencies. You should always check the Python standard library first. If it's not in the standard library, you could try to find an established external package. If there is a big community for it, changes are it's probably fine. In the worst case, you can build it yourself, which is a lot easier to do in Python than in Rexx. So even if there is no 3rd party languages, core Python is still great.

- So how do you see the future of Automation (languages) on the mainfrane platform?

In the next 20 years we won't see Rexx (or Clist, the predecessor of Rexx) go away. But if somebody wants to build something new, it will, or should be, in Python. Maintaining new languages is so much easier, so building infrastructure (automation) will be done using new languages and technologies.
On top of that, data science/analysis, one-off financial reports and much more, are all done in Python. So there are so many more people who now Python than any of the older languages. If you want to attract new talent, you have to use the languages they know.
Python is also more fully featured. It has all sorts of stuff built in that Rexx doesn't have. Even just converting variables is way easier in Python. Rexx in general is so much tougher to work with, which defeats the purpose of scripting.
Lastly, Python used to be relatively slow, but it has gotten a lot faster.

- What about access to Python on the z/OS platform?

API access is still a real problem for Python. ZOAU is constantly adding more though, it's growing. It'll probably be a while before we have all the Python or Linux functionalities in z/OS. But the good thing for companies adopting Python now and being early is, you won't have to do a lot when more and more functionality becomes available. You will already have the knowledge and experience to use it, while others will have to start from scratch when they want to adopt Python later on.
