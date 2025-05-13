### 135. Candy

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

* Each child must have at least one candy.
* Children with a higher rating get more candies than their neighbors.  

Return the minimum number of candies you need to have to distribute the candies to the children.

**Example 1:**

Input: ratings = [1,0,2]  
Output: 5  
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

**Example 2:**

Input: ratings = [1,2,2]  
Output: 4  
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.  
The third child gets 1 candy because it satisfies the above two conditions.  
 

**Constraints:**

n == ratings.length  
1 <= n <= 2 * 104  
0 <= ratings[i] <= 2 * 104

```python
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        i = 1
        size = len(ratings)
        sum = 1
        while i < size:
            if ratings[i] == ratings[i-1]:
                sum+=1
                i +=1 
                continue
            peak = 1
            while i < size and ratings[i] > ratings[i-1]:
                peak += 1
                sum += peak
                i += 1
            down = 1
            while i < size and ratings[i] < ratings[i-1]:
                sum += down
                down += 1
                i += 1
            if down > peak:
                sum += (down-peak)

        return (sum)
```