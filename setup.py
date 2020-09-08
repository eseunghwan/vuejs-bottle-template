# -*- coding: utf-8 -*-
import os, sys

__dir__ = os.path.dirname(os.path.abspath(__file__))
os.chdir(__dir__)

if not os.path.exists(os.path.join(__dir__, "env")):
    os.system(f"{sys.executable} -m pip install virtualenv")
    os.system(f"{sys.executable} -m virtualenv ./env")
    os.system(f"{os.path.join(__dir__, 'env', 'Scripts', 'python')} -m pip install -r ./requirements.txt")

os.chdir(os.path.join(__dir__, "frontend"))
os.system("npm install")
