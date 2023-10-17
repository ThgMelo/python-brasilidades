class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")
        
    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False