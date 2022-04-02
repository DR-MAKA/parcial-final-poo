import math as m

class Masas:

    def calcular_movimiento(self,A,Cr,m1):
        
        #Donde A es el angulo, CR es coeficiente de rozamiento y m1 es la masa 1  
        #La ecuación es: F= m2*g-(m1*g*(sin(a)+u*cons(a)))
        #Si F es mayor a 0 es porque el sistema está bajando, de lo contrario el sistema está en equilibrio o está subiendo.
        #se crea la lista donde se guardaran los datos 
        list=[]
        m2=0
        x=m.ceil(9.8*((m2-(m1*m.sin(m.radians(A)))-(m1*Cr*m.cos(m.radians(A))))/(m1+m2)))
        list.append([m2,"subiendo"])
        while x<0:
            m2+=0.5
            x=m.ceil(9.8*((m2-(m1*m.sin(m.radians(A)))-(m1*Cr*m.cos(m.radians(A))))/(m1+m2)))
            list.append([m2,"subiendo"])
        list.append([m2,"bajando"])
        return list

    def calcular_angulo(self,m1,m2,Cr):
        resp=-1
        x=0
        for i in range(75):
            x=round(m2*9.8-(m1*9.8*(m.sin(m.radians(i+10))+Cr*m.cos(m.radians(i+10)))),1)
            if x==0:
                resp=i+10
                break
        return resp

a=Masas()

print(a.calcular_movimiento(55,0.15,6))
print(a.calcular_angulo(8,6,0.2))