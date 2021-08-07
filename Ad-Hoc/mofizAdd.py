# -*- coding: utf-8 -*-

def addMofiz(a, b):
    a += (1 << 32)
    b += (1 << 32)
    return a^b
    
def main():
  while True:
    try:
      a, b = [int(n) for n in input().split()]
      if '' not in [a, b]:
        print(addMofiz(a, b))
      else:
        return
    except EOFError:
      return
    
main()
    