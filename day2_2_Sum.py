#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

if __name__ == '__main__':
    N = int(input("Enter lenght array : "))
    nums= []

    print("Enter value :")
    for i in range(N):
        nums.append(input().strip())#thêm giá trị vào mảng
        
    target =int(input("Enter integer target :"))
    
    for i in range(len(nums)): #chạy từ 0 đến len(nums)-1
        for j in range(i+1,len(nums)):
            if int(nums[i]) +int(nums[j]) ==target :
                print ([i,j])
       
      
        
