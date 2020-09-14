# -*- coding: utf-8 -*-
from .Index import get_test, set_test

def register(bottle_app):
    bottle_app.get("/fn/get", callback = get_test)
    bottle_app.post("/gn/set", callback = set_test)
