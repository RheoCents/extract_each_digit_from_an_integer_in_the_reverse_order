print('This code will reverse your inputted number and add spaces in between')
user_input_number = int(input('Now can you give me a number? '))
print('Your reversed number is:')

for i in range (-1,((len(str(user_input_number))*-1)-1),-1):
    print(str(user_input_number)[i], end=" ")