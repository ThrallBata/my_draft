def addTwoNumbers(l1, l2):
    list_1 = l1[::-1]
    list_2 = l2[::-1]

    sum = int(''.join(str(i)for i in list_1))+int(''.join(str(i)for i in list_2))
    return list(str(sum))

print(addTwoNumbers([2, 4, 3], [5, 6, 4]))


class Solution:
    def longestCommonPrefix(self, strs):
        res_list = []
        min_elem = min(strs, key=len)
        min_elem_copy = min_elem
        strs.remove(min_elem)

        for elem in strs:

            count = -1
            while True:
                count += 1
                count_elem = len(min_elem) - count

                min_elem_copy = min_elem[:count_elem]
                if min_elem_copy in elem:
                    res_list.append(min_elem_copy)
                    break
        if strs != ['']:
            return min(res_list, key=len)


list22 = ["flower", "flow", "flight"]
list23 = ["dog","racecar","car"]
Igor = Solution()
print(Igor.longestCommonPrefix(list22))




list2 = ['flow', 'xyzq257772', 'abcefefe']
# print(min(list2, key=len))

if min(list2, key=len) in list2[1]:
    b = min(list2, key=len)
    # print(b[:4])

def longestCommonPrefix(self, strs):
        count = -1
        min_elem = min(strs, key=len)
        strs.remove(min_elem)
        for elem in strs:
            if min_elem in elem:
                return list(min_elem)
            else:
                for i in len(min_elem):
                    count += 1
                    compare = min_elem[len(min_elem) - count]
                    if compare in elem:
                        return list(compare)


def BinarySearch(nums, target):
    first = 0
    last = len(nums) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        res = mid #удалить
        if nums[mid] == target:
            index = mid
        else:
            if target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1#вернуть индекс и будет реальный бинарный поиск
    # if len(nums) >= 2:
    #     if target < nums[1] and target > nums[0]:
    #         return 1
    # if target <= nums[-1]:
    #     return res
    # else:
    #     return res + 1
    if nums[res] < target:
        return res +1
    else:
        return res



print(BinarySearch([1,2,4,6,7], 5))


def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        count_hay = 0
        for elem in haystack:
            if elem == needle[0]:
                count = count_hay + len(needle)
                if haystack[count_hay: count] == needle:
                    return count_hay
            count_hay += 1
    else:
        return -1


# print(strStr("sabutsad", "sad"))

list_12 = 'sabutsad'

# print(list_12[2:4])


def strStr1(haystack: str, needle: str) -> int:
    return haystack.find(needle)


# print(strStr1("sabutsad", "sad"))


def decodeMessage(key: str, message: str) -> str:
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    key_list = list(key)
    key_list_sort = sorted(set(key_list), key=lambda d: key_list.index(d))
    if ' ' in key_list_sort:
        key_list_sort.remove(' ')

    decode_dict = dict(zip(key_list_sort, alfabet))
    res_list = []
    for letter in message:
        if letter != ' ':
            res_list.append(decode_dict[letter])
        else:
            res_list.append(' ')
    return ''.join(res_list)



print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
print(decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))

# dsfgwg = "the quick brown fox jumps over the lazy dog"
# x = list(dsfgwg)
# y = sorted(set(x), key=lambda d: x.index(d))
# y.remove(' ')
# print(y)


def maxProfit(prices: list) -> int:
    profit = 0
    count = 1
    if len(prices) == 1:
        return 0
    for i in prices:
        max_profit_i = max(prices[count:]) - i
        if max_profit_i > profit:
            profit = max_profit_i
        if count == (len(prices)-1):
            break
        count += 1
    return profit if profit > 0 else 0

def maxProfit2(prices: list) -> int:
    profit = 0
    count = 1
    if 0 in prices:
        prices = [i for i in prices if i != 0]
        print(prices)
    if len(prices) == 1:
        return 0
    max_elem = max(prices[count:])
    for i in prices:
        if max_elem == i:
            max_elem = max(prices[count:])
        max_profit_i = max_elem - i
        if max_profit_i > profit:
            profit = max_profit_i
        if count == (len(prices)-1):
            break
        count += 1
    return profit if profit > 0 else 0

print(maxProfit2([7,1,5,3,6,4,0, 0, 0, 0 ]))

# def maxProfit1(prices: list) -> int:
#     buy, sell, maxx = prices[0], 0, 0
#     for cur in prices:
#         buy = min(buy, cur)
#         sell = cur - buy
#             maxx = max(sell, maxx)
#         return maxx


# print(maxProfit1([7,1,5,3,6,4,0, 0, 0, 0 ]), 'anih')



def singleNumber(nums):
    trio = []
    nums1 = nums.copy()
    for i in nums:
        (nums1.remove(i))
        if i in nums1:
            trio.append(i)

        elif i not in trio:
            return i



nums = [2,2,3,2]
print(singleNumber(nums))


def longestSubarray1(nums: int) -> int:
    nums = [i for i in nums if i != 0]
    nums.pop()
    return nums


# print(longestSubarray1([1,1,1,1,1,0,1,0,1,1,1,0,0,1,0]))


def longestSubarray(nums: int) -> int:
    max_s = []
    count_zero = 0
    count = 0
    count_1 = 0
    count_zero_1 = 0
    elem_past = any
    for elem in nums:
        if elem == 1 and count_zero <= 1:
            count += 1
            if count_zero == 1 or count_zero_1 == 1:
                count_1 += 1
        elif count_zero < 1 and elem == 0 and count != 0:
            count_zero += 1
            max_s.append(count_1)
            count_1 = 0
            count_zero_1 = 0
        elif elem == 0 and count != 0 and count_zero == 1:
            max_s.append(count)
            count = 0
            count_zero = 0
            count_zero_1 = 1
        elif elem == 0 and elem_past == 0 and count_1 != 0:
            max_s.append(count_1)
            count_1 = 0
        elem_past = elem
    max_s.append(count)
    max_s.append(count_1)
    return max(max_s) if 0 in nums else max(max_s) - 1


print(longestSubarray([1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1]))
nums = [2,2,3,2]
nums.insert(1, 65)
print(nums)


def isHappy1(n: int) -> bool:
    try:
        sum_squares = 0
        for elem in str(n):
            sum_squares += int(elem) ** 2
            print(sum_squares)
        if sum_squares == 1:
            return True
        if sum_squares != 1:
            return isHappy1(sum_squares)
    except RecursionError:
        return False


print(isHappy1(21))


def isHappy(n: int) -> bool:
    count = 0
    def sum_squares_number(n:int, count):
        sum_squares = 0
        for elem in str(n):
            sum_squares += int(elem) ** 2
            print(sum_squares)
        if sum_squares == 1:
            return True
        if sum_squares != 1 and count <= 100:
            count += 1
            return sum_squares_number(sum_squares, count)
        else:
            return False

    return sum_squares_number(n, count)



# print(isHappy(19))


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for idx in set(s):
        if s.count(idx) != t.count(idx):
            return False
    return True


print(isAnagram('awfwfwfwf', 'awfwfwfwf'))



# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        ...







[3, 9, 20, None, None, 15, 7]
[1,None,2,3]


def sfsdgsdg(nums, val):
    res = [i for i in nums if i != val]
    return len(res)

print(sfsdgsdg([3,2,2,3], 3))

INPUT = [1, 2, 5, 12, 3, 5, 2, 7, 12]


def isPalindrome(x: int):
    inv_list = []
    for elem in str(x):
        if elem != '-':
            inv_list.insert(0, elem)
    if int(''.join(inv_list)) == x:
        return True
    return False


print(isPalindrome(-12211))





