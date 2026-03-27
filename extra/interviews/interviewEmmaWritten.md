# Interview with Emma about Python and Rexx on Mainframe and RACF

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
