import re

from check50 import *

class Mario(Checks):
  
  @check()
  def exists(self):
    """mario compiles"""
    self.require("mario.py")
