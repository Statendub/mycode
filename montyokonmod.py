#!/usr/bin/env python3

#This is short for, ‘else-if’, as in, “our condition wasn’t matched in the if statement, but it maybe matched in this statement”. Here, we want to code what is going to happen if we hit the third round, and the user didn’t type ‘Brian’. We’re still in the while-loop, so indent four spaces.


round = 0    # # integer round initiated to 0
while(True): # sets up an infinite loop condition
    round = round + 1    # increase the round counter to wherever you need
    print('finish the movie title, "monty python\'s the life of ______"')
    answer = input()   # string answer collected from user
    if (answer.upper() == 'BRIAN'):  # logic to check if user gave correct answer, modified to accept upper or lower
        print('CORRECT!')
        break
    elif (answer.upper() == 'SHRUBBERY'): # This is short for, ‘else-if’, as in, “our condition wasn’t matched in the if statement, but it maybe matched in this statement, use this as the "OR" option
        print('YOU GOT THE SECRET ANSWER!')
        break
    elif(round==3):    # Here, we want to code what is going to happen if we hit the third round, and the user didn’t type ‘Brian’. We’re still in the while-loop
        print('Sorry the answer as Brian') #Indent 8 spaces (4 for the while-loop + 4 for the elif), and print a message of dissapointment to the screen.
        break  #we’d want to escape the program at this point, because the program has ended. So, indent 8 whitespaces and then write the word break
    else:
        print('Sorry try again')



