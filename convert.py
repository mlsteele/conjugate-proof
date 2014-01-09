#!/usr/bin/env python
"""
Convert proof.md to proof.py
"""

MD_FILEPATH = "proof.md"
PY_FILEPATH = "proof.py"

md_file = open(MD_FILEPATH)
py_file = open(PY_FILEPATH, "w")

reading_code = False
for line in md_file:
  if reading_code:
    if line.startswith("```"):
      reading_code = False
    else:
      py_file.write(line)
  else:
    if line.startswith("``` python"):
      reading_code = True
    else:
      if line == "\n":
        py_file.write(line)
      else:
        py_file.write("# " + line)

md_file.close()
py_file.close()
