# def func_polindrom(string: list[str]) -> int:
#     d = {}
#     count = 0
#     for j in string:
#         if string.count(j) > 1:
#             count += string.count(j)
#             d[j] = count
#             count = 0
#         if string.count(j) <= 1:
#             count += string.count(j)
#             d[j] = count
#             count = 0
#     print(d)




# func_polindrom(["ab", "ty", "yt", "lc", "cl"])
# from collections import defaultdict
# def longestPalindrom(words: list[str]) -> int:
#
#     m = defaultdict(int)
#     unpaired = ans = 0
#
#     for w in words:
#         if w[0] == w[1]:
#
#             if m[w] > 0:
#                 unpaired -= 1
#                 m[w] -= 1
#                 ans += 4
#             else:
#                 m[w] += 1
#                 unpaired += 1
#         else:
#             if m[w[::-1]] > 0:
#                 ans += 4
#                 m[w[::-1]] -= 1
#             else:
#                 m[w] += 1
#     if unpaired > 0: ans += 2
#     return ans
#
# print(longestPalindrom(["ab","ty","yt","lc","cl","ab"]))


def isValid(s):
    opening = []
    closing = []
    for i in range(len(s)):
        if s[i] in ['(', '[', '{']:
            opening.append(s[i])
        if s[i] in [')', ']', '}']:
            closing.append(s[i])
    if len(opening) == len(closing):
        return True
    return False


print(isValid(['(', '[', '{', '}', ']', ')']))

