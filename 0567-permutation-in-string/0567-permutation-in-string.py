class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hashmap count s1, sliding window to see if we can find substring of len(s1) with matching counts in s2

        # count letter occurrences in s1
        count_s1 = {}
        for c in s1:
            count_s1[c] = count_s1.get(c, 0) + 1

        count_s2 = {} # to count letter occurrences in sliding window substring
        left, right = 0, 0
        while right < len(s2):

            # decrement/remove counter for letter if needed
            win_len = right - left + 1
            if win_len > len(s1): # start shrinking window from left
                count_s2[s2[left]] -= 1
                if count_s2[s2[left]] == 0: # so it'll match count_s1
                    del count_s2[s2[left]]
                left += 1

            # increment/add counter for letter
            count_s2[s2[right]] = count_s2.get(s2[right], 0) + 1

            # we found a permutation of s1, very epic
            if count_s1 == count_s2:
                return True

            right += 1

        return False