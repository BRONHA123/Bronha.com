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
  print("[Robot] >>> Be strong, I am always with you!") 
  d=raw_input("[You] >>> ")
  print("[Robot] >>> Do you love Bronha?\n=============================\n1. Yes!\n2. No! \n=============================\n[You] >>> ")
  h=raw_input() 
  if h==1:
    print("oh.........! 😂 Did you tell him already?\n=============================\n1. Yes. \n2. No.\n=============================")
    i=raw_input()
    if i==1:
      Print("[Robot] >>> He love you or not?\n=============================\n1. Yes he love me too.\n2. No! He have his cr.\n=============================")
      j=raw_input() 
      if j==1:
        print("[Robot] >>> wish you and him..... 😂")
        print("[You] >>> ")
        print("[Robot] >>> Now i want to sleep 😴") 
        time.sleep(2)
        os.exit("[System] >>> Robot is sleeping now!") 
      else:
        print("[System] >>> Your input is wrong please see the options above") 
        j=raw_input() 
      if j==2:
        print("[Robot] >>> Ohh so sad, Be strong, I'm here with you!.")
        k=raw_input("[You] >>> ") 
        print("[Robot] >>> I want to sleep now! Goodbye!")
        time.sleep(2)
        os.exit("[System] >>> Robot is sleeping now!") 
      else:
        print("[System] >>> Your input is wrong please see the options above") 
        j=raw_input()
    else:
      print("[System] >>> Your input is wrong please see the options above") 
      i=raw_input()
    if i==2:
      print("[Robot] >>> So why you not tell him?")
      raw_input("[You] >>> ") 
      print("[Robot] >>> Rrrrrr!")
      time.sleep(3)
      print("[Robot] >>> Sorry, I want to sleep now!") 
      time.sleep(2)
      os.exit("[System] >>> Robot is sleeping now!") 
    else:
      print("[System] >>> Your input is wrong please see the options above") 
      i=raw_input()
  else:
    print("[System] >>> Your input is wrong please see the options above") 
    i=raw_input()
  if h==2:

    print("[Robot] >>> why?")
    raw_input("[You] >>> ") 
    print("[Robot] >>> Rrrrrr!")
    time.sleep(3)
    print("[Robot] >>> Sorry, I want to sleep now!") 
    time.sleep(2)
    os.exit("[System] >>> Robot is sleeping now!") 
  else:
    print("[System] >>> Your input is wrong please see the options above") 
    h=raw_input()
  print("[Robot] >>> hmmm i am a baby Robot so i don't have something to say with you more")
  e=raw_input("[You] >>> ")
  print("[System] >>> (Robot is sleeping)") 
else:
    print("[System] >>> Your input is wrong please see the options above") 
    c=raw_input()
if(c==2):
  print("[Robot] >>> So good!")
  f=raw_input("[You] >>> ")
  print("[Robot] >>> hmmm i am a baby Robot so i don't have something to say with you more")
  g=raw_input("[You] >>> ")
  print("[System] >>> (Robot is sleeping)") 
else:
    print("[System] >>> Your input is wrong please see the options above") 
    c=raw_input()
