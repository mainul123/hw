#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

app_count = 0
org_countnt = 0

for one_apple in apple:
    if one_apple > 0:
        if t >= a + one_apple >= s:
            app_cnt += 1
for one_orange in orange:
    if one_orange < 0:
           if t >= b + one_orange >= s:
            org_cnt += 1

print(app_count)
print(org_count)
