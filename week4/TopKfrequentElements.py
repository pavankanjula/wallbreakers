import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Time - O(nlogk)
        #Space - O(n)
        hashmap = collections.Counter(nums) #To count the frequencies
        freq_list = [] #To store the tuples of unique numbers and frequencies.
        for num, freq in hashmap.items():
            freq_list.append((freq, num))
        if len(freq_list) < k:
            return
        prior_list = [] # Minheap
        output = [] #Output
        size = 0
        for each in freq_list:
            if size < k: #until we reach a size of k, we construct a minheap
                heapq.heappush(prior_list, each)
                size += 1
            else:# if size reached to k, we update the heap such that k maximum frequencies exists in the heap.
                least = heapq.heappop(prior_list)
                if each[0] > least[0]:
                    heapq.heappush(prior_list, each)
                else:
                    heapq.heappush(prior_list, least)
        for each in prior_list:
            output.append(each[1])
        return output