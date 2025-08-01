# Sorted-Names


![Sorting-Algorithms.png](https://www.crio.do/blog/content/images/2022/02/Sorting-Algorithms.png)
# Solution for leetcode  problem 2418. Implementing Sorting a list

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

# Solution 
 * combining the names with heights, with the height first as that is  what we will be 
        sorting by. sort the list by height in descending order: reverse=True. Return just the 
        sorted names without the heights
   - create an empty list to hole the height and names
   - loop through the indexes and create pairs of heights and names. Height being first as this what we want to sort by
   - sort the pairs by the height in descending order
   - create an empty list to store only the names of the sorted list
   - get the name from the height
   - return just the name from the sorted list
