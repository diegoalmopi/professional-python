from platform import system
from os import system as console_command
from time import sleep
from datetime import date
from typing import Any, Callable, Generator, List
from numpy import arange as np_range


# Validations

def validate_strings(x: int, y: int, header: str, error_message: str) -> str:
  """Validate strings."""

  while True:
    gotoxy(x, y); print(header, end='')
    gotoxy(x+len(header), y); string_not_formatted: str = input('').rstrip().title()
    if string_not_formatted.replace(' ', '').isalpha() and string_not_formatted != '':
      if string_not_formatted[0] != ' ':
        blank_space: List = [pos for pos, char in enumerate(string_not_formatted) if char == ' ']
        into_bucle: bool = False
        for idx in blank_space:
          try:
            iterator: int = idx + 1
            if string_not_formatted[idx] == string_not_formatted[iterator]:  # ' ' == ' ' -> ERROR!
              into_bucle = True
              break
          except IndexError: pass
        if not into_bucle:
          string: str = ''
          for letter in string_not_formatted.split(): string += letter + ' '
          return string.strip()
      else: pass
    else: pass
    gotoxy(x+len(header)+len(string_not_formatted), y); print(error_message)
    sleep_screen(x+len(header)+len(string_not_formatted), y, error_message, string_not_formatted)

def validate_floats(x: int, y: int, header: str, error_message: str, type: str) -> float:
  """Validate floats."""

  while True:
    gotoxy(x, y); print(header, end='')
    try:
      gotoxy(x+len(header), y); numbers: str = input('').rstrip()
      if numbers[0] != ' ':
        if type == 'w':
          number_weight = [round(x, 2) for x in np_range(20, 635.01, 0.01)]
          if binary_search(number_weight, float(numbers)):
            return float(numbers)
        else:
          number_height = [round(i, 2) for i in np_range(0.72, 2.73, 0.01)]
          if binary_search(number_height, float(numbers)):
            return float(numbers)
      else: pass
    except ValueError: pass
    gotoxy(x+len(header)+len(numbers), y); print(error_message)
    sleep_screen(x+len(header)+len(numbers), y, error_message, numbers)

def validate_dates(x: int, y: int, header: str, error_message: str) -> date:
  """Validate dates."""
  
  while True:
    gotoxy(x, y); print(header, end='')
    try:
      gotoxy(x+len(header), y)
      string: str = input('').rstrip().replace(' ', '!').replace('\t', '!!!!!!!!')
      list_string: List = string.split('/')
      if list_string[0][0] != '0' and list_string[1][0] != '0' and list_string[2][0] != '0':
        if len(list_string) == 3:
          return date(int(list_string[0]), int(list_string[1]), int(list_string[2]))
        else: pass
      else: pass
    except (SyntaxError, ValueError, NameError, TypeError, IndexError): pass
    gotoxy(x+len(header)+len(string), y); print(error_message)
    sleep_screen(x+len(header)+len(string), y, error_message, string)

def calculate_age(birth_date: date) -> int:
  """Calculate age."""

  today: date = date.today()
  age: int = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
  return age

def validate_blood(x: int, y: int, header: str, error_message: str) -> str:
  """Validate type of blood."""
  
  while True:
    gotoxy(x, y); print(header, end='')
    gotoxy(x+len(header), y); string: str = input('').rstrip().upper()
    if string[0] != ' ':
      if len(string) in range(2, 4):
        if len(string) == 2:
          if string in ('O+', 'O-', 'A+', 'A-', 'B+', 'B-'): return string
          else: pass
        else:
          if string in ('AB+', 'AB-'): return string
          else: pass
    else: pass
    gotoxy(x+len(header)+len(string), y); print(error_message)
    sleep_screen(x+len(header)+len(string), y, error_message, string)
  
def validate_gender(x: int, y: int, header: str, error_message: str) -> str:
  """Validate a person's gender."""

  while True:
    string: str = validate_strings(x, y, header, error_message)
    if string[0] != ' ':
      if len(string) == 1:
        if string in ('M', 'F'): return string
        else: pass
    else: pass
    gotoxy(x+len(header)+len(string), y); print(error_message)
    sleep_screen(x+len(header)+len(string), y, error_message, string)


# Fuctions for the program.

def welcome_traveler() -> None:
  """Welcome the traveler and explain the program."""

  clean_screen()
  gotoxy(4, 4); print("INTERSTELLAR TRAVEL    ⊂(◉‿◉)つ")
  gotoxy(6, 6); print("* Hello traveler, welcome to the adventure of your life!")
  gotoxy(7, 8); print("+ Then, sign out to see if you can do interestellar")
  gotoxy(9, 9); print("travel without any problems.")
  gotoxy(6, 11); print("→ Press a key to continue..."); input('')

def greeting_traveler(func) -> Callable[[Any], Any]:
  """Greet the traveler."""

  def wrapper(*args: Any) -> Any:
    clean_screen()
    gotoxy(4, 4); print("INTERSTELLAR TRAVEL    ⊂(◉‿◉)つ")
    gotoxy(6, 6); print("→ Hello traveler, we are preparing")
    gotoxy(9, 7); print("you for the trip!")
    return func(*args)
  return wrapper

def processing(x: int, y: int, sms: str) -> None:
  """It's responsible for simulating a system processing."""

  for _ in range(1, 16):  # 5 seconds for processing.
    try:
      gotoxy(x, y); print(sms+next(generator))
      sleep(0.333333334)
      gotoxy(x, y); print('     '*len(sms))
    except (NameError, StopIteration):
      generator: Generator = (i for i in ('.  )', '.. )', '...)'))

