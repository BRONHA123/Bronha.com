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
  if h==1 and b=="Panha":
    print("[Robot] >>> Oh really?  He loves you too, but he doesn't tell you because he doesn't want to love you!  And if you want to know more, please ask him yourself!")
  if h==1:
    	print("[Robot] >>> but he have his cr, sorry i can't help you")
        raw_input("[You] >>> ")
        print("[Robot] >>> sorry i want to sleep now bye!")
        time.sleep(2)
        os.exit("[System] >>> Robot is sleeping now!")
    
  if h==2:
  	print("[Robot] >>> Why? ")
    Z=raw_input("[You] >>> ")
    print("[Robot] >>> hmm so sad !")
    
if(c==2):
  print("[Robot] >>> So good!")
  f=raw_input("[You] >>> ")
  print("[Robot] >>> hmmm i am a baby Robot so i don't have something to say with you more")
  g=raw_input("[You] >>> ")
  time.sleep(2)
  print("[System] >>> (Robot is sleeping)")










