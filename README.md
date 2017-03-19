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

### Docker-based build ###

The accompanying Dockerfile can be used to create a Docker image.

An example of building:
```bash
docker build -t flaskdemo:latest .
```

Using the 'flask initdb' steps outlined in the installation documentation,
create the test database and move that to a path which will become our shared
volume.

```bash
flask initdb
cp flaskdemo/flaskdemo.db /data/flaskdemo/flaskdemo.db
```

Create a configuration file in the same location which will be shared with
running instances:

```bash
echo 'DATABASE="/data/flaskdemo/flaskdemo.db"' >
/data/flaskdemo/flaskdemo.conf'
```

Run the docker image with a port mapping and volume sharing:

```bash
docker run -d -p 80:5000 --name flaskdemo -v /data:/data flaskdemo:latest
```

### See Also ###

* https://github.com/pallets/flask
* https://github.com/rosickey/flask-datatables
