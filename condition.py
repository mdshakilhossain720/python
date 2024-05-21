mark=80
result=''
if mark <30:
    print('Fail')
elif(mark<50):
    print('Mid result')
elif(mark>75):
    print("result is passed")
else:
    print("passwed")
words = ["one", "two", "three"]
for s in words:
    print(s)
i=1
while i<10:
    print(i)
    i=i+1

for letter in 'python':
    if letter =='t':
        continue
    print('this is the ',letter)
var =100
if(var ==100):
    print('is the 100')
    print('is good')
num=8
print ("num = ",num)
if num%2==0:
   if num%3==0:
      print ("Divisible by 3 and 2")
   else:
      print ("divisible by 2 not divisible by 3")
else:
   if num%3==0:
      print ("divisible by 3 not divisible by 2")
   else:
      print ("not Divisible by 2 not divisible by 3")
