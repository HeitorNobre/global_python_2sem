
class Paciente:
    def __init__(self, nome):
        self.nome = nome
        self.remedios = []
        self.tratamentos = []
        self.anotacoes = []

    def ver_remedios(self):
        return self.remedios

    def ver_tratamentos(self):
        return self.tratamentos

    def adicionar_anotacao(self, anotacao):
        self.anotacoes.append(anotacao)


class Medico:
    def cadastrar_remedio(self, paciente, remedio):
        paciente.remedios.append(remedio)

    def atribuir_tratamento(self, paciente, tratamento):
        paciente.tratamentos.append(tratamento)

    def ver_tratamentos_paciente(self, paciente):
        return paciente.tratamentos

def salvar_pacientes_em_arquivo(pacientes, arquivo):
    with open(arquivo, "w") as file:
        for nome, paciente in pacientes.items():
            file.write(f"Nome: {nome}\n")
            file.write(f"Remédios: {', '.join(paciente.remedios) if paciente.remedios else 'Nenhum'}\n")
            file.write(f"Tratamentos: {', '.join(paciente.tratamentos) if paciente.tratamentos else 'Nenhum'}\n")
            file.write(f"Anotações: {', '.join(paciente.anotacoes) if paciente.anotacoes else 'Nenhum'}\n")
            file.write("\n")
    print(f"Dados dos pacientes salvos em {arquivo}")


def mostrar_todos_pacientes(pacientes):
    if pacientes:
        print("\nLista de Pacientes:")
        for nome in pacientes:
            print(nome)
    else:
        print("Não há pacientes cadastrados.")

pacientes = {}
medico = Medico()
def menu_medico(pacientes, medico ):

    
    while True:
        print("\nMenu:")
        print("1. Cadastrar Paciente")
        print("2. Cadastrar Remédio para Paciente")
        print("3. Atribuir Tratamento a Paciente")
        print("4. Ver Tratamentos de Paciente")
        print("5. Ver Remédios de Paciente")
        print("6. Adicionar Anotação ao Paciente")
        print("7. Salvar Pacientes em Arquivo TXT")
        print("8. Ver Todos os Pacientes")
        print("0. Sair")
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                nome = input("Nome do paciente: ").title().strip()
                pacientes[nome] = Paciente(nome)
                print(f"Paciente {nome} cadastrado com sucesso.")

            case 2:
                nome = input("Nome do paciente: ").title().strip()
                remedio = input("Nome do remédio: ")
                if nome in pacientes:
                    medico.cadastrar_remedio(pacientes[nome], remedio)
                    print(f"Remédio {remedio} cadastrado para {nome}.")
                else:
                    print("Paciente não encontrado.")

            case 3:
                nome = input("Nome do paciente: ").title().strip()
                tratamento = input("Descrição do tratamento: ")
                if nome in pacientes:
                    medico.atribuir_tratamento(pacientes[nome], tratamento)
                    print(f"Tratamento {tratamento} atribuído a {nome}.")
                else:
                    print("Paciente não encontrado.")

            case 4:
                nome = input("Nome do paciente: ").title().strip()
                if nome in pacientes:
                    tratamentos = medico.ver_tratamentos_paciente(pacientes[nome])
                    print(f"Tratamentos de {nome}: {tratamentos}")
                else:
                    print("Paciente não encontrado.")

            case 5:
                nome = input("Nome do paciente: ").title().strip()
                if nome in pacientes:
                    remedios = pacientes[nome].ver_remedios()
                    print(f"Remédios de {nome}: {remedios}")
                else:
                    print("Paciente não encontrado.")

            case 6:
                nome = input("Nome do paciente: ").title().strip()
                anotacao = input("Anotação: ")
                if nome in pacientes:
                    pacientes[nome].adicionar_anotacao(anotacao)
                    print(f"Anotação adicionada ao paciente {nome}.")
                else:
                    print("Paciente não encontrado.")
            case 7:
                nome_arquivo = input("Digite o nome do arquivo para salvar (inclua .txt no final): ")
                salvar_pacientes_em_arquivo(pacientes, nome_arquivo)
            
            case 8:
                mostrar_todos_pacientes(pacientes)

            case 0:
                opcoes()
                break
            case _:
                print("Opção inválida. Por favor, tente novamente.")



def menu_paciente(paciente):
    while True:
        print("\nMenu Paciente:")
        print("1. Ver Tratamentos")
        print("2. Ver Remédios")
        print("3. Adicionar Comentário")
        print("4. Salvar Tratamento em TXT")
        print("0. Sair")
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                print(f"Tratamentos: {paciente.ver_tratamentos()}")
            case 2:
                print(f"Remédios: {paciente.ver_remedios()}")
            case 3:
                anotacao = input("Digite o comentário: ")
                paciente.adicionar_anotacao(anotacao)
                print("Comentário adicionado.")
            case 4:
                nome_arquivo = input("Digite o nome do arquivo para salvar (inclua .txt no final): ")
                salvar_pacientes_em_arquivo({paciente.nome: paciente}, nome_arquivo)
            case 0:
                opcoes()
                break
            case _:
                print("Opção inválida. Por favor, tente novamente.")

pacientes = {}
medico = Medico()
def opcoes():
    while True:
        tipo_usuario = input("Você é médico ou paciente? (Digite 'm' ou 'p'), caso queira sair, digite 1: ").lower().strip()

        if tipo_usuario == 'm':
            menu_medico(pacientes, medico)
            break
        elif tipo_usuario == 'p':
            nome_paciente = input("Digite seu nome: ").title().strip()
            paciente = pacientes.get(nome_paciente)
            
            if not paciente:
                print("Paciente não encontrado. Cadastrando um novo paciente.")
                paciente = Paciente(nome_paciente)
                pacientes[nome_paciente] = paciente
            menu_paciente(paciente)
            break
        elif tipo_usuario == '1':
            print('Encerrando sistema!')
            break
        else:
            print("Opção inválida.")
opcoes()

