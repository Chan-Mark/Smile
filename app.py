from flask import Flask, render_template, request, session
import sqlite3
from sqlite3 import Error

DB_NAME = "smile_db"

app = Flask(__name__)


def create_connection(db_file):
    """create a connection to the sqlite db"""
    try:
        connection = sqlite3.connect(db_file)
        # intialise_tables(connection)
        return connection
    except Error as e:
        print(e)

    return None

@app.route('/')
def render_homepage():
    return render_template("home.html")


@app.route('/menu')
def render_menu_page():

    # connect to the database
    con = create_connection(DB_NAME)

    # SELECT the things you want from your table(s)
    query = "SELECT name, description, volume, price, image FROM product"

    cur = con.cursor() # You need this line next
    cur.execute(query) # This line actually executes the query
    product_list = cur.fetchall() # Puts the results into a list usable in python
    con.close()

    return render_template("menu.html", products = product_list)


@app.route('/contact')
def render_contact():
    return render_template("contact.html")


app.run(host="0.0.0.0")
