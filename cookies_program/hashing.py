import hashlib
import hmac

SECRET="legend" #it is the string that we gonna add to make our hash more secure as no one knows what is the extra string we have added


def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()


def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))


def check_secure_val(h):

    val = h.split("|")[0]
    if make_secure_val(val) == h:
        return val



