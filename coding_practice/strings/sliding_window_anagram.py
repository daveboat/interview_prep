from collections import Counter


def make_dict(s):
    d = {c: 0 for c in
         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']}
    for c in s:
        d[c] += 1
    return d


def findAnagrams(s, p):
    """
    - create S and P histograms only once
    - use a sliding window approach to change the histogram for s instead of recreating it every time
    """
    if len(s) < len(p):
        return []

    l = len(p)

    p_hist = make_dict(p)
    s_hist = make_dict(s[0:0 + l])
    out_list = []
    if p_hist == s_hist:
        out_list.append(0)
    for i in range(1, len(s) - l + 1):
        s_hist[s[i - 1]] -= 1
        s_hist[s[i + l - 1]] += 1
        if p_hist == s_hist:
            out_list.append(i)

    return out_list


if __name__ == '__main__':
    # sliding window anagram: eg. s_test = acb, s = abcdefgjiebca, return a list of starting indices where an anagram of
    # s_test can be found in s

    s = 'abcdefgjiebca'
    s_test = 'acb'

    print(findAnagrams(s, s_test))