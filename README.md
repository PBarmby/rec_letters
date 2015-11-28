# rec_letters
script for generating recommendation letters

Generates a set of related latex documents, with different 

* addressee 
* postal address
* saluation
* name of job
* institution

The above fields are listed in the "address" file, a sample of which is in `sample_address`. 
The script `rec_script.py` inserts these into a template LaTeX file as macros and runs LaTeX on the resulting file.
Usage: `python rec_script sample.tex sample_address`, which produces `sample_misk_su.tex` and `sample_misk_su.pdf`.
