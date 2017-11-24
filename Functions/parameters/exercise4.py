def calculator(num1, num2, operation='add', output_format='float'):
  result = 0

  if operation == 'add':
    result = num1 + num2
  elif operation == 'sub':
    result = num1 - num2
  elif operation == 'mul':
    result = num1 * num2
  elif operation == 'div':
    result = num1 / num2
  else:
    raise ValueError("Invalid Operator")

  if output_format == 'float':
    return float(result)
  if output_format == 'int':
    return round(result)
  else:
    raise ValueError("Invalid output format")
  return result


if __name__ == '__main__':
    print(calculator(2, 3.0))  
    print(calculator(2, 3.0, output_format='int'))  
    print(calculator(2, 3.0, operation='div'))  
    print(calculator(2, 3.0, operation='div', output_format='int'))  
