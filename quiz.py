print("Hello!:)")
print("Welcome! to my quiz about human muscle")
play=input("Do you want to play? ")

if play.lower() != "yes":
    quit()
else:
    print("lets get started :)")
    score=0

#first question
question=input("what is the biggest muscle in the human body? ")

if question.lower() =="glutes":
    print("Good job! lets continue.")
    score += 1
else:
    print("incorect")
#second question
question=input("Which muscle is responsible for the movement of the upper arm and shoulder, often known as the shoulder muscle? ")

if question.lower() =="deltoid":
    print("fantastic! lets continue.")
    score +=1


else:
    print("incorect")

#third question
question=input("What is the strongest muscle in the human body ")

if question.lower() =="jaw muscle":
    print("WOW! you are very good at this, lets continue.")
    score +=1
else:
    print("incorect")

#forth question
         
question=input(" What is the name of the muscle group located on the back of the upper arm? ")

if question.lower() =="triceps":
    print("Good job! you have compited the quiz.")
    score +=1

    print("you have got"  +  str(score) + "question(s) correct")
else:
    print("incorect")