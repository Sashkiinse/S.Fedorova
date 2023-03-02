n = int(input())
while n > 0: 
    print(n % 10); n //= 10
import math

i=int(input())

a=[int(a) for a in str(i)]

if a[0]+a[1]==a[2]+a[3]:

   print('сумма двух первых цифр РАВНА сумме двух последних цифр')

else:

   print('сумма двух первых цифр НЕ РАВНА сумме двух последних цифр')

if sum(a)%3==0:

   print('сумма цифр кратна 3')

else:

   print('сумма цифр НЕ кратна 3')