# python-leetcode-problems

## When to Use a Hashmap in LeetCode Problems

When solving problems on LeetCode, identifying the right data structure is key to crafting an efficient solution. Hashmaps, known for their fast lookups, are often a go-to choice under certain conditions. Here are some indicators that suggest a hashmap might be the right tool for the job:

### 1. Need for Fast Lookups

If the problem involves frequent searches or lookups, especially to check if an item exists, a hashmap can provide constant time complexity for these operations.

### 2. Counting Elements

For problems that require counting occurrences of elements or tracking the frequency of items, hashmaps allow you to maintain a count for each unique element efficiently.

### 3. Finding Complements or Pairs

In scenarios where you need to find pairs that satisfy a certain condition (like the "Two Sum" problem), hashmaps can store elements in a way that complements can be easily searched.

### 4. Need for Mapping Relationships

Whenever there's a need to map a unique key to a specific value, or to maintain a relationship between pairs of data, hashmaps are a natural choice.

### 5. Subarray or Substring Problems

Problems involving subarrays or substrings with certain conditions (e.g., unique characters or a specific sum) can benefit from hashmaps to track elements within the current window of consideration.

### 6. Space for Time Trade-off

If a problem suggests that trading extra space for time could lead to a more efficient solution, consider using a hashmap. This is often the case in optimization problems where reducing time complexity is a priority.

### 7. Grouping or Categorizing Data

When you need to group or categorize data based on certain attributes or conditions, hashmaps can efficiently support these operations by using keys as categories and values as lists or sets of items belonging to those categories.

Recognizing these patterns will help you quickly determine when a hashmap is a suitable data structure for solving a given problem on LeetCode or similar platforms.
