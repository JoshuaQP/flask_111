#!/urs/bin/env python3
# -*- Coding:utf8 -*-
"""Simple flask app"""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def about_me():      #view function
    me = {
        "first_name": "Joshua",
        "last_name":"palmier",
        "hobbies": "DIY stuff"

    }
    return me

    