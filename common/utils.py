import pytz, datetime
from flask import request
import random, string


def get_request_ip():
    if request.headers.getlist("X-Forwarded-For"): ip = request.headers.getlist("X-Forwarded-For")[0]
    else: ip = request.remote_addr
    return ip

def random_string(str_len):
    #http://stackoverflow.com/a/23728630/2213647
    rand_str = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(str_len))
    return rand_str


def split_username(username):
    if "\\" in username:
        domain, username = username.split("\\")[:2]
    elif "@" in username:
        username, domain = username.split("@")[:2]
    else:
        username = username
        domain   = ""
    return username, domain.lower()