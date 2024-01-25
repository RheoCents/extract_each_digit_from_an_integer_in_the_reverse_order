print('This code will reverse your inputted number and add spaces in between')
user_input_number = input('Now can you give me a number? ')

for i in range (-1,((len(user_input_number)*-1)-1),-1):
    print(user_input_number[i], end="")