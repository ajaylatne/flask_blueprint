from flask import Blueprint, render_template

client_bp = Blueprint('ClientBluePrint', __name__, template_folder='templates')


@client_bp.route('/cv1')
def client_view1():
    return render_template('client.html')
