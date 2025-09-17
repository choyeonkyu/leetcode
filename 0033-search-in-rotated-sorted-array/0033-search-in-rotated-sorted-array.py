class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        answer = len(nums)
        # rotate 된 지점의 index를 먼저 찾음
        # 정렬된 상태에서 target의 index를 찾음
        # 그 후에 
        rotated_index, sorted_target_index = 0, 0
        demo_nums = list(nums)
        if len(nums) <= 2:
            if target in nums:
                print(nums.index(target))
                return nums.index(target)
            else:
                return -1
        while len(demo_nums) > 2:
            print(demo_nums)
            if demo_nums[mid] > demo_nums[right]: # [2,4,5,6,7,0,1], [5,6,7,0,1,2,4]
                demo_nums = demo_nums[mid:]
                rotated_index += mid
                right = len(demo_nums) -1
                mid = (left + right) // 2
            else:
                demo_nums = demo_nums[:mid+1]
                right = len(demo_nums) -1
                mid = (left + right) // 2
                print(demo_nums)
        if len(demo_nums) == 1:
            print(rotated_index)
        elif demo_nums[0] > demo_nums[1]:
            rotated_index += 1
            print(rotated_index)
        else:
            print(rotated_index)
        sorted_nums = nums[rotated_index:] + nums[:rotated_index] if rotated_index > 0 else nums
        print(sorted_nums)
        left = 0
        right = len(sorted_nums) - 1
        mid = (left + right) // 2
        while len(sorted_nums) > 2:
            if target == sorted_nums[mid]:
                return (rotated_index + mid + sorted_target_index) % answer
            elif target < sorted_nums[mid]:
                sorted_nums = sorted_nums[:mid]
                right = len(sorted_nums) - 1
                mid = (left + right) // 2
            else:
                sorted_nums = sorted_nums[mid:]
                sorted_target_index += mid
                right = len(sorted_nums) - 1
                mid = (left + right) // 2
            print(sorted_target_index, sorted_nums)
        if target in sorted_nums:
            print((rotated_index + sorted_target_index + sorted_nums.index(target)) % answer)
            return (rotated_index + sorted_target_index + sorted_nums.index(target)) % answer
        else:
            return -1