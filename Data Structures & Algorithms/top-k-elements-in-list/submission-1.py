class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
        
        heap = []
        for key,value in hm.items():
            heapq.heappush(heap,tuple([value,key]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        

        
        