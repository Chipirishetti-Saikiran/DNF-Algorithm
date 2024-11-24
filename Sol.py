def sortColors(nums):
        i,j,k=0,0,len(nums)-1 
        arr=nums
        while j<=k:
            if arr[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1 
            elif arr[j]==1:
                j+=1 
            else:
                arr[j],arr[k]=arr[k],arr[j]
                k-=1 
        return  arr   
nums = [2,0,2,1,1,0]
print(sortColors(nums))

        
