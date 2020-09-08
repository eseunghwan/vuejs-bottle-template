# -*- coding: utf-8 -*-
import os, sys, shutil

__dir__ = os.path.dirname(os.path.abspath(__file__))
os.chdir(__dir__)

# get project name
project_name = os.path.basename(__dir__)

# set dist dir
dist_dir = os.path.join(__dir__, "build", project_name)

# make dist of frontend
if os.path.exists(os.path.join(__dir__, "frontend", "package.json")):
    os.chdir(os.path.join(__dir__, "frontend"))
    os.system("npm run build")
    os.chdir(__dir__)

# make dist of backend
os.system(" ".join([
    sys.executable, "-m", "PyInstaller", "./start.py",
    "--workpath=./build/temp", "--distpath=./build",
    f"--name={project_name}", "--icon=./frontend/dist/favicon.ico",
    "--onedir", "--exclude-module=matplotlib", "--noconfirm", "--clean"
]))

# create frontend and copy dist
os.mkdir(os.path.join(dist_dir, "frontend"))
shutil.copytree(
    os.path.join(__dir__, "frontend", "dist"),
    os.path.join(dist_dir, "frontend", "dist")
)

# remove temp
shutil.rmtree(os.path.join(__dir__, "build", "temp"))
