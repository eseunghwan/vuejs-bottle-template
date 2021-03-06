# -*- coding: utf-8 -*-
import os

__dir__ = os.path.dirname(os.path.abspath(__file__))

# make dist of frontend
if os.path.exists(os.path.join(__dir__, "frontend", "package.json")):
    os.chdir(os.path.join(__dir__, "frontend"))
    os.system("npm run build")
    os.chdir(__dir__)

# run server
from backend.server import start_server
start_server("0.0.0.0", 47352, True)
