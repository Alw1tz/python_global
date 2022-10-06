#input
# 59
# 480 1227875044 -4 -3 67 -5351 141187766 -8509591 16678549 146293 -2889 -170407464 -31 -431289 -69 168 13 833 346 133173075 150 59343 39627598 160 -25227 -4625 -508 111203789 -168186422 1303000 -183 -129798436 -947737 124974 -5097533 -140 196978 163518 -124574976 -46936 7689359 4 -16333 68620218 2 33283 -13 -21726403 -1959 85549 -241 2 93426 6439 988086988 19919714 -11 18751241 374940148

n = int(input())

numbers = [int(x) for x in input().split()]

for num in numbers:
  bits = bin(num)
  if (num >= 0):
    print(bits.count("1"), "", end="")
  else:
    print(format(num + 1, '033b').count("0"), "", end="")