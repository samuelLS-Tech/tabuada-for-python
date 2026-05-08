# tabuada
for n in range(1, 11):
    print("Tabuada de:", n)
    for m in range(1, 11):
        print(f"{n}.{m:2} = {n*m:3}")

n = int(input("De qual número você quer a tabuada?"))
limite = int(input("Qual é o limite que você deseja?"))
print(f"Tabuada de {n}")

for m in range(1, limite + 1): 
    print(f"{n}.{m:2} = {n*m:4}")