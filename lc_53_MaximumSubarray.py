


test = {
    'input':{
        'nums':[-2,1,-3,4,-1,2,1,-5,4]
    },
    'output':6
    
}


def maxSubArray(nums: int) -> int:

    #step 1 start sum from left, put it in sum_so_far, initialize max_so_far 
    # step 2 keep on adding if next number increases value of sum_so_far
    # step 3 replace  max(max_so_far , sum_so_far) each step
    # re-initialize current_so_far if it goes below 0

    sum_so_far=0
    max_so_far = nums[0]


    for i in nums:
        if sum_so_far<0:
            sum_so_far=0
        sum_so_far+=i
        max_so_far=max(max_so_far,sum_so_far)
    print(max_so_far)
    return max_so_far


print(maxSubArray(**test['input'])==test['output'])