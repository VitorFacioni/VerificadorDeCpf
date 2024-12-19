class validarcpf():
    def validar (cpf):
        digito1 = 0
        digito2 = 0
        m1 = 10
        m2 = 11
        for i,num in enumerate(cpf):
            if i == 9:
                break
            digito1 = digito1 + (int(num)*m1)
            m1 = m1 -1
        digito1 = (digito1 * 10)%11
        for i,num in enumerate(cpf):
            if i == 10:
                break
            digito2 = digito2 + (int(num)*m2)
            m2 = m2 - 1
        digito2 = (digito2 * 10)%11
        for i,num in enumerate(cpf):
            if i == 9:
                if int(num) == digito1:
                    val1 = True
                else:
                    val1 = False     
            if i == 10:
                if int(num) == digito2:
                    val2 = True
                else:
                    val2 = False
        if val1 == True and val2 == True:
            return True
        else:
            return False
    def numerador (cpf,cont):
        cont = cont - 1
        for i,num in enumerate(cpf):
            if i == cont:
                return num

                
            