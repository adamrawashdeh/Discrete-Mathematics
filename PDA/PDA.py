'''
Name: Adam Rawashdeh
UCID: aor9
'''

pda = ['--------->   :  q1'] #declare the pda transition array that will be holding whats being processed each transition
stack = [] #declaring our stack

#prompts the user if they want to enter a string
def question():
    print("Do you want to enter a string?")
    user_input = input()
    return user_input

def state1(curr):
    if curr == '%': #checks to see if current character is %
        stack.append(curr) #if so, append the % to the stack
        nextState = 2 #if so, it moves on to state 2
        pda.append('% , ε -> %   :  q2') #if so, we state the transition process
    else:
        nextState = -1 #if not than it means it's not valid and we set to -1 for the machine to crash
        pda.append('Program crashed when reading ' + curr + ' on state 1') #we state what caused the machine to crash
    return nextState #return the next state

def state2(curr):
    if curr == '#': #checks to see if current character is #
        nextState = 3 #if so, it moves on to state 3
        pda.append('# , ε -> ε   :  q3') #if so, we state the transition process
    else:
        nextState = -1 #if not than it means it's not valid and we set to -1 for the machine to crash
        pda.append('Program crashed when reading ' + curr + ' on state 2') #we state what caused the machine to crash
    return nextState #return the next state

def state3(curr):
    if curr == '(': #checks to see if current character is (
        stack.append(curr) #append the ( to the stack
        nextState = 3 #if so, it moves on to state 3
        pda.append('( , ε -> (   :  q3') #if so, we state the transition process
    elif curr == '.': #checks to see if current character is .
        nextState = 4 #if so, it moves on to state 4
        pda.append('. , ε -> ε   :  q4') #if so, we state the transition process
    elif curr in '0123456789': #checks to see if current character is digit 0-9
        nextState = 6 #if so, it moves on to state 6
        pda.append(curr + ' , ε -> ε   :  q6') #if so, we state the transition process
    else:
        nextState = -1 #if not than it means it's not valid and we set to -1 for the machine to crash
        pda.append('Program crashed when reading ' + curr + ' on state 3') #we state what caused the machine to crash
    return nextState #return the next state

def state4(curr):
    if  curr in '0123456789': #checks to see if current character is digit 0-9
        nextState = 5 #if so, it moves on to state 5
        pda.append(curr + ' , ε -> ε   :  q5') #if so, we state the transition process
    else:
        nextState = -1 #if not than it means it's not valid and we set to -1 for the machine to crash
        pda.append('Program crashed when reading ' + curr + ' on state 4') #we state what caused the machine to crash
    return nextState #return the next state

def state5(curr):
    if curr in '0123456789': #checks to see if current character is digit 0-9
        nextState = 5 #if so, it moves on to state 5
        pda.append(curr + ' , ε -> ε   :  q5') #if so, we state the transition process
    elif curr in '+-/*': #checks to see if current character is operator +,-,*, or /
        nextState = 3 #if so, it moves on to state 3
        pda.append(curr + ' , ε -> ε   :  q3') #if so, we state the transition process
    elif curr == ')': #checks to see if current character is )
        if stack[-1] == '(': #checks to see if top of the stack is (
            stack.pop() # if so, pop the ( from the stack 
            nextState = 7 #if so, it moves on to state 7
            pda.append(') , ε -> (   :  q7') #if so, we state the transition process
        else:
            pda.append('Program crashed when trying to pop ( on state 5') # else, we state what caused the machine to crash
            nextState = -1 #we set to -1 for the machine to crash
    elif curr == '>': #checks to see if current character is >
        if stack[-1] == '%': #checks to see if top of the stack is %
            stack.pop() #if so, pop the % from the stack
            nextState = 8 #if so, it moves on to state 8 (the accept state)
            pda.append('> , % -> ε   :  q8') #if so, we state the transition process
        else: 
            pda.append('Program crashed when trying to pop % on state 5') #else, we state what caused the machine to crash
            nextState = -1 #we set to -1 for the machine to crash
    else: #if not than it means it's not valid and we set to -1 for the machine to crash
        nextState = -1 #if not than it means it's not valid and we set to -1 for the machine to crash
        pda.append('Program crashed when reading ' + curr + ' on state 5') #we state what caused the machine to crash
    return nextState #return the next state

