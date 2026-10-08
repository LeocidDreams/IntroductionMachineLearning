from flask import Blueprint,render_template

#defining Blueprint object
bp=Blueprint('index',__name__)

@bp.route('/')
def index():
    return render_template('index.html')

