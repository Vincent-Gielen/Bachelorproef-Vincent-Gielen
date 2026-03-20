# Use cases

## Co-promotor Bobby

- IPL LPAR
- Use API's

## Arthur Coucke

- Comparing ISPF Rexx File Tailoring services with skeletons against Python Jinja templating for generating JCL

## Discord

- Make a REST API call
- Set up a Dictionary
- Pull information out of SDSF
- Submit a Job and report output

### Form Responses

- One thing I’m currently working on is a REXX script to process SMF data. Eventually, I’d like to rewrite it in Python, but our shop hasn’t fully adopted it yet and we’re missing some key components (like ZOAU)
- REXX is great for generating routine JCL that only needs a few variables changed or designing new ISPF panels quickly
- My $0.02 on this is to use the language you are most comfortable using that provides the features you need.  If you are doing an ISPF dialog then REXX is your language due to its excellent interface to ISPF services, including panel/skel REXX. If your intended audience is primarily 3270 (TSO, TSO/ISPF) then use REXX - if your intended audience is shell based then use Python.
- I would not use REXX for anything that will be heavily used even if you have the REXX compiler - it is not truly a compiled/efficient language - I don't know about Python in this respect. But if the use case if for something used up to several times an hour compared to several times per minute, or second, then go with the interpreted language - for speed use C/C++/MetalC/BAL/...
- I use Python for RACF clean ups and security automation, it's fairly good at handling large amounts of data
- I was given the task of deleting 17000 RACF profiles at work and created a Python script with SEAR to delete them, really impressed the requestor that I was able to delete them so quickly
- At my current place of work I think REXX is most heavily used in 3 areas:

  1) System Automation (for startup/shutdown of LPARs and managing the correct dependencies of started tasks, what to do for certain messages in the log, that sort of things)
  2) ISPF stuff, both vendor provided and home grown panels and functions. There are not many ISPF apps you can start that don't have any REXX underneath the hood.
  3) I don't know what else to call it other than 'glue'. So little tools, bits and pieces, to perform small tasks in JCLs that are not worth writing a whole COBOL app for, but too difficult to do with SORT or IEB* utils.

- A fourth one is more specific to me because I use REXX extensively in my own build/deploy utility. I wrote a small collection of REXX's to perform COBOL compile, link-edit, DB2 bind, CICS phasein, regular IEBCOPY of members etc. etc.
- Python is most heavily used in automation that either originates from outside Z or has to perform some tasks that are not on Z. So when Azure pipelines run, or Ansible Automation Platform playbooks run, or something like that, it's quite often ssh to get into Z and then run Python to do stuff.
- And the other way around, when to perform a task on Z and there's need to call a REST API somewhere outside Z, it's way easier with Python (requests) than in REXX.
- And to expand upon what Lionel said: I wouldn't use either of them for heavy lifting (so no handling of millions of records, and no running high volume in parallel for throughput). Performance is one major reason, but others are ability to monitor, trace, debug, dump, a lot of the secondary functions that both aren't great at.
- I do think there’s something to be said about the performance of Python when dealing with complex data. We utilize Python to ingest a Syslog offload from the previous day, it reads millions of rows of data, parses it out to a hundreds of thousands of dictionaries, and sends it off to our logging platform all in a matter of seconds
- Adding my data point here. Stopped using REXX because it didn’t seem strategic for future talent. Primary use cases: Integrating zOS with other platforms, management automation, abstraction of complex tasks into simple module invocations, abstraction of legacy systems (RACF is the primary one here) to fit modern data structures (RACF Identities to SCIM identities). No shade to REXX, I used to be specifically REXX. I just think it would be a disservice to new talent who may not stick with Z to make them learn it.
- As a new sysprog myself, the transition from modern scripting languages to REXX is honestly fairly smooth. However, I’d definitely prefer to use Python
- Yeah most people who are handy with learning languages will be able to easily pivot once they know one or the other
- Nothing beats the PARSE command though, that thing is easily written and buttery smooth
- To Lionel’s point, one area where Python struggles is with ‘address command’ capbilities where there is no z/OS specific Python package. So ‘address ISPF’ xxx will cause you grief in Python. But others like ‘address sdsf’ - many of those features are available through Z Open Automation Utilities Python interfaces.
- If I look at my rexx PDS, the members that get used most often are named FIX1, FIX2, FIX3, etc.  Each is basically nothing but an EXECIO to read data into a stem variable, then a loop to go through every line, do something with that data, and spit that out to another dataset with a second EXECIO.  For example, I might take a list of tape volsers and make multiple-line RMM commands out of them. So basically, I use Rexx mostly for quick ad-hoc text work that would be difficult to do with the ISPF editor, DFSORT, etc

