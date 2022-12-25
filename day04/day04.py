numbers = list(map(int, input("Enter a list of integers: ").split()))

sum = 0
for number in numbers:
  sum += number
average = sum / len(numbers)

print(average)
print("Numbers greater than the average:")
for number in numbers:
  if number > average:

    print(number)