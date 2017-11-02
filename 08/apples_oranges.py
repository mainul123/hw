
app_count = 0
org_count = 0

for one_apple in apple:
    if one_apple > 0:
        if t >= a + one_apple >= s:
            app_cnt += 1
for one_orange in orange:
    if one_orange < 0:
           if t >= b + one_orange >= s:
            org_cnt += 1

print(app_cnt(s,t))
print(org_cnt(s,t))
