def chek(nums):
    digit = [0,0,7]

    for num in nums:
        if num == digit[0]:
            digit.pop(0)
        if not digit:
            return True
    return False


mynums = list(map(int, input().split()))
print(chek(mynums))