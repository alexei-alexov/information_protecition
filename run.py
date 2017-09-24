# -*- coding: utf-8 -*-
"""
This module is all programs entrance.
It have menu.
"""
from flask import Flask, request, render_template

from helpers import input, range_validator
from ciphers import main as ciphers_main


MENU_OPTIONS = (("Lab #1. Ciphers.", ciphers_main),)

PATH_ROOT = "/"
PATH_LAB = "/lab/"
PATH_LAB_1 = PATH_LAB + "1"
PATH_LAB_2 = PATH_LAB + "2"
PATH_LAB_2 = PATH_LAB + "3"


app = Flask(__name__)


@app.route(PATH_ROOT)
def root_page():
    return render_template('main_page.html')

@app.route(PATH_LAB_1)
def lab1_page():
    return render_template('labs/lab1.html')


app.run(port=8002, debug=True, host='0.0.0.0', threaded=True)

menu_text = "Hello!Please, choose lab #:\n"
menu_additional_text = u"\n".join(["[{}]".format(n) + option_text for n, (option_text, _) in enumerate(MENU_OPTIONS)])
print repr(menu_text)
answer = input(menu_additional_text, 0, range_validator(0, len(MENU_OPTIONS)))
MENU_OPTIONS[answer][1]()


