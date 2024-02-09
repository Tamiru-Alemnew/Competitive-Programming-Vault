class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indices_dict = defaultdict(list)
        for index, num in enumerate(nums):
            indices_dict[num].append(index)
      
      
        distances = [0] * len(nums)
      
        for indices in indices_dict.values():
            left_distance = 0
            right_distance = sum(indices) - len(indices) * indices[0]

            for idx_position in range(len(indices)):
                distances[indices[idx_position]] = left_distance + right_distance
              
                if idx_position + 1 < len(indices):
                    gap = indices[idx_position + 1] - indices[idx_position]
                    left_distance += gap * (idx_position + 1)
                    right_distance -= gap * (len(indices) - idx_position - 1)
      
        return distances