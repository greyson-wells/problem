import check50
import re

@check50.check()
def exists():
  """mario.py exists"""
  check50.exists("mario.py")
  
@check50.checks(exists)
def test1():
  """input of 1 yields correct output"""
  output = check50.run("python3 mario.py").stdin("1", prompt=False).stdout(r'\$?#', '#').exit()
