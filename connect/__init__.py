import check50
import re 

@check50.check()
def exists():
  """mario.py exists"""
  check50.exists("mario.py")
  check50.include("p1win1.txt", "p1win2.txt", "p1win3.txt", "p1win4.txt", "p2win1.txt", "p2win2.txt", "p2win3.txt", "p2win4.txt")
  
@check50.check(exists)
def test_player1_condition1():
  """player 1 wins with a horizontal line"""
  input = open("p1win1.txt").read
  check50.run("python connect.py").stdin("0")
