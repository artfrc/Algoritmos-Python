class Solution(object):
  
    def maximumCount(self, nums):
      
        index_zero = self.find_index_element_zero(nums) #achar o index do elemento zero
        pos = 0
        neg = 0
        
        if index_zero != -1: # encontrei o zero

            aux = index_zero
            while aux >= 0 and nums[aux] == 0:
                aux -= 1
            
            if aux >= 0:
                neg = aux + 1  

            aux = index_zero
            while aux <= (len(nums) - 1) and nums[aux] == 0:
                aux += 1
            
            if aux <= len(nums) - 1:
                pos = len(nums) - aux  # Quantidade de números positivos
        
        else: # Se não há zeros, contar os negativos e positivos diretamente
            
            neg = len([x for x in nums if x < 0])
            pos = len([x for x in nums if x > 0])
        
        return max(pos, neg)

    def find_index_element_zero(self, nums):
        left = 0
        right = len(nums) - 1
        target = 0

        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1