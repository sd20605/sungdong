var = int(input("몇단까지 입력할까요?"))
print(var)
print("구구단을 출력합니다.\n")
def multi (var):
   for x in range(1,var+1):
       print("------["+str(x)+"단] ------")
       for y in range(1,var+1):
           print(x, "X", y, "=", x*y)

multi(var)