## Form

- Ability to integrate with other systems.
- Robustness/stability over longer period of time.
- Support from either software vendor or community.

- interface to ISPF File Tailoring works great in REXX - not in python.  ISPF Skeletons are ideal for JCL generation and filling in variables. Rexx is used to build tools that interface with the scores of ISPF services both for dialog management (DISPLAY, FTINCL, SETMSG, etc.) and library management (EDIT, LMMLIST, LMDDISP, etc.). Rexx is fully supported by ISPF, I am unaware if Python is.
- Any language is evenly well equipped for any task. However some tasks are just done easier in one language than the other. That being said, some language are just better at doing certain things than others.

- If we take z/OS environments as the 'domain of discourse' here and I would have to do a proper/honest MultiCriteria Analysis on REXX vs Python I think one should focus on the 'solution' the program has to give and the skillset available (now and in the future) of the people having to maintain the code.

- My 'advise' / 'gut feeling' on a couple of usecases:
  
  1. For ISPF applications -> REXX
  2. JCL Generation -> Python, especially since we have ZOAU now:)
  3. Report Generation (PDF,XLSX) -> Python
  4. Math based solutions -> Python
  5. Interfacing with MasterConsoles -> REXX
  6. Data Analysis -> Python

- PARSE and ADDRESS in REXX are extremely powerful, so I would be interested to see what the equivalent in Python are.
- Additionally, what are the security vulnerabilities one might introduce using Python packages."
- Since you are focusing on ZOS, the important consideration should be the ability to invoke system/platform and subsystems services like DFSMS, RACF, ZOS, ISPF, SDSF, WLM, DB2, USS, TSO etc.
- Second is Performance and CPU usage as on ZOS MIPS is still key for any evaluation.
- Also as a language how much robust it is and how much rich it is.
- A little bit harsh: Do you perfer to code everything yourself (REXX) or use other peoples packages (Python)
- Ease of reuse of your own code.
- Structuring of code
- Object orientation
- REXX stems vs lists of dict or objects
- Rexx is Native to the platform and easy to expand with own environments
- Integration with native z/OS tools: For example, whether the language can run within environments such as Netview, System Automation or be invoked directly from ISPF or TSO panels.
- Data access capabilities: The ease of working with z/OS datasets versus USS files, and how naturally each language interacts with these data structures.
- Availability of libraries: The breadth and maturity of built-in or add-on libraries that extend the language’s functionality.
- AI/LLM support: The effectiveness of Large Language Models when generating or assisting with code in each language, specifically how easily and accurately developers can create or customize scripts in Python versus REXX using LLM tools.
- Performance characteristics: CPU utilization and overall performance when performing comparable tasks on the platform.
- I think about using different environments like TSO, MVS, OPS/MVS, etc vs APIs.
- Code pages rexx full EBCDIC vs Python full UTF-8
- What it takes to complete a task: how much code do you need to write yourself in either language to accomplish the same goal
- how easy is it to build reusable capabilities
- how easy is it to understand the code after it is written by someone else new to the area
- how easy is it to make capabilities that can be shared across systems and organizations.  
- Ease of coding modern applications.
- How many lines of code are necessary to reach a certain goal.
- Recently we tried to use rexx to perform file read/writes into Unix System Services datasets.  We found that we did not have the add-on libraries installed.  This pre requisite setup should be done before a fair comparison of rexx can be done against python, as python provides these capabilities natively.
- As well you may wish to set context of the history of REXX and it's predecessor CLIST language.
- Amount of people proficient in each language
- API / command interfaces
- Amount of guides online
- Standard library functionality
- Cost, Python runs on zIIP
- Developer tooling, such as linters"
- Python on Z is still Python - with all of its packages, and data structures and object oriented design. It's flexible, powerful, extensible. But it's not Rexx.
- Rexx is closer to the operating system, has ISPF dialog services embedded in it, so that you can write online, interactive applications using panels, messages, skeletons and tables. None of that in Python.
- However, both are valid programming languages with benefits and drawbacks. Their use is dependent upon the application.
- python has many libraries which had in-built many functions whereas rexx has some dependency on OS version for execution.
- Like REXXis executed primarily on ZOS whereas python can execute on any OS.
- Being able to perform the task that is need but more specific is to interact with other services is the key. If the function depends on other libraries they should come with that service or be included in the OS.
- I think to make the shift we need to be able to convert so people new to the platform doesn't have to learn both just to maintain old routines. It should not be much hard to interact with the operating system in Python and making people write a lot of code defeats the purpose I would say.
- I tried to use USS tools on the mainframe, but I even have issues with EBCDIC code page translation. Specifically, when you use another code page than USA or IBM-1047, it becomes the true hell. So, in my opinion, the first objective should be to find the easiest way to write or interact with the languages.
  - Today, 3270 emulator do not integrate functions to easily interact with the USS world, and USS itself is not able to easily identify code written in other code pages. I know we can tag a file with a specific code page, but it’s not automatic — it’s fully manual.
  - I can give you a simple example: In an emulator using a French code page, if you write a JCL and add Python code in the instream like SYSIN *, you first need to convert your code to UTF-8 before executing it. Otherwise, you can have many problems, like variables not being handled correctly.
