p = 29
ints = [14, 6, 11]

# Find the minimum value of x from p, which is from 0 to 28. x squared mod(pow(x, 2, p)) in the "ints" list.
flag = min(x for x in range(p) if pow(x,2,p) in ints)

print(flag)