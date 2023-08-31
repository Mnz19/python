A = int(2)
B = int(7)
C = float(3.5)
L = False

expr1 = (2<5) and ((15/3)==5)
expr2 = (2 < 5) and ((15/3) == 5)
expr3 = B = A * C and (L or True)
expr4 = B == A * C and (L or True)
expr5 = not L or True
expr6 = ((B/A) == C) or ((B/A)!=C)
expr7 = ((B/A) == C) or ((B/A)!=C) and L

print(expr1)
print(expr2)
print(expr3)
print(expr4)
print(expr5)
print(expr6)
print(expr7)
    