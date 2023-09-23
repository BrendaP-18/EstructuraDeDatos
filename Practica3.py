maxf = 3
maxc = 5
a = [[0.0 for _ in range(maxf)] for _ in range(maxc)]

for f in range(maxf):
    for c in range(maxc):
        a[f][c] = float(input(f"Introduce un valor para a[{f}][{c}]: "))
    
    print("La matriz es: ")
    for f in range(maxf):
         
         for c in range(maxc):
              print(a[f][c], end = " ")
         print()
