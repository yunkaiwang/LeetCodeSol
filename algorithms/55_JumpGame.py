class Solution:
    def canJump(self, nums):
        """
        O(n) solution using O(1) space, idea is remember the
        furthest position you can get and if you reached there
        and the destination is still not reachable, then return
        false, if at any position you find that the destination is
        reachable, then you return true. This is much simpler than
        the Jump Game 2 question, they should swap the order of
        these two questions.
        """
        target = len(nums) - 1
        c_r, i = nums[0], 1
        if c_r >= target:
            return True
        while i <= c_r:
            sum = nums[i] + i
            if sum > c_r:
                if sum >= target:
                    return True
                else:
                    c_r = sum
            i += 1
        return False