n = int(input())
plateleira = input().split()
def trocar_position(x,y):
    global plateleira
    for i in range(0,len(plateleira)-1):
        if plateleira[i] == x:
            try:
                
                plateleira[i+y] = x
                a = i + y
                while a > 0:
                    plateleira[a-1] = plateleira
            except:
                pass


for i in range(5):
    moves = input().split()
    trocar_position(moves[0],int(moves[2]))
    print(plateleira)