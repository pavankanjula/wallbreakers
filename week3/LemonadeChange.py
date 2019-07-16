class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change5 = 0 #Tracks number of 5$ bills available
        change10 = 0 #Tracks number of 10$ bills available
        #3 cases in total
        for bill in bills:
            if bill == 5: #case 1 -  5$
                change5 += 1
            elif bill == 10: #case2 - 10$
                change10 += 1# add 1 10$ bill to counter 10
                if change5 >= 1:
                    change5 -= 1 # substract 1 5$ bill from counter 5
                else:
                    return False
            else: #case3 - 20$
                if change10 >= 1 and change5 >= 1:
                #if any 10$ bills are present, give it first and then a 5$ bill(GREEDY PART)
                    change10 -= 1
                    change5 -= 1
                elif change10 < 1 and change5 >= 3:
                #if only 10$ bills are not present and more than 3 5$ bills are there, give 3 5$ bills.
                    change5 -= 3
                else:
                    return False
        return True