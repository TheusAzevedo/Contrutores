#criar a classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento


#criar o objeto
usuario1 = Funcionarios('Jair', 'Santos', '18/04/68')
usuario2 = Funcionarios('Solange', 'Dias', '22/12/65')

'''
#criar os parametros do usuario 1
#usuario1.nome = 'Jair'
#usuario1.sobrenome = 'Santos'
#usuario1.data_nascimento = '18/04/68'

#criar os parametros do usuario 2
#usuario2.nome = 'Solange'
#usuario2.sobrenome = 'Dias'
#usuario2.data_nascimento = '22/12/65'

#print

Metodo mais longo
'''
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)
print(usuario2.nome)
print(usuario2.sobrenome)
print(usuario2.data_nascimento)