from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from BX_CLOUD.auth import login_required


import os
bp = Blueprint('blog', __name__)


@bp.route('/')
@login_required
def index():
    posts=os.listdir('BX_CLOUD/files')
    return render_template('blog/index.html', posts=posts)

@bp.route('/<string:file>/download',methods=('GET','POST'))
@login_required
def download(file):
    return "FILE"