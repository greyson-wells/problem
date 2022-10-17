import check50
import re
from re import escape

@check50.check()
def exists():
  """mario.py exists"""
  check50.exists("mario.py")
  check50.include("1.txt", "2.txt", "5.txt", "8.txt")
  
@check50.check(exists)
def test1():
  """input of 1 yields correct output"""
  output = check50.run("python3 mario.py").stdin("1").stdout()
  checkPyramid(output, open("1.txt").read())
  

@check50.check(exists)
def test2():
  """input of 2 yields correct output"""
  output
  
@check50.check(exists)
def test_negative_two():
  """rejects a height of -2"""
  output = check50.run("python3 mario.py").stdin("-1").stdout()
  if not output == "":
    raise check50.Failure("program did not reject invalid input")

def checkPyramid(output, correct):
  if output == correct:
    return
