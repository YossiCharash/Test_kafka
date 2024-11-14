from flask import Flask
from routes.main_route import Email


app = Flask(__name__)


app.register_blueprint(Email)


if __name__ == '__main__':
    app.run()