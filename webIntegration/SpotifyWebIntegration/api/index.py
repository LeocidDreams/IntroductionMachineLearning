from flask import Blueprint,render_template,jsonify


#creating blueprint object
bp=Blueprint('index',__name__)

@bp.route('/')
def index():
    return render_template('index.html')
