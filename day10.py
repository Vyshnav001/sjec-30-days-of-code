number_of_marbles = int(input("Enter how many marbles you have: "))
def shareing_marbles(marbles, friends, min_marbles):
  if marbles == 0:
    yield []
  elif friends == 0:
      return
  else:
    for i in range(min_marbles, marbles + 1):
      for solution in shareing_marbles(marbles - i, friends - 1, min_marbles):
        yield [i] + solution

# for solution in shareing_marbles(number_of_marbles, 5, 2):
#   print(solution)


solution_count = sum(1 for _ in shareing_marbles(number_of_marbles, 5, 2))
print(f"Total number of possible combination is: {solution_count}")