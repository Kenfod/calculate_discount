def large_power(base, exponent):
  """
  Checks if the result of base raised to the exponent is greater than 5000.

  Args:
      base: The base number.
      exponent: The exponent to which the base is raised.

  Returns:
      True if the result is greater than 5000, False otherwise.
  """
  result = base ** exponent
  return result > 5000

# Example usage
base_value = int(input("Enter the base value: "))
exponent_value = int(input("Enter the exponent value: "))

if large_power(base_value, exponent_value):
  print(f"{base_value}^{exponent_value} is greater than 5000")
else:
  print(f"{base_value}^{exponent_value} is not greater than 5000")
