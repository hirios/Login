cifra = """
a = bb
b = 7y
c = 3d
d = ppk
e = hjk
f = awr
g = iii
h = ybv
i = m7f
j = 89j
k = 788
l = kdf
m = aks
n = qwn
o = ooj
p = kam
q = arr
r = oi0
s = nbm
t = 0km
u = xzs
v = plk
w = imj
y = ykm
x = bb4
z = 08u
  = 777
 """.split()


def codificar(senha):
    password = []
    for letra in senha:
        for indice in range(0, len(cifra)):
            if cifra[indice] == letra:
                password.append(cifra[indice + 2])
    return "`".join(password)


def decodificar(codigo):
    password = []
    split = codigo.split("`")
    for item in split:
        for indice in range(0, len(cifra)):
            if item == cifra[indice]:
                password.append(cifra[indice - 2])
    return "".join(password)


    
