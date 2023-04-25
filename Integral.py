import math

def integral(na, nb, a, b, c):

    if(verificanum(na, nb, a, b, c)):
        na = int(na)
        nb= int(nb)

        a = int(a)
        b = int(b)
        c = int(c)

        delta = b*b - (4*a*c)
       
        if(delta >= 0):
            x1 = (-b + math.sqrt(delta))/2*a
            x2 = (-b - math.sqrt(delta))/2*a

            deltax = int(x2-x1)
            A = int((na*x1 + nb))/deltax
            B = int((na*x2 + nb))/deltax

            resultado = "Resultado: ",int(A),"ln(x - ", int(x1), ")+",int(B),"ln(x - ",int(x2),") + C"
        else:
            resultado = "Trabalhando nisto..."
    else:
        resultado = "Por Favor digite números válidos"

    return resultado

def verificanum(na, nb, a, b, c):
    try:
        int(na)
        int(nb)

        int(a)
        int(b)
        int(c)
    except:
        return False
    return True