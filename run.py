# -*- coding: utf-8 -*-
"""
This module is all programs entrance.
It have menu.
"""
from flask import Flask, request, render_template

from ciphers import additive_cipher, multiply_cipher, affine_cipher, Playfair, Foursquare


PATH_ROOT = "/"
PATH_LAB = "/lab/"
PATH_LAB_1 = PATH_LAB + "1"
PATH_LAB_2 = PATH_LAB + "2"
PATH_LAB_3 = PATH_LAB + "3"
PATH_LAB_4 = PATH_LAB + "4"

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

    ("swaper_key", "3, 1, 4, 5, 2"),
    ("swaper_data", "TEST STRING"),
    ("swaper_result", None),

    ("rswaper_key", "3, 1, 4, 5, 2"),
    ("rswaper_data", "TEST STRING"),
    ("rswaper_result", None),
)

PARAMS_2 = (
    ("plaifair_key", None),
    ("playfair_data", "TEST STRING"),
    ("playfair_result", None),

    ("rplaifair_key", None),
    ("rplayfair_data", "TEST STRING"),
    ("rplayfair_result", None),

    ("foursquare_key1", None),
    ("foursquare_key2", None),
    ("foursquare_data", "TEST STRING"),
    ("foursquare_result", None),

    ("rfoursquare_data", "TEST STRING"),
    ("rfoursquare_key1", None),
    ("rfoursquare_key2", None),
    ("rfoursquare_result", None),
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
            print(err)
    return render_template('labs/lab1.html', **default_context)


@app.route(PATH_LAB_2, methods=['GET', 'POST'])
def lab2_page():
    
    context = {}
    default_context['last_action'] = request.form.get("action", "playfair")
    for param in PARAMS:
        default_context[param[0]] = request.form.get(param[0], param[1])

    if request.method == 'POST':
        try:
            if default_context['last_action'] == 'playfair':
                default_context['additive_result'] = additive_cipher(
                    default_context['additive_data'],
                    int(default_context['additive_key']),
                    reverse=False)
            elif default_context['last_action'] == 'rplayfair':
                default_context['radditive_result'] = additive_cipher(
                    default_context['radditive_data'],
                    1,
                    reverse=True)
            elif default_context['last_action'] == 'foursquare':
                default_context['foursquare_result'] = multiply_cipher(
                    default_context['foursquare_data'],
                    int(default_context['foursquare_key']),
                    reverse=False)
            elif default_context['last_action'] == 'rfoursquare':
                default_context['rfoursquare_result'] = multiply_cipher(
                    default_context['rfoursquare_data'],
                    1,
                    reverse=True)
        except Exception, err:
            print(err)

    return render_template("labs/lab2.html", **context)


app.run(port=8002, debug=True, host='0.0.0.0', threaded=True)
