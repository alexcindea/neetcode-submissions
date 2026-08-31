class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front_pointer = 0
        end_pointer = len(numbers) - 1
        
        while front_pointer < end_pointer: 
            if numbers[front_pointer] + numbers[end_pointer] > target:
                end_pointer -= 1
            if numbers[front_pointer] + numbers[end_pointer] < target:
                front_pointer += 1
            if numbers[front_pointer] + numbers[end_pointer] == target:
                return [front_pointer + 1, end_pointer + 1]

            
            
        