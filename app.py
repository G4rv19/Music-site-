#importing Flask and templates for further use
from flask import Flask, render_template
# naming basic syntax
app = Flask(__name__)
#first route '/' or '/home' which will be homepage 
@app.route('/')
@app.route('/home')
#this def function will further take it to stuff inside the page.
def homepage():
    return render_template('index.html') # just an html template which will change the looks of webpage'/' aka homepage.

@app.route('/about') # another webpage which is called 'about'
def about():
    return render_template('about.html') #importing another template which will render it stuff.

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
#just last debugging syntax and website is done.
