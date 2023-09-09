def fact_rect(n):
if n==0 or n==1:
  return 1
else:
  return n*fact_rect(n-1)

number=int(input ("enter a value"))
res=fact_rect(number)

print("THE FACTORIAL OF {}IS {}". format (number,res))
