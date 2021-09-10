#!/usr/bin/env python
# -*- coding: utf-8 -*-
# run command
# > python diceroll.py

import random

def main():
  print("1D20000 result : {}".format(random.randrange(1, 20000,)))

if __name__ == '__main__':
     main()
