from datetime import date # importa a data exata

class Adocao:
    def __init__(self, animal, adotante):
        self.animal = animal
        self.adotante = adotante
        self.data_adocao = date.today()  
        self.status_adocao = "Pendente"
        self.termo_adocao = ""

    def registrar_adocao(self):
        #  verifica se o adotante cumpre os requisitos solicitados
        if self.adotante.verificar_requisitos():
            # verifica se o animal realmente esta disponivel
            if self.animal.disponibilidade:
                self.status_adocao = "Aprovada"
                self.animal.atualizar_disponibilidade(False)  #tira a disponibilidade do animal
                self.gerar_termo_adocao()  # gera o texto do termo de adocao
                print("Adoção realizada com sucesso!")
                return True
            else:
                print("Erro: Este animal já foi adotado!")
                return False
        else:
            print("Erro: O adotante não atende aos requisitos (menor de idade ou sem comprovante).")
            return False

    def gerar_termo_adocao(self):
        # aqui é criado um texto para o contrato de adocao
        self.termo_adocao = (
            f"\n=== TERMO DE ADOÇÃO RESPONSÁVEL ==="
            f"\nData da Adoção: {self.data_adocao}"
            f"\nNome do Adotante: {self.adotante.nome} | CPF: {self.adotante.cpf}"
            f"\nAnimal Adotado: {self.animal.nome} ({self.animal.especie})"
            f"\nStatus da adoção: {self.status_adocao}"
            f"\n"
            f"\n Assinatura do Responsavel \n"
            f"\n-------------------------------------\n"
        )
        print(self.termo_adocao)