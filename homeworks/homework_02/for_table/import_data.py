#!/usr/bin/env python
# coding: utf-8

import json


def opening(filename):
    coding = ""
    json_status = False
    if "cp1251" in filename.lower():
        coding = "cp1251"
    elif "utf8" in filename.lower():
        coding = "utf8"
    try:
        with open(filename, "r", encoding=coding) as f:
                data = json.load(f)
                json_status = True
    except json.decoder.JSONDecodeError:
        with open(filename, "r", encoding=coding) as f:
            data = f.read()
            json_status = False
    return data, json_status
