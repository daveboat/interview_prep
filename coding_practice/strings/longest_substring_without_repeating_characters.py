"""
LC3 - longest substring without repeating characters

Solution using a queue-ish solution, except I just use sliced strings. Go through string, appending characters until
you hit a character that's already in your string, throw away characters from the front of the string until you reach
the character.
"""


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) <= 1:
        return len(s)

    substring = ""

    max_len = 1

    for c in s:
        if c not in substring:
            substring += c
            if len(substring) > max_len:
                max_len = len(substring)
        else:
            substring = substring[substring.index(c) + 1:] + c

    return max_len


if __name__ == '__main__':
    print(lengthOfLongestSubstring("dvdf"))
    print(lengthOfLongestSubstring("pwwkew"))