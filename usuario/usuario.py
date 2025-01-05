class Usuario:
    def __init__(self, cpf, nome, data_nascimento, endereço):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereço = endereço


def criar_usuario(lista_usuarios, cpf, nome, data_nascimento, endereço):
    usuario = Usuario(cpf, nome, data_nascimento, endereço)
    lista_usuarios.append(usuario)
    return usuario


def filtrar_usuario(lista_usuarios, cpf):
    for usuario in lista_usuarios:
        if usuario.cpf == cpf:
            return usuario
