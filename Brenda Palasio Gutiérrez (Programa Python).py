#Brenda Lizeth Palasio Gutiérrez

NUM = 8
nums = [0] * NUM 
total = 0
for i in range(NUM):
    nums[i] = int(input("Por favor introduzca el número: "))
    total += nums[i]
    print("El total del mumero es:",total)