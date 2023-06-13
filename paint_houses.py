# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

from functools import cache
from math import inf

def paint_cost(costs):
    houses = len(costs)
    if houses == 0:
        return 0
    colors = len(costs[0])
    if colors == 0:
        return 0

    @cache
    def dp(house, color):
        if house >= houses:
            return 0
        
        cost = costs[house][color]
        
        min_next_cost = inf
        for next_color in range(colors):
            if next_color != color:
                next_cost = dp(house+1, next_color)
                min_next_cost = min(min_next_cost, next_cost)

        return cost + min_next_cost

    min_cost = inf
    for color in range(colors):
        cost = dp(0, color)
        min_cost = min(min_cost, cost)

    return min_cost


print(paint_cost([[1, 5, 3],[4,10,11]])) #=> 7