#============================================
# La clase A tiene tres números reales 
#============================================

class A: 
      __a:float= 0.0
      __b:float= 0.0 
      __c:float= 0.0

      def __init__(self,a:float,b:float,c:float):
          self.a= a
          self.b= b
          self.c= c

#================================================
# La clase B tiene dos númerps reales 
#================================================
class B:
   __d:float=0.0
   __e:float=0.0

   def __init__(self,d:float,e:float):
       self.d = d
       self.e = e

       #===========================================
       # Método sumar todo (internos  +  externos)
       #===========================================
   def sumar_todo(self, aa:float, bb:float):
           x:float=self.d+self.e+aa+bb
           return x

#================
# Asociación
#================
#Usando objetos independientes
objetoA = A(1.0,2.0,3.0)
objetoB = B(4.0,5.0)
print(objetoB.sumar_todo(objetoA.a,objetoA.b))

#======================================================
# El objeto C tiene dos reales y un objeto A 
# El objeto A se instancia dentro de C
#======================================================
class C: 

    __d:float=0.0
    __e:float=0.0
    __Aa:A=None

    def __init__(self,d:float,e:float):
        self.d = d
        self.e = e
        # A está isntanciado adentro 
        self.Aa = A(1.0,2.0,3.0)

    def sumar_todo(self):
        x:float=self.d+self.e+self.Aa.a+self.Aa.b
        return x
#============================
# Composición 
# Contiene otro objeto dentro 
#=============================
objetoC= C(4.0,5.0)
print(objetoC.sumar_todo())

#====================================================
# Objeto D tiene dos reales y un objeto A
# definido por fuera
#====================================================
class D:
    __d:float=0.0
    __e:float=0.0
    __Aa:A=None

    def __init__(self,d:float,e:float,Aa:A):
        self.d = d
        self.e = e
        self.Aa= Aa

    def sumar_todo(self):
        x:float=self.d+self.e+self.Aa.a+self.Aa.b
        return 
#================================================================
# Ágregación 
# Construye el objeto agregado por fuera
#================================================================
objetoD = D(4.0,5.0,objetoA)
print(objetoD.sumar_todo())
