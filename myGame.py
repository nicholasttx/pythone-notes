import  random
import  sys

secret = random.randint(1,100)

print ("----- Willie's little guessing game-------")
print ("-----" + sys.version + "-----")

temp = input("Let's guess what the number is the right one!")
myAnswer = int(temp)

timesOfTry = 1

while myAnswer != secret:
#    temp = input("Wrong answer, please try again!")

#    if myAnswer == secret:
#        print ("Yay, you got it!\n")

    print ("Try of number : ", timesOfTry)

    if myAnswer > secret:

        newAnswer = input("This is greater, try smaller number!\n")
        myAnswer = int(newAnswer)

    elif myAnswer < secret:

        newAnswer = input("This is smaller, try greater number!\n")
        myAnswer = int(newAnswer)

    else:
        print ("Hmm, let me think... \n")

    timesOfTry += 1

print ('Yay, you got it! Game over, have a nice day!')




