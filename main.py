x = int(input("Līdz kuram skaitlim saskaitīt?: "))
y = 0
for i in range(1, x+1):
  y = i + y
print("Summa ir", y)