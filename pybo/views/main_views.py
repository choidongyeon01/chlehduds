# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 11:41:52 2025

@author: choi dong yean
"""
from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix = '/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))


'''
from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix = '/')

@bp.route('/')
def hello_pybo():
    return 'Hello, Pybo!!!!!!!!'


@bp.route('/hello')
def test():
    return 'test test test'
'''

'''
'main'
=> Blueprint의 별칭


__name__
=> main_views

url_prefix = '/'
=> localhost:5000/

ex) url_prefix = '/main'
=> localhost:5000/main/
'''