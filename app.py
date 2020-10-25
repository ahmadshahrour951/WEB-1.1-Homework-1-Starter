
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


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
