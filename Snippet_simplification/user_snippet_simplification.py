#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Abstract
# Input assistance for snippets
# Enclose the input line with [""] and add a comma to the end

# run command
# -> python user_snippet_simplification.py

def main():
    line_count = sum(1 for line in open('input.txt'))
    with open('input.txt',mode='r',encoding='utf_8') as f_in,\
    open('output.txt',mode='w',encoding='utf_8') as f_out:
        for idx,line in enumerate(f_in.readlines(),1):
            if idx!=line_count:
                text = ('{}'.format('"'+line.rstrip('\n')+'",\n'))
            else: #last line
                text = ('{}'.format('"'+line.rstrip('\n')+'"'))
            f_out.write(text)

if __name__ == '__main__':
    main()