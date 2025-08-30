size = int(input("Enter the size of the pattern:"))
t = size
while t>0 :
  for j in range(size) :
    print('*', end="")
  print('')
  t-=1
