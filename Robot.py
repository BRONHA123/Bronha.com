import time


print("\n\n[Robot] >>> Hello")

print("[Robot] >>> What's your name?")
print("[You] >>> ")
b=raw_input() 
print("[Robot] >>> Nice to meet you "+b) 
print("[Robot] >>> What's your feeling now?\n=============================\n1. Sad\n2. Happy\n=============================")
print(">Choose the option above\n[You] >>> ") 
c=raw_input() 

if(c==1):
  print("[Robot] >>> Why? ")
  d=raw_input()
  print("[Robot] >>> Be strong, I am always with you!") 
  d=raw_input("[You] >>> ")
  print("[Robot] >>> Do you love Bronha?\n=============================\n1. Yes!\n2. No! \n=============================\n[You] >>> ")
  h=raw_input() 
  if h==1:
    print("oh.........! Did you tell him already?\n=============================\n1. Yes. \n2. No.\n=============================")
    
  
if(c==2):
  print("[Robot] >>> So good!")
  f=raw_input("[You] >>> ")
  print("[Robot] >>> hmmm i am a baby Robot so i don't have something to say with you more")
  g=raw_input("[You] >>> ")
  time.sleep(2)
  print("[System] >>> (Robot is sleeping)")


