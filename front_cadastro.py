
class Conta:

    def __init__(self, nome, idade, endereco, telefone, email):
        self.nome = nome 
        self.idade = idade 
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def check_info(self):
    	c_nome = True 
    	c_idade = True
    	c_endereco = True
    	c_telefone = True
    	
    	
    	while c_nome:
    		
    		if (self.nome.isalpha()):
    			c_nome = False

    		else:
		    	self.nome = input("\nNome Invalido\nInsira nome: ")


    	while c_idade:

    		try:
    			int(self.idade)
    			c_idade = False
    			
    		except ValueError:
    			self.idade = input("\nIdade Invalida\nInsira idade: ")
    			


    	while c_endereco:

    		if (self.endereco.isalpha()):
    			c_endereco = False

    		else:    			
    			self.endereco = input("\nEndereco Invalido\nInsira endereco: ")




    	while c_telefone:

    		try:
    			int(self.telefone)
    			c_telefone = False
    			
    		except ValueError:
    			self.telefone = input("\nTelefone Invalido\nInsira telefone: ")



    	return True
    		

def main():
	nome = input("Insira nome: ")
	idade = input("Insira idade: ")
	endereco = input("Insira um endereco: ")
	telefone = input("Insira um telefone: ")
	email = input("Insira o email: ")

	pessoa = Conta(nome, idade, endereco, telefone, email)
	
	if (pessoa.check_info()):
		print("sucesso")
		print(pessoa.__dict__)

	else:
		pessoa.check_info()




if __name__ == '__main__':
	main()

	