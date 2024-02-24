#!/bin/python3
alice = list(map(int, input().split()))
bob = list(map(int, input().split()))
aliceScore = 0
bobScore = 0
for i in range(3):
    if alice[i] > bob[i]:
        aliceScore += 1
    elif alice[i] < bob[i]:
        bobScore += 1
print(aliceScore, bobScore)
