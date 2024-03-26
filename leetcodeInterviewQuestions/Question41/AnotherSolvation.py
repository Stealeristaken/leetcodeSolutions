f = open("user.out", 'w')
for line in stdin:
    s = set(map(int, line.rstrip()[1:-1].split(',')))
    ans = 1
    while ans in s:
        ans += 1
    print(ans, file=f)
exit(0)