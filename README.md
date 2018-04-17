# excel2html
this is a demo program for showing how to load/import data from a
excel sheet and to present the data with a table in webpage.

## setup
setup a python 3.6 (only tested with 3.6) virtualenv
and then run:
>    pip install -r requiremens.md

## run program
this is a web service program, so a "modern" browser is needed to
launch to see the presentation page.
start the web service:
>    python app.py

then access http://127.0.0.1:5000/ with a browser(chrome tested to
be ok)
a table with simple searching/ordering enable with show.(filtering
not available for now)
loading paging at the first time will take a while to download both
the css and js dependences.

## source data
the source data file is stored in $PROGRAM_ROOT/datas/test_data.xls.
