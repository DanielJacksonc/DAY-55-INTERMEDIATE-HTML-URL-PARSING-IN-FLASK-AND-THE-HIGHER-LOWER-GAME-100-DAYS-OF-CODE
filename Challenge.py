""" In this challenge, we will use decorators to style our Flask"""

# lets do this
# import flask library
from flask import Flask

# initialise the app to the flask
app = Flask(__name__)

# STEPS: start by creating a decorator

def italics(function):
    def show():
        return f"<em>{function()}</em>"
    return show

def underlines(function):
    def show():
        return f"<u>{function()}</u>"

    return show
def bold(function):
    def show():
        return f"<b>{function()}</b>"

    return show





# start creating your web app
@app.route('/') # this is the home page
@italics
@underlines
@bold
def home():
    return ('<h1 style="text-align: center">Welcome to the home page</h1>'
            '<p>This is the continuation of our text, please don\'t mind us</p>'
            '<img src="https://media2.giphy.com/media/g5R9dok94mrIvplmZd/giphy.gif?cid=ecf05e47en7hpr6421l6enw1iiyob8yw5bthpj0c8kjdel9u&ep=v1_gifs_related&rid=giphy.gif&ct=g"  width="500" > ')

# create About page
@app.route('/about')

def about():
    return 'this webpage is for tutorial onl '
# create for contact
@app.route('/<name>/<int:number>')
def contact(name, number):
    return (f' Hi {name}, {number} Welcome, please see our contact address here+3545663, would you want us to anything for you,'
            f'ofcourse i can help')


if __name__ == "__main__":
    app.run(debug=True)


