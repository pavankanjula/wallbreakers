class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time - O(n)
        # Space - O(n)
        hashmap = {}  # stores the next greater element if it has one
        stack = []  # To store the number for which we didn't find a next greater element till now
        for elem in nums2:  # Loop through the list nums2
            if len(stack) == 0:  # add to stack if stack is empty
                stack.append(elem)
            else:  # if not empty, check if it is greater then elements in the stack and store in hashmap.
                while elem > stack[-1]:
                    hashmap[stack.pop()] = elem
                    if len(stack) == 0 or elem <= stack[-1]:
                        break
                stack.append(elem)
        output = []
        for num in nums1:  # Finally we can loop through nums1 list and check in hashmap if not found put -1 else the value.
            if num in hashmap:
                output.append(hashmap[num])
            else:
                output.append(-1)

        return output