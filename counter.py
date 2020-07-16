from collections import Counter 

number_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))  
customers = int(input())
 
earnings = 0
 
for i in range(customers):
    size, value = list(map(int, input().split()))
    if shoe_sizes[size]: 
        earnings += value
        shoe_sizes[size] -= 1 
        
print(earnings)
