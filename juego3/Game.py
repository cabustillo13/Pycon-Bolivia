#!/usr/bin/python
# -*- coding: utf8 -*-

# guadaquiz2
# Un simple juego de preguntas pensado para pantalla tactil
# Author: Alfonso E.M.
# License: Free (GPL) 
# Version: 2.0 - /Apr/2007
# Modificado por Carlos Bustillo

import pygame
import os,sys
import getopt
import random
import Tools 
import Gui
from unidecode import unidecode

# MAIN INITIALIZATION
def main():

  questionfile=""
  appdir=os.path.dirname(sys.argv[0])
  questionfiles=os.listdir(appdir+"Preguntas")
  print ("Using: "+appdir+"Preguntas\n")

  ok=0
  wrong=0

  gui=Gui.Gui(appdir)
  gui.show_intro()

  while 1:
   questionfile=""
   while questionfile[0:1] != "q":
     questionfile=random.choice(questionfiles)
   try:
       qfile=open(appdir+"Preguntas/"+questionfile)
   except:
      sys.exit("ERROR: can't open question file "+questionfile)
   
   question =qfile.readline().replace("\n","")
   question =question.replace("\r","")
   question.encode('utf-8')
   
   answer1=qfile.readline().replace("\n","")
   answer1=answer1.replace("\r","")
   answer1.encode('utf-8')
   
   answer2=qfile.readline().replace("\n","")
   answer2=answer2.replace("\r","")
   answer2.encode('utf-8')
   
   answer3=qfile.readline().replace("\n","")
   answer3=answer3.replace("\r","")
   answer3.encode('utf-8')
   
   right_answer=qfile.readline().replace("\n","")
   right_answer=right_answer.replace("\r","")
   qfile.close

   gui.show_question(question,answer1,answer2,answer3)
   answer=gui.wait_for_answers()
   if answer == right_answer:
      ok=ok+1
   else:
      wrong=wrong+1

   if answer == "A":
      show = answer1
   elif answer == "B":
      show = answer2
   elif answer == "C":
      show = answer3
   gui.show_result(show,answer,right_answer)
   
   print ("OK:",ok," ERRORS:",wrong,"\n")
 

if __name__ == '__main__': main()
