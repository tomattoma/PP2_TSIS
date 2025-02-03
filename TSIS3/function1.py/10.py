def unique(nums):
    unique_nums = []
    
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
        
    return unique_nums


nums = list(map(int, input().split()))
print(unique(nums))