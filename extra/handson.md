# Code

## JCL Skeleton

```jcl
//{{ job_name }} JOB ({{ job_class }}),'{{ job_desc }}',CLASS={{ job_class }},
//             MSGCLASS={{ msg_class }},NOTIFY=&SYSUID
//STEP1    EXEC PGM={{ program }}
//SYSPRINT DD SYSOUT=*
//INPUT    DD DSN={{ input_dsn }},DISP=SHR
//OUTPUT   DD DSN={{ output_dsn }},DISP=(NEW,CATLG,DELETE),
//             SPACE=(CYL,(10,5)),UNIT=SYSDA
```

## Rexx code

```rexx
/* REXX script to generate JCL using file tailoring */

job_name = 'MYJOB01'
job_class = 'A'
job_desc = 'Sample JCL Generation'
msg_class = 'H'
program = 'IEFBR14'
input_dsn = 'MY.INPUT.DATASET'
output_dsn = 'MY.OUTPUT.DATASET'

/* Allocate input dataset to a DD name */
ADDRESS TSO "ALLOCATE DD(SKELDD) DSN('Z65305.THESIS.JCL(SKELETON)') SHR"
if RC <> 0 then do
  say 'Error: PDS Z65305.THESIS.JCL not found. Please create the PDS first.'
  exit
end

/* Allocate output dataset to a DD name (create if needed) */
/* First, check if dataset exists */
ADDRESS TSO "LISTCAT ENTRIES('Z65305.THESIS.JCL.RESULT')"
dataset_exists = (RC = 0)

/* Build the ALLOCATE command based on whether dataset exists */
if dataset_exists then do
  /* Dataset exists - overwrite it */
  ADDRESS TSO "ALLOCATE DD(OUTDD) DSN('Z65305.THESIS.JCL.RESULT'),
   OLD REUSE"
end
else do
  /* Dataset doesn't exist - create new */
  ADDRESS TSO "ALLOCATE DD(OUTDD) DSN('Z65305.THESIS.JCL.RESULT'),
   NEW SPACE(1,1) TRACKS RECFM(F B) LRECL(80) BLKSIZE(800)"
end

if RC <> 0 then do
  say 'Error allocating OUTDD: RC=' RC
  ADDRESS TSO "FREE DD(SKELDD)"
  exit
end

/* Read template from allocated DD */
ADDRESS TSO "EXECIO * DISKR SKELDD (STEM skel. FINIS"

/* Perform replacements on each line */
do i = 1 to skel.0
  line = skel.i

  /* Replace job_name */
  do while INDEX(line, '{{ job_name }}') > 0
    p = INDEX(line, '{{ job_name }}')
    line = SUBSTR(line, 1, p-1) || job_name || ' ' || SUBSTR(line, p+15)
  end

  /* Replace job_class */
  do while INDEX(line, '{{ job_class }}') > 0
    p = INDEX(line, '{{ job_class }}')
    line = SUBSTR(line, 1, p-1) || job_class || SUBSTR(line, p+15)
  end

  /* Replace job_desc */
  do while INDEX(line, '{{ job_desc }}') > 0
    p = INDEX(line, '{{ job_desc }}')
    line = SUBSTR(line, 1, p-1) || job_desc || SUBSTR(line, p+14)
  end

  /* Replace msg_class */
  do while INDEX(line, '{{ msg_class }}') > 0
    p = INDEX(line, '{{ msg_class }}')
    line = SUBSTR(line, 1, p-1) || msg_class || SUBSTR(line, p+15)
  end

  /* Replace program */
  do while INDEX(line, '{{ program }}') > 0
    p = INDEX(line, '{{ program }}')
    line = SUBSTR(line, 1, p-1) || program || SUBSTR(line, p+13)
  end

  /* Replace input_dsn */
  do while INDEX(line, '{{ input_dsn }}') > 0
    p = INDEX(line, '{{ input_dsn }}')
    line = SUBSTR(line, 1, p-1) || input_dsn || SUBSTR(line, p+15)
  end

  /* Replace output_dsn */
  do while INDEX(line, '{{ output_dsn }}') > 0
    p = INDEX(line, '{{ output_dsn }}')
    line = SUBSTR(line, 1, p-1) || output_dsn || SUBSTR(line, p+16)
  end

  out.i = line
end

/* Write to allocated DD */
ADDRESS TSO "EXECIO * DISKW OUTDD (STEM out. FINIS"

/* Free the DD names */
ADDRESS TSO "FREE DD(SKELDD)"
ADDRESS TSO "FREE DD(OUTDD)"

say 'JCL generated in Z65305.THESIS.JCL.RESULT'
```

## Python code

```python
from jinja2 import Template

# Define the JCL template as a string (or load from file)
jcl_template = """
//{{ job_name }} JOB ({{ job_class }}),'{{ job_desc }}',CLASS={{ job_class }},
//             MSGCLASS={{ msg_class }},NOTIFY=&SYSUID
//STEP1    EXEC PGM={{ program }}
//SYSPRINT DD SYSOUT=*
//INPUT    DD DSN={{ input_dsn }},DISP=SHR
//OUTPUT   DD DSN={{ output_dsn }},DISP=(NEW,CATLG,DELETE),
//             SPACE=(CYL,(10,5)),UNIT=SYSDA
"""

# Data to inject into the template
data = {
    'job_name': 'MYJOB01',
    'job_class': 'A',
    'job_desc': 'Sample JCL Generation',
    'msg_class': 'H',
    'program': 'IEFBR14',  # Dummy program for testing
    'input_dsn': 'MY.INPUT.DATASET',
    'output_dsn': 'MY.OUTPUT.DATASET'
}

# Render the template
template = Template(jcl_template)
rendered_jcl = template.render(data)

# Output the generated JCL
print(rendered_jcl)

# Optionally, save to a file
with open('generatedjob.jcl', 'w') as f:
    f.write(rendered_jcl)
```
