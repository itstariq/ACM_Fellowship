print("Welcome to Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("So! play :)")
score = 0

answer = input("Who Is the current president of india? ")
if answer.lower() == "droupadi murmu":
    print('Congrats you are right!')
    score += 1
else:
    print("sorry incorrect!")

answer = input("Who is the current president of Canada? ")
if answer.lower() == "justin trudo":
     print('Correct!')
    score += 1
else:
   print("sorry incorrect!")

answer = input("What does PCB stands for? ")
if answer.lower() == "pakistan cricket board":
    print('Congrats you are right!')
    score += 1
else:
    print("sorry incorrect!")

answer = input("When bangladesh seperated with pakistan? ")
if answer.lower() == "1971:
      print('Congrats you are right!')
    score += 1
else:
    print("sorry incorrect!")

print("You Score + str(score) + " questions correct!")
print("Your Score " + str((score / 4) * 100) + "%.")
