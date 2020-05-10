n=17
for i in range(1,n+1):
    print(str(i).rjust(len(bin(n)[2:])),oct(i)[2:].rjust(len(bin(n)[2:])),hex(i)[2:].upper().rjust(len(bin(n)[2:])),bin(i)[2:].rjust(len(bin(n)[2:])))
        
