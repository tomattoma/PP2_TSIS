def histogram(nums):
    for x in nums:
        res = ""
        for y in range(0,x):
            res+="*"
        print(res)


mylist = list(map(int, input().split()))
histogram(mylist)