class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        #Time - O(right - left)
        #Space - O(1)
        output = []
        for num in range(left, right+1):
        #Looping through all the numbers between the given bounds, set a varaible accept to True.
            accept = True
        # Loop through all the digits and if any rule is violated, change accept to False and break the loop.
            for digit in str(num):
                if int(digit) == 0 or num % int(digit) != 0:
                    accept = False
                    break
            # if accept is not False, we will append that number to the output list.
            if accept:
                output.append(num)
        return output