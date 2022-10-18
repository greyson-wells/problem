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
  if not output == open("1.txt").read():
    raise check50.Failure("did not correctly build pyramid of height 1")
  

@check50.check(exists)
def test2():
  """input of 2 yields correct output"""
  output = check50.run("python3 mario.py").stdin("2").stdout()
  if not output == open("2.txt").read():
    raise check50.Failure("did not correctly build pyramid of height 2")
    
@check50.check(exists)
def test5():
  """input of 5 yields correct output"""
  output = check50.run("python3 mario.py").stdin("5").stdout()
  if not output == open("5.txt").read():
    raise check50.Failure("did not correctly build pyramid of height 5")
    
@check50.check(exists)
def test8():
  """input of 8 yields correct output"""
  output = check50.run("python3 mario.py").stdin("8").stdout()
  if not output == open("8.txt").read():
    raise check50.Failure("did not correctly build pyramid of height 8")
    
@check50.check(exists)
def test0():
  """rejects a height of 0"""
  output = check50.run("python3 mario.py").stdin("0").stdout()
  if not output == "":
    raise check50.Failure("program did not reject invalid input")
    
@check50.check(exists)
def test9():
  """rejects a height of 9"""
  output = check50.run("python3 mario.py").stdin("9").stdout()
  if not output == "":
    raise check50.Failure("program did not reject invalid input")
  
@check50.check(exists)
def test_negative_two():
  """rejects a height of -2"""
  output = check50.run("python3 mario.py").stdin("-2").stdout()
  if not output == "":
    raise check50.Failure("program did not reject invalid input")

@check50.check(exists)
def test_foo():
  """rejects a non-numeric height of "foo" """
  output = check50.run("python3 mario.py").stdin("foo").stdout()
  if not output == "":
    raise check50.Failure("program did not reject invalid input")
    
@check50.check(exists)
def test_empty():
  """rejects a non-numeric height of "" """
  output = check50.run("python3 mario.py").stdin("").stdout()
  if not output == "":
    raise check50.Failure("program did not reject invalid input")
