Flask-AjaxDialogDemo
====================

This is a quick little Flask app I wrote which mashes together a few separate examples
of basic Flask usage:

* AJAX-based data population in tables.
* AJAX-based data population in dialog boxes.
* Use of DataTables for presenting table data.
* Use of SQLite for storing and presenting data.

The Flask example applications *minitwit* and *flaskr* as well as rosickey's flask-DataTables
examples served as a useful base for mashing these capabilities together.

### Installation ###

```bash
pip install --editable .
export FLASK_APP=flaskdemo
flask initdb
flask run
```

The application will be accessible from http://localhost:5000

### See Also ###

* https://github.com/pallets/flask
* https://github.com/rosickey/flask-datatables
