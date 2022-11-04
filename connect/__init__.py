import check50
import re 

@check50.check()
def exists():
  """connect.py exists"""
  check50.exists("connect.py")
  check50.include("p1win1.txt", "p1win2.txt", "p1win3.txt", "p1win4.txt", "p2win1.txt", "p2win2.txt", "p2win3.txt", "p2win4.txt")

@check50.check()
def test(exists):
  """testing"""
  
@check50.check(exists)
def test_player1_condition1():
  """player 1 wins with a horizontal line"""
  input = open("p1win1.txt").read()
  check50.run("python connect.py").stdin(input).stdout("P1 WINS")
