#!/usr/bin/env python3

userInput = input("type something")

if(userInput == 'hot'):
    print('The weather is', userInput, 'you should wear sandals')
elif(userInput == 'rain'):
    print('The weather is', userInput, 'you should wear galoshes')
elif(userInput == 'snow'):
    print('The weather is', userInput, 'you should wear boots')
else:
    print('The weather is', userInput, 'you should wear shoes')

inputNumberA = int(input("1st# = "))
inputNumberB = int(input("2nd# = "))
inputNumberC = input("operator = ")
inputNumberD = int(input("answer = "))


if(inputNumberC == '+'):
    answer = inputNumberA + inputNumberB
elif (inputNumberC == '-'):
    answer = inputNumberA - inputNumberB
elif(inputNumberC == '*'):
    answer = inputNumberA * inputNumberB
elif(inputNumberC == '/'):
    answer = inputNumberA / inputNumberB

if (inputNumberD == answer):
    print(inputNumberD, 'Is correct')
else:
    print(inputNumberD, 'Is not correct!', answer, 'is the correct Answer')