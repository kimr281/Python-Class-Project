"""
The input validation module contains functions to read in and validate
for an integer or float data type.
"""

def get_integer(prompt="Please enter an integer: "):
  """
  Prompts for an integer and returns a valid integer
  :param prompt: Optional string to use as prompt
  :return: a valid integer
  """
  num = 0
  valid = False

  while not valid:
      try:
          num = int(input(prompt))
          valid = True
      except:
          print("Invalid integer.")

  return num


def get_float(prompt="Please enter a float: "):
  """
  Prompts for a float and returns a valid float
  :param prompt: Optional string to use as prompt
  :return: a valid float
  """
  num = 0
  valid = False

  while not valid:
      try:
          num = float(input(prompt))
          valid = True
      except:
          print("Invalid float.")

  return num
