#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#prints the max subaary like in this eg. it prints [4,-1,2,1].
def maxsub(nums):
        add = [None] * len(nums)
        flag=0
        new=[]
        add[0]=nums[0]
        #for creating the subarray of additions
        for i in range(1,len(nums)):
            check = add[i-1]+nums[i]
            if check > 0 and check > nums[i]:
                add[i]=check
            else:
                add[i]=nums[i]
        start = add.index(max(add))
        #finding out the max subarray in list
        for i in range(start,-1,-1):
            if add[i] >=0 :
                flag =flag+1
            else:
                break
        #printing the value
        while(flag!=0):
            new.append(nums[start])
            start=start-1
            flag=flag-1
        add.clear()
        new.reverse()
        print(new)
            
l=[-2,1,-3,4,-1,2,1,-5,4]
maxsub(l)

