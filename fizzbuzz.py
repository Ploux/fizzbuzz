"""
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
"""

def fizzbuzz():
  arr = []
  for i in range(1,101):
    if (i % 15 == 0):
      arr.append("Fizzbuzz")
    elif (i % 3 == 0):
      arr.append("Fizz")
    elif (i % 5 == 0):
      arr.append("Buzz")
    else:
      arr.append(i)

  return arr