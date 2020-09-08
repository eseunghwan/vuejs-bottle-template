# -*- coding: utf-8 -*-
import os, threading, requests, webbrowser, signal
from bottle import run, route, static_file, template, redirect
from . import __path__, fn, utils

backend_dir = __path__[0]
root_dir = os.path.dirname(backend_dir)
frontend_dir = os.path.join(root_dir, "frontend")


@route("/state")
def get_state():
    return True

@route("/")
def get_index():
    return static_file("index.html", root = os.path.join(frontend_dir, "dist"))

@route("/<view_name>")
def get_view(view_name:str):
    view_name_only = os.path.splitext(view_name)[0]
    if view_name == view_name_only or view_name.endswith(".html"):
        view_file = f"{view_name_only}.html"
    else:
        view_file = view_name

    return static_file(view_file, root = os.path.join(frontend_dir, "dist"))

@route("/<static_file_path:path>")
def get_static_files(static_file_path:str):
    return static_file(static_file_path, root = os.path.join(frontend_dir, "dist"))


def __start_server(host, port):
    run(host = host, port = port, quiet = False)

def start_server(host:str, port:int):
    threading.Thread(target = __start_server, args = [host, port], daemon = True).start()

    while True:
        try:
            requests.get(f"http://127.0.0.1:{port}/state")
            webbrowser.open_new(f"http://127.0.0.1:{port}")
            break
        except requests.ConnectionError:
            pass

    try:
        while True:
            pass
    except KeyboardInterrupt:
        os.kill(os.getpid(), signal.SIGTERM)
