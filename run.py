# -*- coding: utf-8 -*-
"""
This module is all programs entrance.
It have menu.
"""
import tempfile
import uuid

from flask import Flask, request, render_template, send_file

from ciphers import (additive_cipher, multiply_cipher,
                     affine_cipher, Playfair,
                     Foursquare, Vigenere, Swaper,
                     ElGamal, check_sign, generate_key)


PATH_ROOT = "/"
PATH_LAB = "/lab/"
PATH_LAB_1 = PATH_LAB + "1"
PATH_LAB_2 = PATH_LAB + "2"
PATH_LAB_3 = PATH_LAB + "3"
PATH_LAB_4 = PATH_LAB + "4"
PATH_LAB_6 = PATH_LAB + "6"

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

PARAMS_2 = (
    ("playfair_key", ""),
    ("playfair_data", "TEST STRING"),
    ("playfair_result", None),

    ("rplayfair_key", ""),
    ("rplayfair_data", "TEST STRING"),
    ("rplayfair_result", None),

    ("foursquare_key1", ""),
    ("foursquare_key2", ""),
    ("foursquare_data", "TEST STRING"),
    ("foursquare_result", None),

    ("rfoursquare_data", "TEST STRING"),
    ("rfoursquare_key1", ""),
    ("rfoursquare_key2", ""),
    ("rfoursquare_result", None),
)

PARAMS_3 = (
    ("vigenere_key", ""),
    ("vigenere_alph", ""),
    ("vigenere_data", "ЗАХИСТ_ІНФОРМАЦІЇ"),
    ("vigenere_result", None),

    ("rvigenere_key", ""),
    ("rvigenere_alph", ""),
    ("rvigenere_data", "ФОЧИВЕБІЯЖРРЮОШІЧ"),
    ("rvigenere_result", None),

)

PARAMS_4 = (
    ("swaper_key", "3, 1, 4, 5, 2"),
    ("swaper_data", "ENEMYATTACKSTONIGHT"),
    ("swaper_result", None),

    ("rswaper_key", "3, 1, 4, 5, 2"),
    ("rswaper_data", "ETTHEAKIMAOTYCNXNTSG"),
    ("rswaper_result", None),
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
        except Exception as err:
            print("exception: ", err)
    return render_template('labs/lab1.html', **default_context)


@app.route(PATH_LAB_2, methods=['GET', 'POST'])
def lab2_page():
    
    default_context = {}
    default_context['last_action'] = request.form.get("action", "playfair")
    for param in PARAMS_2:
        default_context[param[0]] = request.form.get(param[0], param[1])

    if request.method == 'POST':
        try:
            if default_context['last_action'] == 'playfair':
                p = Playfair(default_context['playfair_key'])
                default_context['playfair_result'] = p.encipher(default_context['playfair_data'])
            elif default_context['last_action'] == 'rplayfair':
                p = Playfair(default_context['rplayfair_key'])
                default_context['rplayfair_result'] = p.decipher(default_context['rplayfair_data'])
            elif default_context['last_action'] == 'foursquare':
                f = Foursquare(default_context['foursquare_key1'], default_context['foursquare_key2'])
                default_context['foursquare_result'] = f.encipher(default_context['foursquare_data'])
            elif default_context['last_action'] == 'rfoursquare':
                f = Foursquare(default_context['rfoursquare_key1'], default_context['rfoursquare_key2'])
                default_context['rfoursquare_result'] = f.decipher(default_context['rfoursquare_data'])
        except Exception as err:
            print("exception: ", err)

    return render_template("labs/lab2.html", **default_context)


@app.route(PATH_LAB_3, methods=['GET', 'POST'])
def lab3_page():
    
    default_context = {}
    default_context['last_action'] = request.form.get("action", "vigenere")
    for param in PARAMS_3:
        default_context[param[0]] = request.form.get(param[0], param[1])

    if request.method == 'POST':
        try:
            if default_context['last_action'] == 'vigenere':
                v = Vigenere(default_context['vigenere_alph'], default_context['vigenere_key'])
                default_context['vigenere_result'] = v.encipher(default_context['vigenere_data'])
                default_context['last_pattern'] = v.last_pattern
                default_context['alph'] = v.alph
                default_context['sep'] = "*" * len(v.last_pattern)
            elif default_context['last_action'] == 'rvigenere':
                v = Vigenere(default_context['rvigenere_alph'], default_context['rvigenere_key'])
                default_context['rvigenere_result'] = v.decipher(default_context['rvigenere_data'])
                default_context['last_pattern'] = v.last_pattern
                default_context['alph'] = v.alph
                default_context['sep'] = "*" * len(v.last_pattern)
        except Exception as err:
            print("exception: ", err)

    return render_template("labs/lab3.html", **default_context)


@app.route(PATH_LAB_4, methods=['GET', 'POST'])
def lab4_page():
    
    default_context = {}
    default_context['last_action'] = request.form.get("action", "swaper")
    for param in PARAMS_4:
        default_context[param[0]] = request.form.get(param[0], param[1])

    if request.method == 'POST':
        try:
            if default_context['last_action'] == 'swaper':
                v = Swaper(default_context['swaper_key'])
                default_context['swaper_result'] = v.encode_data(default_context['swaper_data'])
            elif default_context['last_action'] == 'rswaper':
                v = Swaper(default_context['rswaper_key'])
                default_context['rswaper_result'] = v.decode_data(default_context['rswaper_data'])
        except Exception as err:
            print("exception: ", err)

    return render_template("labs/lab4.html", **default_context)


EL_DOCUMENT = "el-gamal-document"
EL_SIGN = "el-gamal-sign"
EL_ACTION = "action"
EL_ERROR = "error"
EL_SUCCESS = "success"

EL_ACTION_TYPE_SIGN = 'sign'
EL_ACTION_TYPE_CHECK = 'check'
EL_ACTION_TYPE_GEN = 'generate'

@app.route(PATH_LAB_6, methods=['GET', 'POST'])
def lab6_page():

    context = {}
    if request.method == 'POST':
        try:
            
            action = request.form.get(EL_ACTION, EL_ACTION_TYPE_SIGN)
            document = request.files.get(EL_DOCUMENT, None)
            key = request.files.get(EL_SIGN, None)
            
            if action == EL_ACTION_TYPE_GEN:
                p = str(uuid.uuid4()) + '.txt'
                f = open(p, 'w')
                print(f, p)
                f.write("%s\n%s\n%s\n%s" % (*generate_key(), ))
                f.close()
                return send_file(p, as_attachment=True)
            
            print(action)
            if not document or not key:
                context[EL_ERROR] = "Відсутні потрібні файли!"
            else:
                if action == EL_ACTION_TYPE_SIGN:
                    
                    p, g, x, y = (int(line) for line in key.readlines())
                    print(p, g, x, y)
                    (a, b) = ElGamal(p, g, x, y).sign(document.read())
                    path = str(uuid.uuid4()) + '.txt'
                    f = open(path, 'w')
                    f.write("%s\n%s\n%s\n%s\n%s" % (a, b, p, g, y, ))
                    f.close()
                    return send_file(path, as_attachment=True)
                else:
                    a, b, p, g, y = (int(line) for line in key.readlines())
                    if check_sign(document.read(), a, b, p, g, y):
                        context[EL_SUCCESS] = True
                    else:
                        context[EL_ERROR] = "Не правильний підпис!"


        except Exception as err:
            print("Exception: %s" % (err, ))
    return render_template("labs/lab6.html", **context)

app.run(port=8002, debug=True, host='0.0.0.0', threaded=True)
