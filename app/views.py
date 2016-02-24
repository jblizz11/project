"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
from app import app
from flask import render_template, request, redirect, url_for, json, session,flash
from werkzeug import generate_password_hash, check_password_hash

app.secret_key = 'why would I tell you my secret key?'

from app import db
from app.models import User
from .forms import profileform

###
# Routing for your application.
###


@app.route('/theform', methods=["GET", "POST"])
def theform():
    form = profileform()
    return render_template('theform.html', form=form)
    

@app.route('/profile/')
def profile():
    """profile add"""
    if session['logged_in'] == True:
        return render_template("profile.html")
    return redirect(url_for('login'))   
    
@app.route('/add', methods=['POST'])
def add_entry():
    """add a file"""
    title = request.form['title']
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join("app/static/uploads", filename))
    return render_template("profile.html",title=title)
    #g.db.execute('insert into entries (title, text) values (?, ?)',
    #             [title, filename])
    #g.db.commit()
    #flash('New entry was successfully posted')
    #return redirect(url_for('show_entries'))
    
    
def fileiterate():
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads'):
        for file in files:
            filepath = os.path.join(subdir, file)
    return files 
    
    
@app.route('/login', methods=['POST','GET'])
def login():
    error = None 

    if request.method == 'POST':
        if request.form['username'] != "admin":
            error = 'Invalid username' 
        elif request.form['password'] != "aa":
            error = 'Invalid password' 
        else: 
            session['logged_in'] = True
            flash('You were logged in') 

    return render_template("login_form.html",error=error)

  
  
@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

@app.route('/profiles')
def profiles():
     """Render the website's profile page and also get the current date."""
    result= time.strftime("%a, %d %b %Y ");
    return render_template('profiles.html',timereal=result)
    
    
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


    
    
@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
