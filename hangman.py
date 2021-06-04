import time

name = input("What is your name? ")

print ("Hello, " + name+ " Time to play hangman!")

print (" ")

time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

#here we set word as secret
word = "secret"

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

        if char in guesses:    
            print (char)    

        else:
            print ("_"),     
            failed += 1    

    if failed == 0:        
        print ("You won"  )

        break              

    print

    guess = input("guess a character:") 

    guesses += guess                    

    if guess not in word:  
 
        turns -= 1        
 
        print ("Wrong")
 
        print ("You have", + turns, 'more guesses' )
 
        if turns == 0:           
    
            print ("You Lose")
