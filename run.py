# -*- coding: utf-8 -*-
"""
This module is all programs entrance.
It have menu.
"""
from helpers import input, range_validator
from ciphers import main as ciphers_main


MENU_OPTIONS = (("Lab #1. Ciphers.", ciphers_main),)


if __name__ == "__main__":

    menu_text = "Hello!Please, choose lab #:\n"
    menu_additional_text = u"\n".join(["[{}]".format(n) + option_text for n, (option_text, _) in enumerate(MENU_OPTIONS)])
    print repr(menu_text)
    answer = input(menu_additional_text, 0, range_validator(0, len(MENU_OPTIONS)))
    MENU_OPTIONS[answer][1]()


