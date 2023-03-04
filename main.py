def arithmetic_sequence_elements(a, d, n):
    list_progress = []
    for i in range(n):
        list_progress.append(str(a))
        a += d
    return ', '.join(list_progress)


print(arithmetic_sequence_elements(1, 2, 5))


def arithmetic_sequence_elements1(a, r, n):
    return ", ".join((str(a+r*i) for i in range(n)))


print(arithmetic_sequence_elements(1, 2, 5))


def alphanumeric(password):
    result = False
    for element in password:
        if element in ['!','@','#','$','%','^','&','*','(',')', ' ','<','>', '|', '_', '+', '=', '-']:
            result = False
        elif element in str(range(0, 10)):
            result = True

    return result


#print(alphanumeric("hell0 world_"))
#print(alphanumeric("4Y>qkqlWSWBU"))


def alphanumeric1(password):
    if password.isalnum() == True:
        return True
    return False

#print(alphanumeric1("0fw787"))
#print(alphanumeric1("Y34535>qkqlWSWBU"))


def password_validation(regex):
    if (regex.isalnum() == True) and (regex.lower() == regex) == False:
        return True
    return False

regex = 'Fjd3IR9'
#print(regex.lower())
print(password_validation('fjd3IR9'))
