
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
from flask import Flask

app = Flask(__name__)
if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
