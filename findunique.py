import copy
class Solution:
    def findunique(self,arr):
        result ={}
        i=0
        while i<len(arr):
            if arr[i] in result:
                result[arr[i]]+=1
            else:
                result[arr[i]]=1
            i+=1
        return [x for x in result if result[x]==1]
    def findunique2(self,arr):
        result ={}
        for i in range(len(arr)):
            if arr[i] in result:
                result[arr[i]]+=1
            else:
                result[arr[i]]=1
        return [x for x in result if result[x]==1]
    
    def findunique3(self,arr): 
        return [x for x in arr if arr.count(x)==1]


input=[1,3,4,5,6,7,2,4,6,1,6,7]

# s = Solution().findunique(input)
# print(input,s)

# s2 = Solution().findunique2(input)
# print(input,s2)

s3= Solution().findunique3(input)
print(input,s3)