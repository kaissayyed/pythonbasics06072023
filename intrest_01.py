p = float(input("Enter Amount : "))
r = float(input("Enter Rate : "))
t = float(input("Enter Period : "))
def calculate(p,r,t):
  result = (p*r*t) / 100
  print(result)

calculate(p,r,t)
