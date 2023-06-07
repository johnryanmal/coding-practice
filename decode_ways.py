# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

from functools import cache

def solution(msg):
    length = len(msg)
    
    @cache
    def dp(i):
        if i >= length - 1:
            return 1
        
        char = msg[i]
        after = msg[i+1]
        if char == '1' or (char == '2' and '0' <= after <= '6'):
            return dp(i+1) + dp(i+2)
        else:
            return dp(i+1)
    
    return dp(0)


print(solution('111')) #=> 3
