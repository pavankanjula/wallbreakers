import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        #Time - worstcase(nlogn) to sort the frequncies when there is no repetitions in characters.
        #Space - O(n) To store the multisets and list of frequencies.
        multiset = collections.Counter(s) # multiset with no. of occurances of characters.
        freq_to_key = {} #hashmap stores frequencies as keys and list of characters with that frequency as values.
        freq_list = [] # List of all frequencies.
        for key,value in multiset.items():
            if value in freq_to_key:
                freq_to_key[value].append(key)
            else:
                freq_to_key[value] = [key]
        for key in freq_to_key.keys():
            freq_list.append(key)
        freq_list.sort(reverse = True) #Sorts the frequencies in reverse order.
        output = "" #output string
        for freq in freq_list:
            for char in freq_to_key[freq]:
                output += char*freq #for each frequeny, we check in freq_to_key multiset and appends the chars multiplied by frequency.
        return output