# -*- coding: utf-8 -*-
"""This module contains all helper functions used in module"""


def input(prompt, default_value, validator):
    prompt = "%s\n[%s]> " % (prompt, default_value, )
    while 1:
        value = raw_input(prompt)
        if value == '':return default_value
        try:
            return validator(value)
        except ValueError, err:
            print err


def positive_int_validator(n):
        try:
            n = int(n)
            if n < 1:raise ValueError("Number must be greater than 0")
            return n
        except:
            raise ValueError("Error parsing number. Check input please!")


def boolean_validator(n):
    n = n.lower()
    if n in ['true', 'y', 'yes', 'tak', 'sure', 't']:
        return True
    if n in ['false', 'n', 'no', 'ni', 'not sure', 'f']:
        return False
    raise ValueError("Wrong value!")


def not_empty_validator(n):
    return n.upper()


def range_validator(min, max):
    def _range_validator(value):
        try:
            value = int(value)
            if value >= min and value < max:
                return value
            else:
                raise ValueError("Value is not acceptable")
        except ValueError, err:
            raise ValueError(err)
        except:
            raise ValueError("Error to parse value")
    return _range_validator


def in_list_validator(values_list):
    def _in_list_validator(value):
        if value in values_list:
            return value
        else:
            raise ValueError("Wrong value!")
    return _in_list_validator
