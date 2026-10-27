n = int(input())
cards = list(map(int, input().split()))
left = 0
right = n - 1
scores = [0, 0] 
turn = 0  
while left <= right:
    if cards[left] > cards[right]:
        scores[turn] += cards[left]
        left += 1
    else:
        scores[turn] += cards[right]
        right -= 1
    turn = 1 - turn  # switches between 0 and 1
print(scores[0], scores[1])