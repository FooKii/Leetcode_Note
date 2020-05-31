class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # slide window
        # a b c a b c b b
# index   0 1 2 3 4 5 6 7
# left    0 0 0 1 2 3 5 7
# window  1 2 3 3 3 4 2 1
        left_index = 0
        max_len = 0 # init as 0 due to empty input ("")
        found_dict = {}
        for ind, char in enumerate(s):
            tmp = found_dict.get(char, 0)
            if tmp > left_index:
                left_index = tmp
            found_dict[char] = ind + 1
            length = ind - left_index + 1 
            if length > max_len:
                max_len = length
        return max_len
        