def state6(curr):
    if curr in '0123456789': #checks to see if current character is digit 0-9
        nextState = 6 #if so, it moves on to state 6
        pda.append(curr + ' , ε -> ε   :  q6') #if so, we state the transition process
    elif curr == '.': #checks to see if current character is .
        nextState = 5 #if so, it moves on to state 5
        pda.append('. , ε -> ε   :  q5') #if so, we state the transition process
    else:
        nextState = -1 #if not than it means it's not valid and we set to -1 for the machine to crash
        pda.append('Program crashed when reading ' + curr + ' on state 6') #we state what caused the machine to crash
    return nextState #return the next state

def state7(curr):
    if curr in '+-/*': #checks to see if current character is operator +,-,*, or /
        nextState = 3 #if so, it moves on to state 3
        pda.append(curr + ' , ε -> ε   :  q3') #if so, we state the transition process
    elif curr == '>': #checks to see if current character is >
        if stack[-1] == '%': #checks to see if top of the stack is %
            stack.pop() #if so, pop the % from the stack
            nextState = 8 #if so, it moves on to state 8 (the accept state)
            pda.append('> , % -> ε   :  q8') #if so, we state the transition process
        else:
            pda.append('Program crashed when trying to pop % on state 7') #else, we state what caused the machine to crash
            nextState = -1 #we set to -1 for the machine to crash
    elif curr == ')': #checks to see if current character is )
        if stack[-1] == '(': #checks to see if top of the stack is (
            stack.pop() #if so, pop the ( from the stack
            nextState = 7 #if so, it moves on to state 7
            pda.append(') , ε -> (   :  q7') #if so, we state the transition process
        else:
            pda.append('Program crashed when trying to pop ( on state 7') #else, we state what caused the machine to crash
            nextState = -1 #we set to -1 for the machine to crash
    else:
        nextState = -1 #if not than it means it's not valid and we set to -1 for the machine to crash
        pda.append('Program crashed when reading ' + curr + ' on state 7') #we state what caused the machine to crash
    return nextState #return the next state

def RejectOrAccpet(Language):
    state = 1 #sets state to 1 since it's our starting state
    for i in range(len(Language)): #loop to go through each character in the input
        if state == 1: #checks to see what state we're on
            state = state1(Language[i]) #sets state to the next we're going to look for based off what was returned from state 1
        elif state == 2: #checks to see what state we're on
            state = state2(Language[i]) #sets state to the next we're going to look for based off what was returned from state 2
        elif state == 3: #checks to see what state we're on
            state = state3(Language[i]) #sets state to the next we're going to look for based off what was returned from state 3
        elif state == 4: #checks to see what state we're on
            state = state4(Language[i]) #sets state to the next we're going to look for based off what was returned from state 4
        elif state == 5: #checks to see what state we're on
            state = state5(Language[i]) #sets state to the next we're going to look for based off what was returned from state 5
        elif state == 6: #checks to see what state we're on 
            state = state6(Language[i]) #sets state to the next we're going to look for based off what was returned from state 6
        elif state == 7: #checks to see what state we're on
            state = state7(Language[i]) #sets state to the next we're going to look for based off what was returned from state 7
        else: #if none of the states above we're entered for the currrent string than our machine will crash
            break #break out of the loop and stop reading characters
    
    if state == 8 and len(stack) == 0: 
        return ['Accepted', pda, stack] #we return accepted if loop ends on a state which is 8 and the stack is empty
    return ['Rejected', pda, stack] #if not than we say the input entered by the user is rejected and so we reject it

if __name__ == "__main__":
    print("Project 2 for CS 341\nSection: 007 \nSemester: Fall 2023\nWritten by: Adam Rawashdeh, aor9\nInstructor: Marvin Nakayama, marvin@njit.edu")
    while (True): #continues while the user wants to keep entering Languages
        stack = [] #reset stack for next input
        pda = ['--------->   :  q1'] #reset pda for next input
        if question() == 'y': #if user enters 'y' then they want to enter an Language
            Language = input("Enter Language: ") #promps the user to enter an Language
            f = open("output.txt", "a") #opens a file by the name of output.txt and appends to it
            f.write(Language + "\n")
            f.write("This table shows what's being read, popped, pushed, and the state it's going to in the form of read , pop -> push  : current state (Epsilon means nothing):" + "\n")
            result = RejectOrAccpet(Language)  # Call the function once and store the result
            for i in result[1]:
                f.write(str(i) + "\n")
            f.write("Stack at the end: " + str(stack) + "\n")
            f.write(result[0] + "\n")
            f.write("\n")
            f.close() #we close the file
        else: # if user enters 'n' then they are finished entering Languages
            exit(1) #terminates the program