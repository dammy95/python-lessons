def gen(n):
  for i in range(0, n + 1):
    yield n - i

if __name__ == '__main__':
  g = gen(10)
  
  for i in g:
    print(i)
