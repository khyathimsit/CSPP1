'''
Author: Khyathi C

Date: 1-Aug-18

Encoding: UTF-8


'''
VARA = 5
VARB = 10
if isinstance(VARA, str) or isinstance(VARB, str):
    print("string involved")
if VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")
