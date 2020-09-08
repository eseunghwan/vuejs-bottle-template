# -*- coding: utf-8 -*-

def read_config(config_file:str):
    with open(config_file, "r", encoding = "utf-8") as cr:
        cl = [line for line in cr.readlines() if not line.strip() == ""]

    return {
        line.split("=")[0]: line.split("=")[1]
        for line in cl
    }
