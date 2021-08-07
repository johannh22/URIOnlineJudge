# -*- coding: utf-8 -*-
# Function that performs the repeated removal
def circRemove(n, k):
  step = k - 1 # The real step is k-1 since you count from the removed element
  circle = [x + 1 for x in range(n)] # Generates the circle
  i = 0 # Index of the element to be removed
  while len(circle) > 1:
    i = (i + step) % len(circle)
    circle.pop(i)

  return circle[0]

def main():
  NC = int(input())
  for i in range(1,NC+1):
    n, k = [int(x) for x in input().split()]
    print(f"Case {i}: {circRemove(n, k)}")

main()
