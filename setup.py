# -*- coding: utf-8 -*-
import os, sys

__dir__ = os.path.dirname(os.path.abspath(__file__))
os.chdir(__dir__)

if not os.path.exists(os.path.join(__dir__, "env")):
    if sys.platform.startswith("linux"):
        # in case of linux
        os.system(f"{sys.executable} -m venv ./env")
        os.system(f"{os.path.join(__dir__, 'env', 'bin', 'python')} -m pip install -r ./requirements.txt")
    elif sys.platform.startswith("win"):
        # in case of windows
        # on windows, sometimes venv doesn't install pip even has no option "--without-pip"
        os.system(f"{sys.executable} -m pip install virtualenv")
        os.system(f"{sys.executable} -m virtualenv ./env")
        os.system(f"{os.path.join(__dir__, 'env', 'Scripts', 'python')} -m pip install -r ./requirements.txt")

if not os.path.exists(os.path.join(__dir__, "frontend", "node_packages")):
    os.chdir(os.path.join(__dir__, "frontend"))
    os.system("npm install")
