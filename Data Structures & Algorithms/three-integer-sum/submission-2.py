class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set([])
        for i in range(0, len(nums) - 2):
            
            front_ptr = i + 1
            end_ptr = len(nums) - 1

            while front_ptr < end_ptr:
               
                if nums[front_ptr] + nums[end_ptr] + nums[i] == 0:
                    triplets.add(tuple([nums[i], nums[front_ptr], nums[end_ptr]]))
                    front_ptr += 1
                elif nums[front_ptr] + nums[end_ptr] > 0 - nums[i]:
                    end_ptr -= 1
                elif nums[front_ptr] + nums[end_ptr] < 0 - nums[i]:
                    front_ptr += 1
                
            
        return list(triplets)
                


        