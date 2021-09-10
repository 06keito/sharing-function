#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Abstract
# Make each line consisting of multiple sentences a new line.
# and further translation can be done.

# > pip install googletrans==4.0.0-rc1 deepl
# > python Multiple_sentence_reconstruction.py --mode [google_trance,deepl]

import sys,re
import argparse
import regex
import googletrans,deepl  
#DeepL api Document -> #https://www.deepl.com/ja/blog/announcing-python-client-library-for-deepl-api

CONSOLE_ARGUMENTS = None

def get_args():
     parser = argparse.ArgumentParser()
     parser.add_argument('-m', '--mode',\
          dest='mode', type=str, default='google_translate', help="choose mode")
     return parser.parse_args()



def input_text_data():
     S,data = str(),list()
     with open('input.txt',mode='r',encoding='utf-8') as fr:
          array = list(regex.split(r'(?<=[.])(?!$)',\
               fr.read().replace('\n',' ')))
          # Separate each sentence.
     line_count = len(array) # Get the number of lines
     if array[-1]!=' ': # add dummy line
          array += [' ']
          line_count += 1

     for i in range(line_count-1):
          S += array[i].lstrip().rstrip()
          if re.search(r'[.,[]', array[i+1][0]) or \
               str.isnumeric(array[i+1][0]) or (array[i+1][0].islower()):
               continue
          else:
               data.append(S)
               S = ''
     return data



def print_error_log(error_frame_point,error_msg):
     print('{frame} : {msg}'\
          .format(frame=error_frame_point,msg=error_msg))



def output_justification_text_data(data):
     with open('output_paragraph_formating.txt',mode='w',encoding='utf-8') as fw:
          for line in data:
               try:
                    fw.write('{l_br}'.format(l_br=line+'\n'))
               except Exception as error_msg:
                    print_error_log(sys._getframe().f_code.co_name,error_msg)
                    continue



def trancerate_with_the_selected_translators():
     mode = CONSOLE_ARGUMENTS.mode
     if mode=='deepl':
          with open('deepl_auth_key.txt',mode='r',encoding='utf-8') as f:
               auth_key = f.read() # get user auth key from deepl_auth_key.txt
          try:
               translator = deepl.Translator(auth_key)
          except Exception as error_msg:
               print_error_log(sys._getframe().f_code.co_name,error_msg)
               translator = googletrans.Translator()
     else:
          translator = googletrans.Translator()

     translator_class_name = str(translator.__class__)[8:-2]
     # get sliced class name  (example) 
     # <class 'googletrans.client.Translator'> 
     #     ->  googletrans.client.Translator

     print('> Using {}'.format(translator.__class__)) # show witch translator
     return translator,translator_class_name



def output_trancerated_text_data(data):
     translator,translator_name = trancerate_with_the_selected_translators()
     write_to_ft = lambda file,tranced : file.write('{}'.format(tranced+'\n'))
     write_to_fba = lambda file,tranced,lne : file.write('{}{}'.format(lne+'\n',tranced+'\n'))
     try:
          with open('output_trancerated.txt',mode='w',encoding='utf-8') as ft,\
          open('output_trancerated_before_and_after.txt',mode='w',encoding='utf-8') as fba:
               if translator_name == 'googletrans.client.Translator':
                    for line in data:
                         trancerated_text = translator.translate(line,src='en', dest='ja').text
                         write_to_ft(ft,trancerated_text)
                         write_to_fba(fba,trancerated_text,line)
               elif translator_name == 'deepl.translator.Translator':
                    for line in data:
                         # If you have selected the deepl Free Plan, there may be a character limit.
                         trancerated_text = translator.translate_text(line, target_lang='JA').text
                         write_to_ft(ft,trancerated_text)
                         write_to_fba(fba,trancerated_text,line)

     except Exception as error_msg:
          print_error_log(sys._getframe().f_code.co_name,error_msg)



def main():
     global CONSOLE_ARGUMENTS
     CONSOLE_ARGUMENTS = get_args()
     text_data = input_text_data() #get text data from input.txt
     output_justification_text_data(text_data) #output text data by output_trancerated.txt,output_trancerated_before_and_after.txt
     output_trancerated_text_data(text_data) #output text data by output_paragraph_formating.txt

if __name__ == '__main__':
     main()