@greeting_traveler
def choice_of_traveler(*args: Any) -> bool:
  """Initialize the traveler's choice."""

  args = args[0]
  age: int; height: float; bmi: float
  age, height, bmi = \
  args[0], args[1], args[2]
  traveler: List = []
  gotoxy(8, 9); print("» Validating data to know if you are")
  gotoxy(11, 10); print("an ideal candidate to travel.")
  # Test 1.
  sms_proc = "(Processing"
  gotoxy(8, 12); print("~ Age         (23-37)")
  processing(30, 12, sms_proc)
  if age in range(23, 38):
    gotoxy(30, 12); print('[ ✓ ]')
    traveler.append(True)
  else:
    gotoxy(30, 12); print('[ X ]')
    traveler.append(False)
  # Test 2.
  gotoxy(8, 13); print("~ Height  (1.50-1.90)")
  processing(30, 13, sms_proc)
  number_height = [round(i, 2) for i in np_range(1.50, 1.91, 0.01)]
  if binary_search(number_height, height):
    gotoxy(30, 13); print('[ ✓ ]')
    traveler.append(True)
  else:
    gotoxy(30, 13); print('[ X ]')
    traveler.append(False)
  # Test 3.
  gotoxy(8, 14); print("~ BMI (             )")
  processing(30, 14, sms_proc)
  if bmi < 18.5:
    gotoxy(15, 14); print(' Underweight ')
    gotoxy(30, 14); print('[ X ]')
    traveler.append(False)
  elif bmi >= 18.5 and bmi < 25:
    gotoxy(15, 14); print('Normal weight')
    gotoxy(30, 14); print('[ ✓ ]')
    traveler.append(True)
  elif bmi >= 25 and bmi < 30:
    gotoxy(15, 14); print(' Overweight  ')
    gotoxy(30, 14); print('[ X ]')
    traveler.append(False)
  elif bmi >= 30:
    gotoxy(15, 14); print('   Obesity   ')
    gotoxy(30, 14); print('[ X ]')
    traveler.append(False)
  if False in traveler: return False
  else: return True

def goodbyes(name: str, choice: bool) -> None:
  """Farewell to the traveler and tells him
  if he passed the test to make the trip or not."""

  if choice:
    gotoxy(6, 16); print("→ Congratulations {}! You are an ideal candidate.".format(name))
  else:
    gotoxy(6, 16); print("→ Sorry {}, you are not an ideal candidate.".format(name))
  gotoxy(0, 17); print('')
  gotoxy(8, 18); print("→ Press a key to exit..."); input('')


# Utilities

def calculate_bmi(weight: float, height: float) -> float:
  """Calculate the Body Mass Index."""

  return round(weight / (height**2), 1)

def binary_search(list_num: List, item: float) -> Any:
  """Binary search algorithm."""

  if len(list_num) == 0: return False
  else:
    midpoint = len(list_num) // 2
    if list_num[midpoint] == item: return True
    else:
      if item < list_num[midpoint]: return binary_search(list_num[:midpoint], item)
      else: return binary_search(list_num[midpoint+1:], item)

def gotoxy(x: int, y: int) -> None:
  """This function is in charge of positioning
     the cursor on any axis of the console."""

  print ("%c[%d;%df" % (0x1B, y, x), end='')

def clean_screen() -> None:
  """This function is responsible for cleaning the screen."""

  if system() == 'Windows': console_command('cls')
  else: console_command('clear')

def sleep_screen(x: int=4, y: int=20, error: str='',
                 date_input: Any='', time: int=3) -> None:
  """This function is responsible for cleaning the
     screen while waiting a few seconds."""

  for second in reversed(range(1, time+1)):
    gotoxy(x+len(error), y); print(' '*150)
    if second != 1:
      gotoxy(x+len(error), y); print("  //  Wait", second, "seconds!")
      sleep(1)
    else:
      gotoxy(x+len(error), y); print("  //  Wait", second, "second !")
      sleep(1)
  gotoxy(x-len(date_input), y); print(' '*200)


# Main program.

def main():
  ERROR_MESSAGE = "    Please enter a valid information..."
  welcome_traveler()
  clean_screen()
  gotoxy(4, 4); print("INTERSTELLAR TRAVEL    ⊂(◉‿◉)つ")
  gotoxy(10, 6); print("TRAVELER DATA")
  names_tvl:      str =  validate_strings(10, 8, "→  Names                      : ", ERROR_MESSAGE)
  birthday_tvl:  date =    validate_dates(10, 9, "→  Birthday  (year/month/day) : ", ERROR_MESSAGE)
  age_tvl:        int =     calculate_age(birthday_tvl)
  gotoxy(10, 10);                          print("→  Age                        :", str(age_tvl), 'years old')
  gender_tvl:     str =  validate_gender(10, 11, '→  Gender (Male"M"|Female"F") : ', ERROR_MESSAGE)
  blood_type_tvl: str =   validate_blood(10, 12, "→  Blood Type   (O+, A-...N±) : ", ERROR_MESSAGE)
  height_tvl:   float =  validate_floats(10, 13, "→  Height            (Meters) : ", ERROR_MESSAGE, 'h')
  weight_tvl:   float =  validate_floats(10, 14, "→  Weight         (Kilograms) : ", ERROR_MESSAGE, 'w')
  gotoxy(6, 16);                           print("→ Press a key to continue..."); input('')
  bmi_tvl:      float = calculate_bmi(weight_tvl, height_tvl)
  choice_tvl:    bool = choice_of_traveler((age_tvl, height_tvl, bmi_tvl))
  goodbyes(names_tvl, choice_tvl)
  clean_screen()


if __name__ == '__main__':
  main()