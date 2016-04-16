git2img
=======
A utility for git repository to create image/binary/...

Usage
-----
python3 git2img.py

Structure
---------
git2img.py
    * Main entry

makelist.ini.sample
    * Repositories to be built

config.ini.sample
    * Not implemented yet

builders.py
    * some builders, including PythonBuilder, Cbuilder

libraries.py
    * some libraries, including class_for_name

Procedure
---------
prepare
    * After prepared, the stamp file of the jobs are created.

configure
    * After configured, the stamp file of the jobs are created.

compile
    * After compiled, the stamp file of the jobs are created.

install
    * After installed, the stamp file of the jobs are created.
