def rec_factorial(n):
  if n < 2:
    return 1

  return n * rec_factorial(n - 1)

if __name__ == '__main__':
  print(rec_factorial(3))
  print(rec_factorial(4))
  print(rec_factorial(6))
