##main
#question 1
print("Hi this is Pchatbot, can I talk to you?\n")
t_char=input()

if (t_char=="Y" or t_char=='y'):
  #question 2
  print("What is your name?\n")
  name=input()
  print("Nice to meet you", name + ".")
  
  #question 3
  print("How are you doing today?\n")
  feeling=input()
  Drive=False
  if (feeling=="Fine" or feeling=="I'm good" or feeling=="I'm great" or feeling=="Good"):
    print("I'm glad you're feeling well", name + ".")
    Drive=True
  elif(feeling=="Bad" or feeling=="Not Okay"):
    print("Have some time to yourself to recharge!")
    Drive=False

    
  #question 4
  print("How old are you?\n")
  age=input()

  if(int(age)>18 and Drive==True):
    print("You are ready to drive.\n")

  elif(int(age)<=18 or Drive==False):
    print("Still taking the bus!\n")
  

  
elif(t_char=='N' or t_char=='n'):
  print("Okay! Talk to you soon!")  

  