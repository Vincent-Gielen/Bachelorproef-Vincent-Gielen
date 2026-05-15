# Commands

verander tag van een file:
`chtag -tc 819 eenscript.py`

verander inhoud van een file naar andere tag en steek het in een andere file:
`iconv -f 1047 -t 819 -T APIOffMainframe.py > APIOffMainframe819.py`

bekijk dump van een file:
`od -X filenaam`

activeer virtual environment:
`. venv/bin/activate` OR `. venv/Script/activate`

selecteer member in list op ISPF:
`s <membername>`

kopieer een USS file naar dataset
`result = subprocess.run(['/bin/cp', '-P', 'RECFM=FB,LRECL=80', '/tmp/inactive.txt', f"//'{dataset}'"], capture_output=True, text=True)`