import random
from flask import Flask

# generate a random number
numbers = random.randint(0,9)
app = Flask(__name__)
# create a decorator
def h1(function):
    def wrapper():
        return f'<h1 style="text-align: center">{function()}</h1>'
    return wrapper

""" up for all the deforators"""

@app.route('/')
@h1
def guess_number():
    return ('Guess a number between 0 and 9\''
            '<p><img src ="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="400"></p>' )




@app.route("/<int:number>")
def answer(number):
    if number < numbers:
        return (f"<h1 style='color: red'>Too Low,try again.You chose {number} the answer is {numbers}<h1>"
                f"<img src ='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='400'>")
    elif number > numbers:
        return (f"<h1 style='color: purple'>Too high,try again.You chose {number} the answer is {numbers}<h1>"
                f"<img src ='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='400'>")
    else:
        return (f"<h1 style='color: green'>You got it.You chose {number} the answer is {numbers}<h1>"
                f"<img src ='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='400'>")









if __name__ == "__main__":
    app.run(debug=True)

