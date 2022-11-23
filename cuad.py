#----------------#Clase de los cuadruplos#----------------#
class cuad:
    def __init__(self ,oper ,op1 ,op2 ,temp):
        self.oper = oper
        self.op1 = op1
        self.op2 = op2
        self.temp = temp

    def mistring(self):
        print(f"[{self.oper}][{self.op1}][{self.op2}][{self.temp}]")
    