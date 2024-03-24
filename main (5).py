import valid as v
#******************************************************************************
# Author:           Kimberly Rodriguez
# Assignment:       Assignment 4
# Date:             2/10/2024
# Description:      This program calculates the number of times a user can
#                   sing a song
# Revisions:        A01 - initial assignment
#                   A02 - refactored the code to use functions for inputs,
#                         calculations and outputs
#                   A03 - Added a loop and a menu to allow the user to       
#                   continue adding songs. A cummulative total of minutes
#                   is kept and printed when the user ends the program.
#                   Added an if statement to print the remaining time the    
#                   user has left and the total number of minutes the user   
#                   will sing during the shower
#                   A04 - Added input validation. The program works as before
#                   but input validation was added to the get_ functions
#                   to ensure valid input was returned.
#******************************************************************************
SEC_PER_MIN = 60
ADD_SONG = 1
QUIT = 2


def main():
  song = ''
  length_in_min = 0
  length_in_sec = 0
  shower_time = 0
  total_length = 0.0
  choice = 0

  total_time_used = 0
  
  print_welcome()

  shower_time = get_shower_time() # Get shower time once outside the loop
  
  while (choice != QUIT) and (total_time_used < shower_time):
    print_menu()
    choice = get_choice()

    if choice == ADD_SONG:
    #Gets input from user
      song = get_song()
      length_in_min = get_length_in_min(shower_time)
      length_in_sec = get_length_in_sec()
      times_to_sing = get_times_to_sing(song)
      
    #Convert the song length in minutes to seconds 
    #So you can add song length in min
      min_to_sec = calc_min_to_sec(length_in_min)
  
      total_length = calc_total_length_in_sec(min_to_sec, length_in_sec)
  
    #Convert the total length back to minutes so that 
    #You can calculate the total times
      total_length = calc_total_length_in_min(total_length) 

      time_needed = total_length * times_to_sing
      
      total_time_used = total_time (total_time_used, time_needed,
                                    shower_time, times_to_sing, song) 

  print_end(total_time_used)
  

def print_welcome():
  """
  Prints information about the program to the user
  :param: none
  :return: none
  """
  print("Welcome to the singing in the shower calculator program!\n")
  print("This program will help plan out your singing time.\n")
  print("\nLet's get ready to sing!\n")
  

def print_menu():
  """
  Prints the menu of options
  :param: none
  :return: none
  """
  print("\n1. Add a song")  
  print("2. Quit")  


def get_choice():
  """
  Prompts the user for a menu choice and returns it
  :param: none
  :return: menu choice as an integer
  """
  choice = 0
  choice = v.get_integer("\nEnter menu choice: ")
  while choice < ADD_SONG or choice > QUIT:
    print("Invalid menu choice!")
    choice = v.get_integer("\nEnter menu choice: ")
  return choice


def get_song():
  """
  Prompt the user for the song and returns it
  :param: none
  :return: song as a string
  """
  song = ''
  song = input("\nPlease enter the name of the song: ")
  while song == '':
    print('Song cannot be blank')
    song = input("\nPlease enter the name of the song: ")
  return song


def get_length_in_min(shower_time):
  """
  Prompt the user for the length of the song in minutes
  :param: none
  :return: length in minutes as an integer
  """
  length_in_min = 0
  length_in_min = v.get_integer("Please enter the"
                                + " song's length in minutes: ")
  while length_in_min < 0 or length_in_min > shower_time:
    print(f"song length in minutes must be 0 - {shower_time}")
    length_in_min = v.get_integer("Please enter the"
      + " song's length in minutes: ")
  return length_in_min


def get_length_in_sec():
  """
  Prompt the user for the length of the song in seconds
  :param: none
  :return: length in seconds as a integer
  """
  length_in_sec = 0
  length_in_sec = v.get_integer("Please enter the song's length in seconds: ")

  while length_in_sec < 0 or length_in_sec > 59:
    print("Song length in seconds must be 0 - 59")
    length_in_sec = v.get_integer("Please"
                                  + " enter the song's length in seconds: ")
  return length_in_sec


def get_shower_time():
  """
  Prompt the user for the shower time
  :param: none
  :return: shower time as a integer
  """
  shower_time = 0
  shower_time = v.get_integer("Please enter your shower time in minutes: ")

  while shower_time < 0:
    print("Shower time must be 0 or greater")
    shower_time = v.get_integer("Please enter your shower time in minutes: ")
  return shower_time


def get_times_to_sing(song):
  times_to_sing = ''
  times_to_sing = v.get_integer('\nHow many times'
                            + f' do you want to sing {song}?: ')
  while times_to_sing < 0:
    print("Please enter a positive number")
    times_to_sing = v.get_integer('\nHow many times'
      + f' do you want to sing {song}?: ')
  return times_to_sing


def calc_min_to_sec(length_in_min):
  """
  Calculate and return minutes to seconds
  :param length_in_min: integer with length in minutes
  :return: minutes to seconds as an integer
  """
  min_to_sec = 0
  min_to_sec = length_in_min * SEC_PER_MIN
  return min_to_sec


def calc_total_length_in_sec(min_to_sec, length_in_sec):
  """
  Calculate and return total length in seconds
  :param min_to_sec: integer with minutes to seconds
  :param length_in_sec: integer with the length in seconds
  :return: total length as an integer
  """
  total_length_in_sec = 0
  total_length_in_sec = min_to_sec + length_in_sec
  return total_length_in_sec


def calc_total_length_in_min(total_length):
  """
  Calculate and return the total length in minutes
  :param total_length: integer with total length
  :return: total length as a float
  """
  total_length_in_min = 0 
  total_length_in_min = total_length / SEC_PER_MIN
  return total_length_in_min


def calc_total_times(shower_time, total_length):
  """
  Calculate and return total times
  :param shower_time: integer with shower time
  :param total_length: float with total length
  :return: total length as a float
  """
  total_times = 0
  total_times = shower_time / total_length
  return total_times

def total_time(total_time_used, time_needed,
               shower_time, times_to_sing, song):
  """
  Calculate and return total time
  :param total_time_used: integer with total time used
  :param time_needed: float with time needed
  :param shower_time: integer with shower time
  :param times_to_sing: integer with times to sing
  :param song: string with song
  :return: total time as a float
  """
  remaining_time = 0

  #If statement to get total time used and remaining time
  if total_time_used + time_needed <= shower_time:
      total_time_used += time_needed
      remaining_time = shower_time - total_time_used
      print(f'\nYou have {remaining_time:.0f} minutes' 
          + f' left if you sing {song} {times_to_sing:.0f} times')
  else:
      print("Sorry, not enough time left in the shower!")
  return total_time_used


def print_end(total_time_used):
  """
  Prints closing information to the user
  :param: none
  :return: none
  """
  # Calculating total seconds
  total_seconds = (total_time_used % 1) * SEC_PER_MIN
  
  print('\nYou will be singing for a'
        + f' total of {total_time_used:.0f} minutes and {total_seconds:.0f}'
        + ' seconds during your shower.')


# Call main() to start the program 
main()