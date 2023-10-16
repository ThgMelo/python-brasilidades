from cpf_cnpj import Documento

exemplo_cnpj = "35379838000112"
exemplo_cpf = "43826000064"

documento = Documento.cria_documento(exemplo_cpf)
print(documento)