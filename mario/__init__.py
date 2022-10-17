import check50
import re

@check50.check()
def exists():
  """mario.py exists"""
  check50.exists("mario.py")
  check50.include("1.txt", "2.txt", "5.txt", "8.txt")
  
@check50.check(exists)
def test1():
  """input of 1 yields correct output"""
  output = check50.run("python3 mario.py").stdin("1", prompt=False).stdout(r'\$?#', '#\n').exit()

@check50.check(exists)
def test_negative_two():
  """rejects a height of -2"""
  check50.run("python3 mario.py").stdin("-1").stdout(regex(output), regex=False)

def regex(num):
  """testing"""
  return fr'^.*{escape(num)}.*$'
