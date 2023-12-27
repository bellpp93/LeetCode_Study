class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        num_dict = {}  # 딕셔너리 초기화

        # 리스트를 돌면서 현재 값과 목표 값과의 차(sub_dict)를 계산하여 딕셔너리에 저장
        for idx in range(len(nums)):
            num = nums[idx]
            sub_dict = target - num

            # 딕셔너리에 찾고자 하는 값(sub_dict)이 있는지 확인
            if sub_dict in num_dict:
                # 발견하면 해당 값의 인덱스와 현재 인덱스를 리턴시키고 종료
                return [num_dict[sub_dict], idx]
            
            # 현재 값을 딕셔너리에 저장(값과 인덱스를 저장)
            num_dict[num] = idx