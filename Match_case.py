score = int(input("Enter your score: ")) #User enters score

match score:
  case _ if 81 < score <= 100: # Checks if the score is between 81 to 100
   print("You got grade A:", "your score is",score) 

  case _ if 71 < score <= 80: # Checks if the score is 71 to 80
   print("You got grade B:", "your score is",score)

  case _ if 61 < score <= 70: # Checks if the score is 61 to 70
   print("You got grade C:", "your score is",score)

  case _ if 50 <= score <= 60: # Checks if score is between 50 and 60
     print("You got a D:", "your score is",score)

  case _ if 30 < score <= 49: # Checks if score is between 31 and 49
     print("You got a pass:", "your score is",score)

  case _:
   print("You failed the exam!,", "your score is",score)