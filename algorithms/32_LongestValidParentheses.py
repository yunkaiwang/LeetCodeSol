class Solution:
    def longestValidParentheses(self, s):
        """
        Very interesting question, so I tried multiple ways to solve this problem, all of them are running in O(n) time (the easiest solution which is checking all possible substrings takes n^3 time, but that's too easy to be thought of and should not be taken into consideration of this question)
        1. Dynamic programming: initialize an array, where each index represents the longest valid parentheses ended at current position, for all positions where s[i] = "(", these indicies are all 0s. The intersting question now becomes where should be the entry when s[i] is ")", clearly there are two cases, when the first one is the character before it is "(", so these two will form a valid parentheses of length 2, but it might be directly after another valid parentheses, so we need to add the length of the valid parentheses ended at the character before it to the length. Case 2, previous character is not "(", this is the really interesting one to be thought about, if previous character is not "(", then how do we know if there exist a previous open bracket such that these two will form a valid parenthesis? I noticed that if there exist such open bracket, it's located at s[i-dp[i-1]-1], the reason is that if the character before is part of some valid parenthesis, then the last character that is not in the valid parenthesis is located at the index given, and we can check that index to see if we should include current close bracket or not. Here is the implementation of that solution, noticed that I added one more dummy entry in the DP array since I just don't want to avoid checking if i - 2 entry exist in DP array. Best runtime is 76ms, space complexity is O(n)
        """

        max = 0
        
        dp = [0] * (len(s) + 1)
        for i, c in enumerate(s):
            if i == 0:
                continue
            if c == ")":
                if i - dp[i] - 1 >= 0 and s[i - dp[i] - 1] == "(":
                    dp[i+1] = 2 + dp[i] + dp[i - dp[i] - 1]
                    if dp[i+1] > max:
                        max = dp[i+1]
        return max

        """
        2. Second solution uses a stack, which is always taken into consideration when we want to find out if some string is well-paired or not. To use a stack for this problem, we push the index of every open bracket to the stack, and we pop one entry, every time we meet a close bracket. Initially we push an dummy index -1 to the stack, if after we pop, the stack becomes empty, then we push current index to the stack. The reason is that if after we pop, the stack is empty, then we know that this close bracket has no corresponding open bracket for sure, therefore, we push the current index to the stack to represent the index before the next possible valid parenthesis can happen. It's hard to say more about this since it's a complicated step, but everything should become familiar if you actually run an example with the following code provided and you will see the reasoning behind. When we pop, we check the difference between the current index and the peek element of the stack, and that's the current length of the valid parenthesis. This approach also takes O(n) time and O(n) space. Best runtime is 72ms.
        """
        max = 0
        stack = [-1]
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    last_index = stack[-1]
                    if i - last_index > max:
                        max = i - last_index
        
        return max

        """
        3. Brilliant solution described in the solution using ONLY O(1) space and can still accomplish this job in O(n) time, code is listed below, basically it used two counters to keep track the number of open bracket and close bracket we have found when are going through the list forward and backward(I combined them so that I have four counters and one for loop, but it's the same thing). I will focus on proving that this approach is correct.
        Let i and j be the start and end indices of the longest valid parenthesis. First when we go forward, before i-th step, if left = right = 0, then the algorithm will correctly report the longest length. Notice that left and right cannot be both equal to something else other than 0 since otherwise we must have a even longer valid parenthesis which contradict our assumption. If this is not the case, then we can claim that left > right. Then when we go backwards, before we deal with j-th character, we must have left_rev <= right_rev, if they are both 0, then the algorithm must be correct, similarly they cannot both be something else as we can then find a longer valid parenthesis. We focus on the case when left_rev < right_rev, before we have left > right, notice that if these two are both true, then we must be able to find some longer valid parenthesis using characters to the left of i and characters to the right of j, which will contradict our assuemption, therefore, at least one of them is false, then our algorithm is correct.
        """

        max = 0
        left, right, left_rev, right_rev = 0, 0, 0, 0
        
        for i, c in enumerate(s):
            if c == "(":
                left += 1
            else:
                right += 1
                if right == left:
                    if left * 2 > max:
                        max = 2 * left
                elif right > left:
                    left = right = 0
            
            c_rev = s[len(s) - i - 1]
            if c_rev == "(":
                left_rev += 1
                if left_rev == right_rev:
                    if left_rev * 2 > max:
                        max = 2 * left_rev
                elif left_rev > right_rev:
                    left_rev = right_rev = 0
            else:
                right_rev += 1
        
        return max