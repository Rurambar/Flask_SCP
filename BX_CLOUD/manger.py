#文件管理系统
import json
import os
import random
import string
import click
from flask.cli import with_appcontext
from flask import current_app
source="BX_CLOUD/db/files.json"
path="BX_CLOUD/files/private"

@click.command("updateDB")
@with_appcontext
def update():
    up()

def up():
    try:
        load_dict={}
        with open(source,'r') as f:
            load_dict=json.load(f)
        with open(source,'w') as f:
            for filename in os.listdir(path):
                if filename not in load_dict:
                    load_dict[filename]=random.sample(string.ascii_letters + string.digits, 6)


            json.dump(load_dict,f)
        print("已更新文件列表")
    except json.decoder.JSONDecodeError as e:
        print(e)
        with open(source,'w') as f:
            load_dict={}
            for filename in os.listdir(path):

                load_dict[filename]="".join(random.sample(string.ascii_letters + string.digits, 8))


            json.dump(load_dict,f)
        print("已生成文件列表")


@click.command("getFiles")
@with_appcontext
def getDB():
    with open(source,'r') as f:
        load_dict=json.load(f)
        print(load_dict)

def updateDB(app):
    app.cli.add_command(update)

def getFiles(app):
    app.cli.add_command(getDB)