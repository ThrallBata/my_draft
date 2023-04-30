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


# print(cipher_this("Antoi shiskin"))


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


# print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))


import itertools


def choose_best_sum(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls, k) if sum(i) <= t)
    except:
        return None


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# print(choose_best_sum(230, 2, xs))
#
#
# for i in itertools.combinations(xs, 3):
#     if sum(i) <= 230:
#         print(i)
#         print(sum(i))


# def twoSum(nums, target):
    # count = -1
    # for num in nums:
    #     count += 1
    #     for i in range(len(nums)):
    #         if count != i and (num + nums[i]) == target:
    #             res_list = [count, i]
    #             return res_list
    # checked = {}
    # i = 0
    # while target - nums[i] not in checked:
    #     checked[nums[i]] = i
    #     i += 1
    #
    # return [checked[target - nums[i]], i]

    # try:
    #     return max(sum(i) for i in nums if sum(i) == target)
    # except:
    #     return None


# xs = [7, 5, 4, 8, 7, 6, 9, 10, 12, 33, 14, 50, 2, 1, 3, 8]
# print(twoSum(xs, 83))


def arithmeticTriplets(nums, diff):
    ans = 0
    n = len(nums)
    for i in range(n):
        if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
            ans += 1

    return ans


nums =[4,5,6,7,8,9]
# print(arithmeticTriplets(nums, 2))


def distinctAverages(nums):
    res = {}
    for i in range(len(nums)//2):
        res[(max(nums) + min(nums))/2] = i
        nums.remove(max(nums))
        nums.remove(min(nums))
    return len(res)


nums = [4,1,4,0,3,5]

# print(distinctAverages(nums))


def distinctAverages1(nums):
    res = set()
    nums.sort()
    while len(nums) != 0:
        s = (nums.pop(0) + nums.pop(-1))/2
        res.add(s)
    return len(res)

nums1 = [4,1,4,0,3,5]

# print(distinctAverages1(nums1))


def romanToInt(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = [10000]
    i = 0
    for elem in s:
        if res[i] < roman[elem]:
            m = roman[elem] - res.pop()
            res.append(m)
        else:
            res.append(roman[elem])
            i += 1
    return sum(res)-10000


s = "MCMXCIV"

print(romanToInt(s))


def validateStackSequences(pushed, popped):
    stack = []
    res_list = []
    i = 0
    for elem in pushed:
        if elem == popped[i]:
            stack.append(elem)
            res = stack.pop()
            res_list.append(res)
            i += 1
            j = i
            try:
                while stack[-1] == popped[j]:
                    res = stack.pop()
                    res_list.append(res)
                    j += 1
            except IndexError:
                pass
        else:
            stack.append(elem)
    for j in range(len(stack)):
        res = stack.pop()
        res_list.append(res)
    print(popped, res_list)

    return True if popped == res_list else False


print(validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(validateStackSequences([2,1,0], [1,2,0]))
print(validateStackSequences([2,3,0,1],[0,3,2,1]))

result = []
maxcandies = max(candies)
    for i in range(len(candies)):
	    if candies[i]+extraCandies >= maxcandies:
		    result.append(True)
		else:
			result.append(False)
	return result