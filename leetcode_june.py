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


print(strStr("sabutsad", "sad"))

list_12 = 'sabutsad'

print(list_12[2:4])


def strStr1(haystack: str, needle: str) -> int:
    return haystack.find(needle)


print(strStr1("sabutsad", "sad"))