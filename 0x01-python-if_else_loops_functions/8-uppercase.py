#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        print("{}".format(chr(ord(letter) - 32)
                          if (ord(letter) >= ord("a") and
                              ord(letter) <= ord("z")) else letter), end="")
    print()
