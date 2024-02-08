def spy_game(nums):
    for i in nums:
        if nums[i]==0 and nums[i+1] == 0 and nums[i+2] ==7:
            return True 
        return False 
