class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Time - O(n)
        # Space - O(n)
        output = []
        for elem in range(1,n+1):
            if elem % 3 == 0 and elem % 5 == 0:
                output.append('FizzBuzz')
            elif elem % 3 == 0:
                output.append('Fizz')
            elif elem % 5 == 0:
                output.append('Buzz')
            else:
                output.append(str(elem))
        return output