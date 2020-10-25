
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/penguins')
def favanimalpage():
    """Shows a message about peguins"""
    return "Penguins are cute!"


@app.route('/peregrine')
def myfavanimalpage():
    """Shows a message about the peregrine falcon"""
    return "Peregrine falcon's are wayyyy faster than you!"


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'


@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite animal."""
    return f'How did you know I liked {users_dessert}?'


@app.route('/madlibs/<adjective>/<noun>')
def mad_stories(adjective, noun):
    """Takes in 2 strings (adj and noun) and displays a funny story using them!"""
    return f' The {adjective} {noun} is running over the lazy dog!'


@app.route('/multiply/<number1>/<number2>')
def multiple_nums(number1, number2):
    """Takes in 2 numbers and displays it's product with a message"""
    if not number1.isdigit() or not number2.isdigit():
        return "Invalid inputs. Please try again by entering 2 numbers!"
    return f'{number1} times {number2} is {int(number1) * int(number2)}.'


@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    """Takes 2 arguements, the word and the number of times to repeat it. The repeated message is displayed"""
    if not n.isdigit():
        return "Invalid input. Please try again by entering a word and a number!"

    final_string = word
    for cycle in range(int(n)):
        final_string += f' {word}'
    return final_string


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
