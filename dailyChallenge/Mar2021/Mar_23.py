"""
3Sum With Multiplicity

Simple solution based on the idea of 3 sum
"""
import collections
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        num_map = collections.Counter(arr)

        dis_num = list(num_map.keys())
        dis_num.sort()

        num_sol = 0
        for i, num in enumerate(dis_num):
            j, k = i, len(dis_num) - 1
            t = target - num
            while j <= k:
                if dis_num[j] + dis_num[k] < t:
                    j += 1
                elif dis_num[j] + dis_num[k] > t:
                    k -= 1
                else:
                    print(i, j, k, num, dis_num[j], dis_num[k])
                    if i < j < k:
                        num_sol += num_map[num] * num_map[dis_num[j]] * num_map[dis_num[k]]
                    elif i == j < k:
                        num_sol += (num_map[num] * (num_map[num] - 1)) // 2 * num_map[dis_num[k]]
                    elif i < j == k:
                        num_sol += (num_map[dis_num[k]] * (num_map[dis_num[k]] - 1)) // 2 * num_map[num]
                    else:
                        num_sol += (num_map[dis_num[k]] * (num_map[dis_num[k]] - 1) * (num_map[dis_num[k]] - 2)) // 6
                    j += 1
                    k -= 1
        return num_sol % (10 ** 9 + 7)
