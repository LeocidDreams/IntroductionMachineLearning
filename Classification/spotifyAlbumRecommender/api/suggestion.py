# importing required libraries
from flask import Blueprint
from flask import render_template

bp=Blueprint("breed",__name__)

@bp.route('/suggestion')
def suggestion():
    abc={}
    return render_template('suggestion.html',**abc)