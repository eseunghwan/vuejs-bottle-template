# -*- coding: utf-8 -*-
from bottle import request, json_dumps

def get_test():
    return json_dumps({ "message": "test!" })

def set_test():
    print(request.json)
