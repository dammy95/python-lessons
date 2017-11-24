def calculator(*args, operation='add', output_format='float'):
  if len(args) < 2:
    return args

  result = args[0]

  for num in args[1:]:
    if operation == 'add':
      result += num
    elif operation == 'sub':
      result -= num
    elif operation == 'mul':
      result *= num
    elif operation == 'div':
      result /= num
    else:
      raise ValueError("Invalid Operator")

  if output_format == 'float':
    result = float(result)
  elif output_format == 'int':
    result = round(result)
  else:
    raise ValueError("Invalid output format")

  return result


if __name__ == '__main__':
    print(calculator(2, 3.0))
    print(calculator(2, 3.0, output_format='int'))
    print(calculator(2, 3.0, operation='div'))  
    print(calculator(2, 3.0, operation='div', output_format='int'))  
