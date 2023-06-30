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
        print(strs)
        for elem in strs:
            print(elem)
            count = -1
            while True:
                count += 1
                count_elem = len(min_elem) - count
                print(min_elem_copy, count_elem)
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
        print(strs)
        for elem in strs:
            if min_elem in elem:
                return list(min_elem)
            else:
                for i in len(min_elem):
                    count += 1
                    compare = min_elem[len(min_elem) - count]
                    if compare in elem:
                        return list(compare)