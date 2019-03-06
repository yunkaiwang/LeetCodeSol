// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int l = 0, r = n;
        while (l <= r) {
            int mid = l + ((r-l)>>1);
            int res = guess(mid);
            if (res < 0) {
                r = mid - 1;
            } else if (res > 0) {
                l = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
};