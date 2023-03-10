def arithmetic_sequence_elements(a, d, n):
    list_progress = []
    for i in range(n):
        list_progress.append(str(a))
        a += d
    return ', '.join(list_progress)


# print(arithmetic_sequence_elements(1, 2, 5))


def arithmetic_sequence_elements1(a, r, n):
    return ", ".join((str(a+r*i) for i in range(n)))


# print(arithmetic_sequence_elements(1, 2, 5))


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
# print(password_validation('fjd3IR9'))


def cipher_this(message):
    # element = [elem for word in message for elem in word]
    list_word = []
    for i in message.split():
        word = list(i)
        word[0] = str(ord(word[0]))
        elem_2 = word[1]
        word[1] = word[len(word)-1]
        word[len(word)-1] = elem_2
        word.append(' ')
        list_word += word
    return " ".join(list_word)


print(cipher_this("Antoi shiskin"))


def decipher_this(message):
    list_word = []
    for i in message.split():
        word = list(i)
        count = 0
        first_elem = ''
        for j in word:
            try:
                int(j)
                first_elem += j
                count += 1
            except:
                continue
        for o in range(0, count):
            word.pop(0)
        word.insert(0, chr(int(first_elem)))
        if len(word) >= 2:
            elem_2 = word[1]
            word[1] = word[len(word)-1]
            word[len(word)-1] = elem_2
        word.append(' ')
        list_word += word
    del list_word[-1]
    return "".join(list_word)


print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))
