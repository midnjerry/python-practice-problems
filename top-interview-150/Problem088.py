# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
class Problem088:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        The challenge with this solution is to reuse nums1 in lieu of using a new array.
        To circumvent the problem of overwriting data, the trick is to merge arrays from
        last element going to first element.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1
        while(j >= 0):
            if (nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i=i-1
            else:
                nums1[k] = nums2[j]
                j=j-1
            k -= 1

if __name__ == '__main__':
    solution = Problem088()
    nums1 = [1,2,3,0,0,0]
    nums2 = [2, 5, 6]
    solution.merge(nums1, 3, nums2, 3)
    print(f'Expected Result: [1, 2, 2, 3, 5, 6]')
    print(f'Result: {nums1}')

    nums1 = [1]
    solution.merge(nums1, 1, [], 0)
    print(f'Expected Result: [1]')
    print(f'Result: {nums1}')

    nums1 = [0]
    solution.merge(nums1, 0, [1], 1)
    print(f'Expected Result: [1]')
    print(f'Result: {nums1}')