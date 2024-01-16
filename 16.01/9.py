a = int(input())
s = (a//100)%10
d = (a%100)//10
e = (a%10)
sum1 = s + d
sum2 = d + e
print(sum1, sum2)
if sum1 >= sum2:
    print(str(sum1) + str(sum2))
else:
    print(str(sum2) + str(sum1))
