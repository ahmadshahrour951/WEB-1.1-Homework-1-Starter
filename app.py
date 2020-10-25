
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


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
