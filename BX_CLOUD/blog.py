from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from werkzeug.utils import send_file, send_from_directory
from werkzeug.wrappers.response import Response
import json


import os
bp = Blueprint('blog', __name__)


@bp.route('/',methods=('GET','POST'))
def index():

    if request.method=='POST':
        def send_file(file):
            source_path="BX_CLOUD/files/private/"+file
            with open(source_path,'rb') as targetfile:
                while True:
                    data=targetfile.read(20*1024*1024)
                    if not data:
                        break
                    yield data

        error=None
        filename=request.form['filename']
        password=request.form['password']
        file_db="BX_CLOUD/db/files.json"
        with open(file_db,'rb') as f:
            load_dict=json.load(f)

            if filename not in load_dict:
                error="Can't find the file!"
            else:
                if load_dict[filename]==password:
                        response=Response(send_file(filename),content_type="application/octet-stream")
                        response.headers["Content-disposition"] = 'attachment; filename=%s' % filename
                        return response
                else:
                    error="False Password!"
        return error
    posts=os.listdir('BX_CLOUD/files/public/')
    return render_template('blog/index.html', posts=posts)



@bp.route('/download/<string:file>',methods=('GET','POST'))
def download(file):
    def send_file():
        source_path="BX_CLOUD/files/public/"+file
        with open(source_path,'rb') as targetfile:
            while True:
                data=targetfile.read(20*1024*1024)
                if not data:
                    break
                yield data

    response=Response(send_file(),content_type="application/octet-stream")
    response.headers["Content-disposition"] = 'attachment; filename=%s' % file
    return response