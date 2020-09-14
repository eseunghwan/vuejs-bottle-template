# -*- coding: utf-8 -*-
import os, threading, requests, webbrowser, signal
from bottle import Bottle, run, route, static_file, template, redirect
from . import __path__, fn

backend_dir = __path__[0]
root_dir = os.path.dirname(backend_dir)
frontend_dir = os.path.join(root_dir, "frontend")

bottle_app = Bottle()

@bottle_app.route("/state")
def get_state():
    return True

@bottle_app.route("/")
def get_index():
    if os.path.exists(os.path.join(frontend_dir, "dist", "index.html")):
        index_file = "index.html"
    else:
        index_file = "Index.html"

    return static_file(index_file, root = os.path.join(frontend_dir, "dist"))

@bottle_app.route("/<view_name>")
def get_view(view_name:str):
    view_name_only = os.path.splitext(view_name)[0]
    if view_name == view_name_only or view_name.endswith(".html"):
        view_file = f"{view_name_only}.html"
    else:
        view_file = view_name

    return static_file(view_file, root = os.path.join(frontend_dir, "dist"))

@bottle_app.route("/<static_file_path:path>")
def get_static_files(static_file_path:str):
    return static_file(static_file_path, root = os.path.join(frontend_dir, "dist"))

@bottle_app.post("/stop")
def stop_server():
    os.kill(os.getpid(), signal.SIGTERM)

fn.register(bottle_app)

def __start_server(host, port):
    run(app = bottle_app, host = host, port = port, quiet = False)

def start_server(host:str, port:int, open_browser:bool = False, wait_server:bool = True):
    threading.Thread(target = __start_server, args = [host, port], daemon = True).start()

    while True:
        try:
            requests.get(f"http://127.0.0.1:{port}/state")            
            if open_browser:
                webbrowser.open_new(f"http://127.0.0.1:{port}")

            break
        except requests.ConnectionError:
            pass

    if wait_server:
        try:
            while True:
                pass
        except KeyboardInterrupt:
            stop_server()
