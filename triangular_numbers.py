# Triangular number
# A triangular number or triangle number counts objects arranged in an equilateral triangle.
# The nth triangular number is the number of dots in the triangular arrangement with n dots on
# each side, and is equal to the sum of the n natural numbers from 1 to n.
# Source: https://en.wikipedia.org/wiki/Triangular_number

def generate_triangular_number(n):
  # The nth triangular number is the sum from 1...n. There is a simple formula for this:
  # sum = n(n+1)/2
  return (n * n+1) / 2

def generate_triangular_numbers():
  # Only generate the first 100 to prove the point
  triangular_numbers = []
  for i in range(100):
    triangular_numbers.append(generate_triangular_number(i))
  return triangular_numbers

print(generate_triangular_numbers())
