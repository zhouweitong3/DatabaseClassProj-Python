from flask import session, request, render_template, redirect, g
from . import routes
from utils.database import checkLogin


@routes.route('/')
def index():
    if "user" not in session:
        redirect("/login")
    return render_template('index.html')
    

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if checkLogin(g.dbConn, request.form['username'], request.form['password']):
            session["user"] = request.form['username']
            return redirect("/")
    
