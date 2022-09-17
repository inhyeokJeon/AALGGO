from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        res = left = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            most_char = counter.most_common()[0][1]
            while right + 1 - left - most_char > k:
                counter[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
            # print(right)

s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
k = 4
sol = Solution()

print(sol.characterReplacement(s, k))



























