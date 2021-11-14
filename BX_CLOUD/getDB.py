import json
import hmac
import hashlib

from werkzeug.security import check_password_hash, generate_password_hash
admin_db="BX_CLOUD/db/admin.json"
def check_admin_db(name,key):
    with open(admin_db,'r') as f:
        load_dict=json.load(f)

        if name in load_dict:
            if load_dict[name]==key:
                return True
    
    return False
