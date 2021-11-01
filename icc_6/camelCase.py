st = input()
st = list(st)
p = False
new = []


def remover(x):
    global st
    r = st[x::]
    for i in range(0,len(r)):
        st.pop()
def modificar():
    global st,new

    for i in new:
        st.append(i)


for i in st:
    if i == '_':
        new = st(i::)
        remover(i)
        modificar()

print(st)