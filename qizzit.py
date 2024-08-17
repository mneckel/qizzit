#!/bin/python
# qizzit.py  v1.4      This is Public Domain
# Very simple quiz generator
# August 10, 2024

import os
import sys
numcorr = 0
tlquestions = 0
questionno = 1
i = 0

def open_and_read_file(file_path):
  """Opens and reads a file, returning its contents as a string.
  Args:
    file_path: The path to the file to be opened.
  Returns:
    The contents of the file as a string.
  """
  try:
    with open(file_path, 'r') as file:
      lines = file.readlines()
      #print(lines[0][0])
  except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
  displayquestions(lines)

def displayquestions(lines):
  global i, questionno
  pans = 1
  while lines:
    if lines[i][0] == "!":         # print question
      print(str(questionno)+".  ", end="")   
      print(lines[i][1:].strip())
      questionno += 1
    if lines[i][0] == "=":         # set the correct answer 
      cansr = (lines[i][1:].strip()).upper()
    if lines[i][0] == "*":         # print the choices
      # clever way to print a. b. c. d.
      print(f"  {chr(pans+96)}.", lines[i][1:].strip())
      pans += 1
    if lines[i][0] == "$":         # end of this question set
      userin(cansr)
      pans = 1
    if lines[i][0] == "#":         # end of quiz
      break    
    i += 1

def userin(cansr):
  global numcorr
  user_input = input("Response: ")
  character = user_input[0].upper()  # Extract the first character
  if character == cansr:
    print("Correct!")
    numcorr += 1
  else:
    print("Incorrect, the correct answer is:", cansr)  
  print()

def get_tl_questions(file_path): # for info and final grade
  global tlquestions
  with open(file_path, 'r') as file:
    for line in file:
      if line[0] == "=":
        tlquestions += 1
  print("Using file:", file_path)
  print("Number of questions in this quiz:", tlquestions)
  print()
  return tlquestions

os.system('cls' if os.name == 'nt' else 'clear') # clear the screen
if len(sys.argv) < 2:   # only error check in this entire app
  print("Usage: python script_name.py filename")
  sys.exit(1)
file_path = sys.argv[1]
get_tl_questions(file_path)
open_and_read_file(file_path)

# generate final score
try:
  print("Total score:", round(numcorr/tlquestions*100,), "%")
except ZeroDivisionError:
  print("Zero correct")
    
