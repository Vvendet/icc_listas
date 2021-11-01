quant_brinquedos = int(input())
brinquedos = input().split()
ordem_original = brinquedos[:]

for i in range(5):
   
    ordem = input().split()

    for j in range(quant_brinquedos):
        if ordem[0] == brinquedos[j]:
            if ordem[1] == 'E':
                try:
                    k=0
                    while k < int(ordem[2]):
                        if (j-k-1) < 0 or (i-k) < 0:
                            break
                        aux = brinquedos[j-k-1]
                        brinquedos[j-k-1] = brinquedos[j-k]
                        brinquedos[j-k] = aux
                        k +=1
                 
                except:
                    
                    pass
                
                break

            if ordem[1] == 'D':

                try:
                    k=0
                    while k < int(ordem[2]):
                        aux = brinquedos[j+k+1]
                        brinquedos[j+k+1] = brinquedos[j+k]
                        brinquedos[j+k] = aux
                        k +=1

                        
    
                except: 
                    pass
                
                break

cont = 0
for l in range(quant_brinquedos):
    if (ordem_original[l] != brinquedos[l]):
        cont +=1

print(cont)