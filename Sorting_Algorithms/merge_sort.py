# # def mergesort(cs):
# #     if len(cs)>1:
# #         mid = len(cs)//2
# #         lefthalf = cs[:mid]
# #         righthalf = cs[mid:]

# #         mergesort(lefthalf)
# #         mergesort(righthalf)

# #         i=j=k=0
# #         while i<len(lefthalf) and j<len(righthalf):
# #             if lefthalf[i]<righthalf[j]:
# #                 cs[k] = lefthalf[i]
# #                 i+=1
# #             else:
# #                 cs[k] = righthalf[j]
# #                 j+=1
# #             k+=1
        
# #         while i<len(lefthalf):
# #             cs[k] = lefthalf[i]
# #             i+=1
# #             k+=1

# #         while j<len(righthalf):
# #             cs[k] = righthalf[j]
# #             j+=1
# #             k+=1
# #     return cs

# # l1 = [9,5,3,73,0,4,85,6,2]
# # print(mergesort(l1))

# # def partition(cs,startIdx,endIdx):
# #     pivot = startIdx
# #     start = startIdx
# #     end = endIdx

# #     while start < end:
# #         while len(cs)>start and cs[start] <= cs[pivot]:
# #             start+=1
# #         while cs[end] > cs[pivot]:
# #             end-=1
        
# #         if start < end:
# #             cs[start],cs[end] = cs[end],cs[start]
# #     cs[pivot],cs[end] = cs[end],cs[pivot]
# #     return end

# # def quickshort(cs,start,end):
# #     if start < end:
# #         pIdx = partition(cs,start,end)
# #         quickshort(cs,start,pIdx-1)
# #         quickshort(cs,pIdx+1,end)

# # l1 = [11,9,29,7,21,5,28]
# # print(quickshort(l1,0,len(l1)-1))
# # print(l1)

# # d1 = {1:23,2:53,3:51,4:74}
# # for i in list(d1):
# #     d1[i+2] = d1.pop(i)

# # print(d1)

# class Solution(object):
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         if len(nums)>1:
#             mid = len(nums)//2
#             lh = nums[:mid]
#             rh = nums[mid:]

#             self.sortColors(lh)
#             self.sortColors(rh)

#             i=j=k=0
#             while i<len(lh) and j<len(rh):
#                 if lh[i]<rh[j]:
#                     nums[k]=lh[i]
#                     i+=1
#                 else:
#                     nums[k]=rh[j]
#                     j+=1
#                 k+=1

#             while i<len(lh):
#                 nums[k]=lh[i]
#                 i+=1
#                 k+=1
            
#             while j<len(rh):
#                 nums[k]=rh[j]
#                 j+=1
#                 k+=1
#         return nums

# n = [2,0,2,1,1,0]
# jd = Solution()
# print(jd.sortColors(n))

n = 19
n = str(n)
c = 0
for i in n:
    c+=int(i)*int(i)
    print(i)

print(c)
