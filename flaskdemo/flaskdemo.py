# -*- coding:utf-8 -*-

import json
import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


book_columns = ['Id','Name','Release Date','Average Rating']
app = Flask(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskdemo.db'),
    DEBUG=True
))
app.config.from_envvar('FLASK_CONFIG', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('dbschema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def _prepare_data(results):
    """
    Prepares our result data in a form suitable for DataTables
    """
    aaData_rows = []
    output = {}

    for row in results:
        aaData_row = []
        for i in range(len(book_columns)):
            aaData_row.append(str(row[book_columns[i]]).replace('"', '\\"'))
        aaData_rows.append(aaData_row)
    output['aaData'] = aaData_rows

    return output


@app.route('/')
def index():
    return render_template('index.html', columns=book_columns )


@app.route('/_server_data')
def get_server_data():
    db = get_db()
    cur = db.execute('SELECT b.id, b.name, b.release_date, avg(r.rating) FROM books b, reviews r WHERE b.id = r.book_id GROUP BY b.id')
    entries = cur.fetchall()

    collection = []
    for entry in entries:
        collection.append(dict(zip(book_columns, entry)))
    results = _prepare_data(collection)

    return json.dumps(results)


@app.route('/reviews/<book_id>')
def get_reviews(book_id):
    db = get_db()
    cur = db.execute('SELECT r.review, r.rating FROM reviews r WHERE r.book_id = ?',book_id)
    reviews = cur.fetchall()
    review_columns = ['Review','Rating']
    return render_template('reviews.html', columns=review_columns, reviews=reviews)


if __name__ == '__main__':
    app.run()