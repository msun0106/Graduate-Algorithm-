# O(n^2)
""" sum(num[i:j])=sum(num[i:j-1])+num[j], thus it's O(n^2)"""
def Max_subarray_square(data):
    n=len(data)
    max_so_far=0

    for i in range(n):
        sum=0
        for j in range(i, n):
            sum=sum+data[j]
            max_so_far=max(sum,max_so_far)
    return max_so_far

# DP solution O(n)
""" sum[0:i] either include data[i] or not,"""
""" when know sum[0:i-1], let max_ending_here= max sum when include data[i], """
""" so, the max_end_here either is itself data[i] or data[i]+sum[0:i-1],"""
""" and the result max_so_far is max(data[i], max_end_here[i-1]+data[i])"""
def Max_subarray_DP(data):
    n=len(data)
    max_end_here=[0 for i in range(n)]
    for i in range(1,n):
        max_end_here[i]=max(max_end_here[i-1]+data[i],data[i])
    return max(max_end_here)

# Divide and Conquer O(nlogn)
""" divide the array into right and left side, and recursively solve the problem
the maxsubarray either in left side, right side or part left and right plus the middle one"""
def Max_subarray_DC(data,start,end):
    if start>end:
        return 0
    if start==end:
        return (0,data)
    mid=(start+end)/2
    leftMaxArray=Max_subarray_DC(data,start,mid)
    rightMaxArray=Max_subarray_DC(data,mid+1,end)
    



if __name__=='__main__':
    data=[9,-1,3,4,5,-7]
    print Max_subarray_square(data)
    print Max_subarray_DP(data)
    print Max_subarray_DC(data,0,len(data)-1)
