#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Abstract
# Input assistance for snippets
# Enclose the input line with [""] and add a comma to the end

# run command
# -> python user_snippet_simplification.py

def main():
    with open('input.txt',mode='r',encoding='utf_8') as f_in,\
    open('output.txt',mode='w',encoding='utf_8') as f_out:
        for line in f_in.readlines():
            f_out.write('{}'.format('"'+line.rstrip('\n')+'",\n'))
    
if __name__ == '__main__':
    main()