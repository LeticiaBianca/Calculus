import math
from sympy import *


x = symbols("x")

na = "x**2 + 2*x + 7"

def integral(da, db, numerador, denominador):

    expr = "(" + numerador +")/(" + denominador +")"

    if(da != "" and db != ""):
        r = integrate(eval(expr), (x, da, db))
    else:
        r = integrate(eval(expr), x)
    
    return latex(r)

    if(verificanum(na) and verificanum(nb) and verificanum(a) and verificanum(b) and verificanum(c)):
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

            if(da != "" and db != ""):
        
                if(verificanum(da) and verificanum(db)):
                    da = calculaDef(A, x1, B, x2, da)
                    db = calculaDef(A, x1, B, x2, db)

                    resultado = da - db
                else:
                    resultado = "Digite números para definir a integral ou n se quiser indefinida"
            else:
                resultado = "Resultado: ",int(A),"ln(x - ", int(x1), ")+",int(B),"ln(x - ",int(x2),") + C"
        else:
            resultado = "Trabalhando nisto..."
    else:
        resultado = "Por Favor digite números válidos"

    return resultado

def verificanum(x):
    try:
        int(x)
    except:
        return False
    return True

def calculaDef(A, x1, B, x2, x):
    aux = int(x) - int(x1)
    if(aux == 0):
        p1 = 0
    else:
        if(aux<0):
            aux = aux * -1
        p1 = math.log(aux,2)
   
    aux = int(x) - int(x2)
    if(aux == 0):
        p2 = 0
    else:
        if(aux<0):
            aux = aux * -1
        p2 = math.log(aux, 2)

    return int(A)*int(p1) + int(B)*int(p2)