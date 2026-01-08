# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:

        # sort the array on the basis of the second element

        intervals.sort(key = lambda x: x[1])

        n = len(intervals)

        prev = 0
        count = 1

        for i in range(1, n) :
            
            if intervals[i][0] >= intervals[prev][1] :
                count += 1
                prev = i
        
        return n - count

nums = [[1,2],[2,3],[3,4],[1,3]]

sol = Solution()
ans = sol.eraseOverlapIntervals(nums)
print(ans)



# Two intervals overlap if their time ranges intersect.

# Goal:
# Remove the minimum number of intervals so that no intervals overlap.



# Key Idea

# Instead of thinking:
# “Which intervals should I remove?”

# We think:
# “How many intervals can I keep without overlapping?”

# Because:
# Intervals Removed = Total Intervals − Max Non-Overlapping Intervals



# Greedy Strategy

# Why Greedy?
# To maximize non-overlapping intervals,
# we should always pick the interval that finishes the earliest.

# Why?
# Because:
# If we pick an interval that ends early,
# We leave more room for future intervals,
# So we can fit more intervals.
# This is a classic greedy idea.



# n = len(intervals)
# prev = 0
# count = 1
# Meaning:

# prev → index of last selected interval

# count → how many intervals we have chosen so far

# We always select the first interval after sorting
# So [1,2] is chosen first.



# Loop Through Intervals

# We now check remaining intervals and see if they overlap.

# ▶️ i = 1

# Interval:

# [2,3]


# Compare:

# start of current  (2)
# >= end of prev    (2)


# Condition:

# if intervals[i][0] >= intervals[prev][1]:


# Here:

# 2 >= 2  ✅ no overlap


# So we KEEP it.

# Update:

# count = 2
# prev = 1

# ▶️ i = 2

# Interval:

# [1,3]


# Compare:

# start = 1
# end of prev = 3


# Check:

# 1 >= 3 ❌ false → overlap detected


# So we do NOT take this interval.
# We simply ignore it.

# count stays 2.

# ▶️ i = 3

# Interval:

# [3,4]


# Compare:

# start = 3
# prev end = 3


# Condition:

# 3 >= 3  ✅ no overlap


# So keep it.

# Update:

# count = 3
# prev = 3