class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Time - O(n)
        #Space - O(n)
        #Loop through the list from backside and add one like we do by hand.
        if len(digits) == 0:
            return [1]
        digits[-1] += 1 #add 1 to the last element.
        for i in range(len(digits)-2, -1, -1):
            if digits[i+1] > 9: #if we get gretaer than 9 anywhere we carry 1 to left and keep remaining.
                digits[i+1] -= 10
                digits[i] += 1
        if digits[0] > 9:
            digits[0] -= 10
            digits.insert(0,1)
        return digits