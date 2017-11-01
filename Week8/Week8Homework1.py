P=int(input())
t=int(input())
r1=0.0498
r2=0.0500
money1=P*((1+r1/4)**(4*t))
money2=P*((1+r2)**t)
print(int(money2))
print(int(money2)-int(money1))
