'''
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
'''

def password_generator(length:int = 10):
    '''Function which generates password with a mix of lowercase letters, uppercase letters, numbers, and symbols
     based on length specified in parameter '''
    import random
    import string

    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    numbers = list(range(0, 10))
    symbols = list('{}()[].,:;+-*/&|<>=~$')

    big_dict = dict(lowercase=lowercase, uppercase=uppercase, numbers=numbers, symbols=symbols)

    # Generate list of 4 numbers with sum = password length
    num_list = [random.randrange(1, 5) for i in range(4)]
    share_list = [i*length/sum(num_list) for i in num_list]
    rand_element_count = [int(round(i)) for i in share_list]

    # Adjust the list if sum != password length
    if sum(rand_element_count) != length:
        diff = length-sum(rand_element_count)

        for i in range(1, 5):
            if rand_element_count[-i] > 1:
                rand_element_count[-i] += diff
                break


    # Generate password
    # create dictionary from a list
    elements_count_dict = dict(lowercase=rand_element_count[0],
                            uppercase=rand_element_count[1],
                            numbers=rand_element_count[2],
                            symbols=rand_element_count[3])

    password_list = [random.sample(big_dict[key], elements_count_dict[key]) for key in big_dict]

    # Unpack list of lists
    password_list = [str(item) for element in password_list for item in element]

    # Random sort
    password_list = sorted(password_list, key=lambda x: random.random())

    # Join all elements
    password = ''.join(password_list)

    return password

new = password_generator(8)
print(new)