# -*- coding: utf-8 -*-
"""
This module is all programs entrance.
It have menu.
"""
from flask import Flask, request, render_template

from ciphers import additive_cipher, multiply_cipher, affine_cipher


PATH_ROOT = "/"
PATH_LAB = "/lab/"
PATH_LAB_1 = PATH_LAB + "1"
PATH_LAB_2 = PATH_LAB + "2"
PATH_LAB_3 = PATH_LAB + "3"

PARAMS = (
    
    ("additive_key", 8),
    ("additive_data", "TEST STRING"),
    ("additive_result", None),

    ("radditive_data", "AS ASRRFW FF!"),
    ("radditive_result", None),

    ("mult_key", 11),
    ("mult_data", "test string".upper()),
    ("mult_result", None),
    
    ("rmult_data", "ADIAOSJDIJ AIOJSDIOAJOI"),
    ("rmult_result", None),

    ("affine_key", 8),
    ("affine_key2", 11),
    ("affine_data", "TEST STRING"),
    ("affine_result", None),

    ("raffine_data", "TEST STRING"),
    ("raffine_result", None),
)


app = Flask(__name__)


@app.route(PATH_ROOT)
def root_page():
    return render_template('main_page.html')

@app.route(PATH_LAB_1, methods=['GET', 'POST'])
def lab1_page():
    
    default_context = {}
    default_context['last_action'] = request.form.get("action", "additive")
    for param in PARAMS:
        default_context[param[0]] = request.form.get(param[0], param[1])

    if request.method == 'POST':
        try:
            print default_context['last_action']
            if default_context['last_action'] == 'additive':
                default_context['additive_result'] = additive_cipher(
                    default_context['additive_data'],
                    int(default_context['additive_key']),
                    reverse=False)
            elif default_context['last_action'] == 'radditive':
                default_context['radditive_result'] = additive_cipher(
                    default_context['radditive_data'],
                    1,
                    reverse=True)
            elif default_context['last_action'] == 'mult':
                default_context['mult_result'] = multiply_cipher(
                    default_context['mult_data'],
                    int(default_context['mult_key']),
                    reverse=False)
            elif default_context['last_action'] == 'rmult':
                default_context['rmult_result'] = multiply_cipher(
                    default_context['rmult_data'],
                    1,
                    reverse=True)
            elif default_context['last_action'] == 'affine':
                default_context['affine_result'] = affine_cipher(
                    default_context['affine_data'],
                    int(default_context['affine_key']),
                    int(default_context['affine_key2']),
                    reverse=False)
            elif default_context['last_action'] == 'raffine':
                default_context['raffine_result'] = affine_cipher(
                    default_context['raffine_data'],
                    1,
                    2,
                    reverse=True)
        except Exception, err:
            print err
    return render_template('labs/lab1.html', **default_context)


@app.route(PATH_LAB_2, methods=['GET', 'POST'])
def lab2_page():
    
    context = {}

    return render_template("labs/lab2.html", **context)


app.run(port=8002, debug=True, host='0.0.0.0', threaded=True)
