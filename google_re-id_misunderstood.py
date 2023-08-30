# Re-ID
# =====
# 
# There's some unrest in the minion ranks: minions with ID numbers like "1",
# "42", and other "good" numbers have been lording it over the poor
# minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has
# tasked you with reassigning everyone new random IDs based on a Completely Foolproof
# Scheme.
# 
# Commander Lambda has concatenated the prime numbers in a single long string:
# "2357111317192329...". Now every minion must draw a number from a hat. That
# number is the starting index in that string of primes, and the minion's new ID number
# will be the next five digits in the string. So if a minion draws "3", their ID
# number will be "71113".
# 
# Help the Commander assign these IDs by writing a function solution(n) which takes in the
# starting index n of Lambda's string of all primes, and returns the next five digits
# in the string. Commander Lambda has a lot of minions, so the value of n will always be
# between 0 and 10000.

import math

def fetch_next_prime(num):
    if num <= 1:
        return 2
    elif num % 2 == 0:
        if num == 2:
            return 3
        num += 1
    else:
        num += 2
        
    while True:
        factor_count = 0
        for i in range(2, math.ceil(num/2)):
            if num%i==0:
                factor_count += 1
        if factor_count == 0:
            return num
        num += 2
        
    
def solution(i):
    id = ""
    index = i
    while len(id) < 5:
        index = fetch_next_prime(index)
        id = id + str(index)
    
    res = ""
    for ch in id:
        res += ch
        if len(res) == 5:
            break
    
    return res

print(solution(0))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
