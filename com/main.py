from flask import Flask
from com.admin import admin_file
from com.client import client_file

app = Flask(__name__)

app.register_blueprint(admin_file.admin_bp)
app.register_blueprint(client_file.client_bp)


@app.route('/')
def home_view():
    return 'home view'


if __name__ == '__main__':
    app.run(debug=True)
