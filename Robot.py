import time
time.sleep(2)
num1="1"
numh2="2"
num2="2"
print("\n\n[Robot] >>> Hello")
time.sleep(1)
print("[Robot] >>> What's your name?")
print("[You] >>> ")
b=raw_input() 
time.sleep(1)
print("[Robot] >>> Nice to meet you "+b) 
time.sleep(1)
print("[Robot] >>> How are you feeling now?\n=============================\n1. Sad\n2. Happy\n=============================")
print(">Choose the number of the option above \n[You] >>> ") 
c=raw_input() 

if(c==num1):
  print("[Robot] >>> Why? ")
  raw_input("[You] >>> ")
  time.sleep(2)
  print("[Robot] >>> Be strong, I am always with you!") 
  raw_input("[You] >>> ")
  time.sleep(1)
  print("[Robot] >>> Do you love Bronha?\n=============================\n1. Yes!\n2. No! \n=============================\n[You] >>> ")
  h=raw_input() 
  loven="Panha"
  
  if h==num1:
    time.sleep(2)
    if b==loven:
      print("[Robot] >>> Oh really?  He loves you too, but he doesn't tell you because he doesn't want to love you or he doesn't have a good time with you!  And if you want to know more, please ask him yourself!")
    else:
    	print("[Robot] >>> Ohh sad, he have his cr already, sorry i can't help you")
        raw_input("[You] >>> ")
        print("[Robot] >>> sorry i want to sleep now bye!")
        time.sleep(2)
        print("[System] >>> Robot is sleeping now!")

  if h==numh2:
    print("[Robot] >>> Oh why?")
    raw_input("[You] >>> ") 
    print("[Robot] >>> Rrrr....") 
    time.sleep(1)
    print("[Robot] >>> Hey! i want to sleep right now!") 
    time.sleep(2)
    print("[System] >>> Robot is sleeping now!") 

if(c==num2):
  print("[Robot] >>> So good!")
  raw_input("[You] >>> ")
  time.sleep(3)
  print("[Robot] >>> hmmm i am a baby Robot so i don't have something to say with you more")
  raw_input("[You] >>> ")
  time.sleep(2)
  print("[System] >>> Robot is sleeping now!")
print("\n\ncreated by @BRONHA!\nCONTACT : http://www.bronha.xyz") 










