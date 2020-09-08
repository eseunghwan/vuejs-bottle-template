# -*- coding: utf-8 -*-
from bottle import get, post, request, json_dumps

@get("/fn/get")
def get_test():
    return json_dumps({ "message": "test!" })

@post("/fn/set")
def set_test():
    print(request.json)
