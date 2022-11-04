import check50
import re 

@check50.check()
def exists():
  """connect.py exists"""
  check50.exists("connect.py")

@check50.check(exists)
def test_player1_condition1():
  """player 1 wins with a horizontal line"""
  check50.run("python connect.py").stdin("p1").stdin("p2").stdin("1").stdin("7").stdin("2").stdin("6").stdin("3").stdin("5").stdin("4").stdout("P1 WINS")
  
@check50.check(exists)
def test_player1_condition2():
  """player 1 wins with a bottom left to top right diagonal line"""
  check50.run("python connect.py").stdin("p1").stdin("p2").stdin("1").stdin("2").stdin("2").stdin("3").stdin("3").stdin("4").stdin("3").stdin("4").stdin("4").stdin("7").stdin("4").stdout("P1 WINS")
  
@check50.check(exists)
def test_player1_condition3():
  """player 1 wins with a vertical line"""
  check50.run("python connect.py").stdin("p1").stdin("p2").stdin("1").stdin("2").stdin("1").stdin("2").stdin("1").stdin("2").stdin("1").stdout("P1 WINS")
  
@check50.check(exists)
def test_player1_condition4():
  """player 1 wins with a top left to bottom right diagonal line"""
  check50.run("python connect.py").stdin("p1").stdin("p2").stdin("1").stdin("1").stdin("4").stdin("1").stdin("1").stdin("3").stdin("3").stdin("2").stdin("6").stdin("2").stdin("2").stdout("P1 WINS")
