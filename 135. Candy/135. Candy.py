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