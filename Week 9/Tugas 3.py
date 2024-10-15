array = [4, 5, 11, 12, 14, 16, 16, 19]
bil_prima = []

for bilangan in array :
    if bilangan >= 2 :
        prima = True
        for i in range (2,int(bilangan ** 0.5)+1) :
            if bilangan % i == 0 :
                prima = False
                break
        if prima :
            bil_prima.append(bilangan)

banyak_prima = len(bil_prima)
print("bilangan prima dalam array :", bil_prima)
print("banyaknya bilangan prima :", banyak_prima, "bilangan")
