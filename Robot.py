import time
time.sleep(2)
num1="1"
numh2="2"
num2="2"
num3="3"
class allcolors:
  green = '\33[32m'
  endc = '\33[0m'
loven="Panha"
print("\n\n[Robot] >>> Hello")
time.sleep(2)
print("[Robot] >>> What's your name?\n[You] >>> ") 
b=raw_input() 
time.sleep(1)
print("[Robot] >>> Nice to meet you "+ allcolors.green + b + allcolors.endc) 
time.sleep(3)
print("[Robot] >>> How are you feeling now?\n=============================\n1. Sad\n2. Happy\n3. Missing your cr\n=============================")
print(">Choose the number of the option above \n[" + allcolors.green + b + allcolors.endc + "] >>> ") 
c=raw_input() 
time.sleep(1)
if(c==num1):
  print("[Robot] >>> Why? ")
  raw_input("[" + allcolors.green + b + allcolors.endc + "] >>> ")
  time.sleep(2)
  print("[Robot] >>> Be strong, I am always with you!") 
  raw_input("[" + allcolors.green + b + allcolors.endc + "] >>> ")
  time.sleep(1)
  print("[Robot] >>> Do you love Bronha?\n=============================\n1. Yes!\n2. No! \n=============================\n[" + allcolors.green + b + allcolors.endc + "] >>> ")
  h=raw_input() 
  
  
  if h==num1:
    time.sleep(2)
    if b==loven:
      print("[Robot] >>> Oh really?  He loves you too, but he doesn't tell you because he doesn't want to love you or he doesn't have a good time with you!  And if you want to know more, please ask him yourself!")
      raw_input("[" + allcolors.green + b + allcolors.endc + "] >>> ") 
      time.sleep(1)
      print("[Robot] >>> Sorry! i want to sleep now bye!")
      time.sleep(3)
      print("[System] >>> Robot is sleeping now!")
      time.sleep(2)
    else:
    	print("[Robot] >>> Ohh sad, he have his cr already, sorry i can't help you")
        raw_input("[" + allcolors.green + b + allcolors.endc + "] >>> ")
        print("[Robot] >>> Oh sorry, I want to help you, but there is no way because it is a heart decision") 
        time.sleep(2)
        print("[Robot] >>> i want to sleep now bye!")
        time.sleep(3)
        print("[System] >>> Robot is sleeping now!")

  if h==numh2:
    time.sleep(1)
    print("[Robot] >>> Oh why?")
    raw_input("[" + allcolors.green + b + allcolors.endc + "] >>> ") 
    time.sleep(1)
    print("[Robot] >>> Rrrr....") 
    time.sleep(1)
    print("[Robot] >>> Hey! i want to sleep right now!") 
    time.sleep(2)
    print("[System] >>> Robot is sleeping now!") 
    time.sleep(2)

if(c==num2):
  time.sleep(1)
  print("[Robot] >>> So good!")
  raw_input("[" + allcolors.green + b + allcolors.endc + "] >>> ")
  time.sleep(3)
  print("[Robot] >>> hmmm i am a baby Robot so i don't have something to say with you more")
  raw_input("[" + allcolors.green + b + allcolors.endc + "] >>> ")
  time.sleep(2)
  print("[System] >>> Robot is sleeping now!")
  time.sleep(2)
if(c==num3):
  print("Who?")
  raw_input("[" + allcolors.green + b + allcolors.endc + "] >>>") 
  print("[Robot] >>> Hahahaha!") 
  time.sleep(2)
print("\n\ncreated by @BRONHA!\nCONTACT : http://www.bronha.xyz") 










