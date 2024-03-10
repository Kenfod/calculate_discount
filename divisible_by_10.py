def divisible_by_ten(num):
  """
  Checks if a number is divisible by ten.

  Args:
      num: The number to check.

  Returns:
      True if the number is divisible by ten, False otherwise.
  """
  return num % 10 == 0  # Check if remainder after division by 10 is 0

# Example usage
numbers = [20, 35, 100, 121]
for num in numbers:
  if divisible_by_ten(num):
    print(f"{num} is divisible by ten")
  else:
    print(f"{num} is not divisible by ten")
