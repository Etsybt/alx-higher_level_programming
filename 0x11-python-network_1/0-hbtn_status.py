#!/usr/bin/python3
"""cript that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if name == "main":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as req_back:
        page = req_back.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(type(page)))
        print("\t- utf8 content: {}".format(page.decode('utf-8')))
