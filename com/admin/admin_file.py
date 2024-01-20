from flask import Blueprint, render_template

admin_bp = Blueprint('AdminBluePrint', __name__, template_folder='templates')


@admin_bp.route('/av1')
def admin_view1():
    return render_template('admin.html')