- Comparing how two languages can accomplish the same task not necessarily the same way just the same task
- how easy it is to maintain the code going forward
- how much new code is required
- Rexx has tremendous support on the mainframe, especially z/VM where it is absolutely integral. Rexx is somewhat less significant on z/OS, it was not as popular with system programmers there.
- Python enthuses the younger generation, and will be the overwhelming choice for system programming scripting going forwards.
- I think the most important thing is that almost all of the young talents who are interested in mainframes know Python, and hardly anyone knows REXX. That's why future script programs should be written in Python whenever possible. IBM itself is also moving strongly in this direction.
- I feel both tools are equally powerful.  I am in the minority in this thinking ...however usage could depend on a number of factors. Here are a few thoughts on some of them.
- Many shops will have an established Rexx procedures and I have yet to see a justification to rewrite all of them in python.  The approach in these environments should be to use what makes sense. If the person building the script is proficient in python, then go that way. However an important thing to consider is IF that same person will be supporting the script... If it will be supported by a team of REXXperts, then the script may be more maintainable in rexx.
- IBM ships many products with Rexx example source code to help integrate and set up. In this scenario, if time to market is important, customizing the sample rexx is much faster than re-engineering in python.
- regular expressions: although rexx parsing is powerful for fixed length strings, it can be difficult to code. any use case requiring regex can be easier to maintain in python vs creating the function in rexx.
- performance: rexx is interpreted, but attempts at compilation do exist but are rarely used. This requires additional IBM libraries to set up. These executables (and interpreted rexx as well) run on general purpose CPUs (GCPs) and could contribute to monthly CPU consumption charges to IBM. This could translate into dollars. python is zIIP eligible (special processor) up to 98 percent. Clients do not pay for zIIP compute cycles, so building new functionality in python can be cheaper from an execution standpoint.
- The technology side of rexx vs python is one thing, but the ""IT Economics"" is an equally important consideration you won't hear about from some technical people.  Often times when I am solutioning for internal clients at the bank, run cost or (total cost of ownership-TCO) is an important and often deciding factor.

- I think Python is better suited for Dev Ops, where the work originates elsewhere (Say a PC) and connects to the mainframe.  Where REXX is better for on prem z/OS scripting.  Python is still having more support added to on prem (eg, TSO) but REXX shines there.  
- Array/Stem manipulation.  Loop/If-Then/Select syntax level readability, dependencies on external libraries, depth of external libraries.  Ease of interfacing with OS.  
- Lines of code to provide equivalent function. Readability and maintainability of equivalent code, slightly subjective this, but a qualitative assessment could possibly be made. Elapsed time performance for running the function. Resource consumption (CPU and zIIP consumption). Ease of use e.g. REXX can be launched easily from the TSO command interface or in batch, I think Python is launched through OMVS, SSH or BPXBATCH which mainframe people generally try to avoid, slightly subjective this, mainframe people are far more familiar with 3270, TSO and ISPF as an interface, non mainframe people probably prefer SSH or OMVS. Level of integration with z/OS e.g. REXX has good integration with z/OS datasets, ISPF, USS, SDSF, z/OS, Db2, IPCS etc, I'm not sure about Python. General restrictions and built in functions e.g. REXX can easily invoke other REXX or compiled program objects from Assembler, Cobol etc, I don't know whether Python can easily do the same. You mentioned Fail tailoring for 3) above, but File Tailoring is an ISPF function not a REXX function, I'm not sure what I would pick as an example application, ideally you would want it to run for minutes rather than fractions of a second so that comparisons can be made, maybe something that searches z/OS Catalogs to retrieve a selective list of datasets and then attempts to total the space used (or something like that).
- Both languages have a solid place and really don't need to be compared with each other.  
- It seems a reasonable subject, I suspect most mainframe sites would be interested in potentially converting REXX to Python, provided it can provide equivalent functionality with no loss of ease of use, and no performance or resource penalties, because programmers are more plentiful than REXX programmers.
