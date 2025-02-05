#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = input("Enter a fahrenheit temperature: ")
  tempF= int(tempF)

  #Convert that temperature to celsius, rounding to 1 decimal precision
  tempC = (tempF - 32) * 5/9
  num = 3.1415926
  tempC = round(tempC, 2) # rounds to two place
  #Output converted temperature.

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
