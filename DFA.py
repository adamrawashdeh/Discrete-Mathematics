'''
Name: Adam Rawashdeh
UCID: aor9
'''
#prompts the user if they want to enter a string
def question():
    print("Do you want to enter a string?")
    user_input = input()
    return user_input

def state1(curr):
    if curr.isalpha(): #checks to see if current character is letter a-z
        nextState = 2 #if so, it moves on to state 2
    else: #if not than it means it's not valid and is sent to the trap state
        nextState = 9 #state 9 is trap state
    return nextState #return the next state

def state2(curr):
    if curr.isalpha(): #checks to see if current character is letter a-z
        nextState = 2 #if so, it stays on state 2
    elif curr == '@': #checks to see if the current chracter is an @
        nextState = 3 #if so, it moves on to state 3
    elif curr == '.': #else if the current character is not a-z, we check to see if it's a dot
        nextState = 1 #if it's a dot we move back to state 1
    else: #if not than it means it's not valid and is sent to the trap state
        nextState = 9 #state 9 is trap state
    return nextState #return the next state

def state3(curr):
    if curr.isalpha(): #checks to see if current character is letter a-z
        nextState = 4 #if so, it moves on to state 4
    else: #if not than it means it's not valid and is sent to the trap state
        nextState = 9 #state 9 is trap state
    return nextState #return the next state

def state4(curr):
    if curr.isalpha(): #checks to see if current character is letter a-z
        nextState = 4 #if so, it stays on state 4
    elif curr == '.': #else if the current character is not a-z, we check to see if it's a dot
        nextState = 5 #if it's a dot we move on to state 5
    else: #if not than it means it's not valid and is sent to the trap state
        nextState = 9 #state 9 is trap state
    return nextState #return the next state

def state5(curr):
    if curr == 'c': #checks to see if the current chracter is c
        nextState = 6 #if so, we move on to state 6
    elif curr.isalpha(): #checks to see if current character is letter a-z
        nextState = 4 #if so, it moves back to state 4
    else: #if not than it means it's not valid and is sent to the trap state
        nextState = 9 #state 9 is trap state
    return nextState #return the next state

def state6(curr):
    if curr == 'o': #checks to see if the current chracter is o
        nextState = 7 #if so, we move on to state 7
    elif curr.isalpha(): #checks to see if current character is letter a-z
        nextState = 4 #if so, it moves back to state 4
    elif curr == '.': #else if the current character is not a-z, we check to see if it's a dot
        nextState = 5 #if it's a dot we move back to state 5
    else: #if not than it means it's not valid and is sent to the trap state
        nextState = 9  #state 9 is trap state
    return nextState #return the next state

def state7(curr):
    if curr == 'm': #checks to see if the current chracter is m
        nextState = 8 #if so, we move on to state 8
    elif curr.isalpha(): #checks to see if current character is letter a-z
        nextState = 4 #if so, it moves back to state 4
    elif curr == '.': #else if the current character is not a-z, we check to see if it's a dot
        nextState = 5 #if it's a dot we move back to state 5
    else: #if not than it means it's not valid and is sent to the trap state
        nextState = 9 #state 9 is trap state
    return nextState #return the next state

def state8(curr):
    if curr.isalpha(): #checks to see if current character is letter a-z
        nextState = 4 #if so, it moves back to state 4
    elif curr == '.': #else if the current character is not a-z, we check to see if it's a dot
        nextState = 5 #if it's a dot we move back to state 5
    else: #if not than it means it's not valid and is sent to the trap state
        nextState = 9 #state 9 is trap state
    return nextState #return the next state

def RejectOrAccpet(email):
    state = 1 #sets state to 1 since it's our starting state
    dfa = [[None, 'q1']] #2d array which will contain the states and each character from the email
    for i in range(len(email)): #loop to go through each character in the email
        if state == 1: #checks to see what state we're on
            state = state1(email[i]) #sets state to the next we're going to look for based off what was returned from state 1
            dfa.append([email[i], 'q' + str(state)])
        elif state == 2: #checks to see what state we're on
            state = state2(email[i]) #sets state to the next we're going to look for based off what was returned from state 2
            dfa.append([email[i], 'q' + str(state)]) #we append the current state and the character recieved on that state
        elif state == 3: #checks to see what state we're on
            state = state3(email[i]) #sets state to the next we're going to look for based off what was returned from state 3
            dfa.append([email[i], 'q' + str(state)]) #we append the current state and the character recieved on that state
        elif state == 4: #checks to see what state we're on
            state = state4(email[i]) #sets state to the next we're going to look for based off what was returned from state 4
            dfa.append([email[i], 'q' + str(state)]) #we append the current state and the character recieved on that state
        elif state == 5: #checks to see what state we're on
            state = state5(email[i]) #sets state to the next we're going to look for based off what was returned from state 5
            dfa.append([email[i], 'q' + str(state)]) #we append the current state and the character recieved on that state
        elif state == 6: #checks to see what state we're on
            state = state6(email[i]) #sets state to the next we're going to look for based off what was returned from state 6
            dfa.append([email[i], 'q' + str(state)]) #we append the current state and the character recieved on that state
        elif state == 7: #checks to see what state we're on
            state = state7(email[i])#sets state to the next we're going to look for based off what was returned from state 7
            dfa.append([email[i], 'q' + str(state)]) #we append the current state and the character recieved on that state
        elif state == 8: #checks to see what state we're on
            state = state8(email[i]) #sets state to the next we're going to look for based off what was returned from state 8
            dfa.append([email[i], 'q' + str(state)]) #we append the current state and the character recieved on that state
        else: #if none of the states above we're entered for the currrent string than we've entered a trap state
            dfa.append([email[i], 'q' + str(state)]) #we append the trap state and the character recieved on that state
            continue #we continue looping through the rest of the string

    if state == 7 or state == 8: 
        return ['Accepted', dfa] #we return accepted if loop ends on a state which is 7 or 8
    return ['Rejected', dfa] #if not than we the string entered by the user is rejected and so we reuturn it

if __name__ == "__main__":
    print("Project 1 for CS 341, 007\nSemester: Fall 2023\nWritten by: Adam Rawashdeh, aor9\nInstructor: Marvin Nakayama, marvin@njit.edu")
    while (True): #continues while the user wants to keep entering emails
        if question() == 'y': #if user enters 'y' then they want to enter an email
            email = input("Enter email: ") #promps the user to enter an email
            f = open("output.txt", "a") #opens a file by the name of output.txt and appends to it
            f.write(email + "\n")
            f.write("This table shows what's being read and the state it's going to (None means nothing read):" + "\n")
            f.write("State Symbol" + "\n")
            for i in RejectOrAccpet(email)[1]: 
                f.write(str(i) + "\n")
            f.write(RejectOrAccpet(email)[0] + "\n") #we append to the file if the email was accepeted or rejected
            f.write("\n")
            f.close() #we close the file
        else: # if user enters 'n' then they are finished entering emails
            exit(1) #terminates the program