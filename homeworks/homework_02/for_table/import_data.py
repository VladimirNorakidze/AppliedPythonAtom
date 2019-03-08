#!/usr/bin/env python
# coding: utf-8

import json


def opening(filename):
    coding = ""
    if "cp1251" in filename.lower():
        coding = "cp1251"
    elif "utf8" in filename.lower():
        coding = "utf8"
    elif "utf16" in filename:
        coding = "utf16"
    try:
        with open(filename, "r", encoding=coding) as f:
                data = json.load(f)
                json_status = True
    except json.decoder.JSONDecodeError:
        with open(filename, "r", encoding=coding) as f:
            data = f.read()
            json_status = False
    except FileNotFoundError:
        raise FileNotFoundError("Файл не валиден")
    return data, json_status
