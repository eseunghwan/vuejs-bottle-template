# -*- coding: utf-8 -*-
import os, sys, shutil

__dir__ = os.path.dirname(os.path.abspath(__file__))
os.chdir(__dir__)

project_name = os.path.basename(__dir__)
dist_dir = os.path.join(__dir__, "build", project_name)

os.system(" ".join([
    sys.executable, "-m", "PyInstaller", "./start.py",
    "--workpath=./build/temp", "--distpath=./build",
    f"--name={project_name}", "--icon=./frontend/dist/favicon.ico",
    "--onedir", "--exclude-module=matplotlib", "--noconfirm", "--clean"
]))

os.mkdir(os.path.join(dist_dir, "frontend"))
shutil.copytree(
    os.path.join(__dir__, "frontend", "dist"),
    os.path.join(dist_dir, "frontend", "dist")
)
shutil.rmtree(os.path.join(__dir__, "build", "temp"))
