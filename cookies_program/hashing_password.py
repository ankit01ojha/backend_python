import random
import string
import hashlib

def make_salt():
    s = ""
    for i in range(0,5):
        s = s+s.join(random.choice(string.letters))
    return s

def make_pw_hash(name, pw):
    salt=make_salt()
    hpw = hashlib.sha256(name+pw+salt).hexdigest()
    return "%s,%s" % (hpw, salt)



def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h,salt)

def valid_pw(name, pw, h):
    salt = h.split(",")[1]
    if make_pw_hash(name,pw,salt)==h:
        return True
    else:
        return False
