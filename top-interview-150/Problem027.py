# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

class Problem027:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        length = len(nums)
        for i in range(0, length):
            if (nums[i] == val):
                k += 1                
                nums[i] = nums[length-k]
        return k
        

if __name__ == '__main__':
    solution = Problem027()
    nums = [3,2,2,3]
    print(f'Result (expected k=2): {solution.removeElement(nums,3)}')
    print(f'nums (expected = [2, 2, *, *]): {nums}')
    