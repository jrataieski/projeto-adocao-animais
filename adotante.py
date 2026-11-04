class Adotante:
    def __init__(self, nome, cpf, idade, endereco, comprovante_residencia, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.comprovante_residencia = comprovante_residencia  # sim ou nao
        self.telefone = telefone

    def verificar_requisitos(self):
        # Regra de negocio: Precisa ser maior de idade E ter comprovante de residencia
        if self.idade >= 18 and self.comprovante_residencia:
            return True
        else:
            return False