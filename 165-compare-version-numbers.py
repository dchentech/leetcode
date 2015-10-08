"""
Question:
    Compare Version Numbers

    Compare two version numbers version1 and version2.

    If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

    You may assume that the version strings are non-empty and contain only digits and the . character.
    The . character does not represent a decimal point and is used to separate number sequences.
    For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

    Here is an example of version numbers ordering:

    0.1 < 1.1 < 1.2 < 13.37

    Credits:
    Special thanks to @ts for adding this problem and creating all test cases.

Performance:
    1. Total Accepted: 34390 Total Submissions: 219694 Difficulty: Easy
    2. Your runtime beats 87.74% of python submissions.
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        class VersionNumber(object):
            def __init__(self, version_number):
                self.version_number = version_number
                self.sorted_nums = map(int, version_number.split("."))

                # fix the end is zero
                while len(self.sorted_nums) > 0 and self.sorted_nums[-1] == 0:
                    self.sorted_nums.pop()

            def __cmp__(self, another):
                assert isinstance(another, VersionNumber), another
                min_count = min(map(len, [self, another]))

                # 1. compare the same length
                curr_idx = 0
                while curr_idx < min_count:
                    if self.sorted_nums[curr_idx] < another.sorted_nums[curr_idx]:
                        return -1
                    if self.sorted_nums[curr_idx] > another.sorted_nums[curr_idx]:
                        return 1
                    curr_idx += 1

                # 2. compare the over length
                if len(self) < len(another):
                    return -1
                if len(self) > len(another):
                    return 1
                return 0

            def __len__(self):
                return len(self.sorted_nums)

        return cmp(VersionNumber(version1), VersionNumber(version2))


assert Solution().compareVersion("0.1", "1.1") is -1
assert Solution().compareVersion("1.1", "1.2") is -1
assert Solution().compareVersion("1.2", "13.37") is -1
assert Solution().compareVersion("0.1", "13.37") is -1
assert Solution().compareVersion("0.1.1", "13.37") is -1

assert Solution().compareVersion("13.37", "1.1") is 1
assert Solution().compareVersion("13.37", "13.36") is 1
assert Solution().compareVersion("13.37", "13") is 1

assert Solution().compareVersion("0", "0") is 0
assert Solution().compareVersion("1.1", "1.1") is 0
assert Solution().compareVersion("1.1.1", "1.1.1") is 0
assert Solution().compareVersion("1.0", "1") is 0
