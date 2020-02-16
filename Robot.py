import time


print("\n\n[Robot] >>> Hello\n=============================\n1. Hello\n=============================")
a=raw_input(">Choose the option above\n[You] >>> ")
print("[Robot] >>> What's your name?")
b=raw_input()
print("[Robot] >>> Nice to meet you "+b) 
print("[Robot] >>> What's your feeling now?\n=============================\n1. Sad\n2. Happy\n=============================")
print(">Choose the option above\n[You] >>> ")
c=raw_input()
if(c==1):
  print("[Robot] >>> Be strong, I am always with you!") 
  d=raw_input("[You] >>> ")
  print("[Robot] >>> hmmm i am a baby Robot so i don't have something to say with you more")
  e=raw_input("[You] >>> ")
  print("[Robot] >>> Robot is sleeping") 
if(c==2):
  print("[Robot] >>> So good!")
  f=raw_input("[You] >>> ")
  print("[Robot] >>> hmmm i am a baby Robot so i don't have something to say with you more")
  g=raw_input("[You] >>> ")
  print("[Robot] >>> Robot is sleeping") 
