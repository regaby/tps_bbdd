#!/usr/bin/env python3
import configparser
from bottle import route, run, template, get, post, error
import psycopg2

CONFIG = configparser.ConfigParser()
CONFIG.read('hello_world.conf')
USER = CONFIG['hello_world']['user']
PASS = CONFIG['hello_world']['pass']
DB = CONFIG['hello_world']['db']
HOST = CONFIG['bottle']['host']
PORT = CONFIG['bottle']['port']
DEBUG = CONFIG['bottle']['debug']

@route('/ciudades')
def get_all_cities():
    # CONNECTION = cx_Oracle.connect(USER, PASS)
    CONNECTION = psycopg2.connect(user=USER,
                                  password=PASS,
                                  host="127.0.0.1",
                                  port="5432",
                                  database=DB)
    CURSOR = CONNECTION.cursor()
    CURSOR.execute("""SELECT * from ciudades;""")
    result = CURSOR.fetchall()
    col_names = [row[0] for row in CURSOR.description]
    CURSOR.close()
    return template("views/all_salaries", col_names=col_names, rows=result)

@route('/')
@route('/welcome/<name>')
def greet(name='Stranger'):
    return template('Welcome {{name}}', name=name)

@get('/login') # o @route('/login')
def login():
    return """
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    """

@post('/login') # o @route('/login', method='POST')
def do_login():
    return "Login correct"

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host=HOST, port=PORT, debug=DEBUG)
