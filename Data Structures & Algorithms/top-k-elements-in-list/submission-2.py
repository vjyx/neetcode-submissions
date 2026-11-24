class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        boxes = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            boxes[cnt].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            if boxes[i] != []:
                res.extend(boxes[i])
            if len(res) == k:
                return res