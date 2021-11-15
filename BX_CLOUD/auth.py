import functools
from . import getDB
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
import hashlib

bp = Blueprint('auth', __name__, url_prefix='/auth')

# @bp.route('/login',methods=('GET',"POST"))
# def login():
#     if request.method=='POST':
#         error=None
#         username=request.form['username']
#         password = request.form['password']
#         if not getDB.check_admin_db(username,password):
#             error="Can't login!"

#         if error is None:
#             session.clear()
#             session['username']= username
#             return redirect(url_for('index'))

#         flash(error)
#     return render_template('auth/login.html')
    
# @bp.before_app_request
# def load_logged_in_user():
#     user_id=session.get('username')

#     if user_id is None:
#         g.user = None
#     else:
#         g.user = 'TBX'


# @bp.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('index'))

# def login_required(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for('auth.login'))

#         return view(**kwargs)

#     return wrapped_view