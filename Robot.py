import time


print("\n\n[Robot] >>> Hello")

print("[Robot] >>> What's your name?")
print("[You] >>> ")
b=raw_input() 
print("[Robot] >>> Nice to meet you "+b) 
print("[Robot] >>> What's your feeling now?\n=============================\n1. Sad\n2. Happy\n=============================")
print(">Choose the option above\n[You] >>> ") 
c=raw_input() 
num1="1" 
if(c==num1):
  print("[Robot] >>> Why? ")
  raw_input("[You] >>> ")
  print("[Robot] >>> Be strong, I am always with you!") 
  raw_input("[You] >>> ")
  print("[Robot] >>> Do you love Bronha?\n=============================\n1. Yes!\n2. No! \n=============================\n[You] >>> ")
  h=raw_input() 
  loven="Panha"
  
  if h==num1:
    time.sleep(2)
    if b==loven:
      print("[Robot] >>> Oh really?  He loves you too, but he doesn't tell you because he doesn't want to love you or he no time with you!  And if you want to know more, please ask him yourself!")
    else:
    	print("[Robot] >>> but he have his cr, sorry i can't help you")
        raw_input("[You] >>> ")
        print("[Robot] >>> sorry i want to sleep now bye!")
        time.sleep(2)
        os.exit("[System] >>> Robot is sleeping now!")
  if h==num2:
    print("[Robot] >>> Oh why?")
    raw_input("[You] >>> ") 
    print("[Robot] >>> Rrrr....") 
    time.sleep(1)
    print("[Robot] >>> Hey! i want to sleep right now!") 
    time.sleep(2)
    os.exit("[System] >>> Robot is sleeping now!") 
num2="2"
if(c==num2):
  print("[Robot] >>> So good!")
  f=raw_input("[You] >>> ")
  print("[Robot] >>> hmmm i am a baby Robot so i don't have something to say with you more")
  g=raw_input("[You] >>> ")
  time.sleep(2)
  print("[System] >>> Robot is sleeping now!")










