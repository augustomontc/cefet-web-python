from datetime import datetime

class Autor():
	def __init__(self,nascimento,primeiro_nome,ultimo_nome,segundo_nome=''):
		self.primeiro_nome = primeiro_nome
		self.segundo_nome = segundo_nome
		self.ultimo_nome = ultimo_nome
		self.nascimento = nascimento
	def nome_como_citado(self):
		return self.ultimo_nome + " " + self.primeiro_nome[:1] + "."
	def __str__(self):
		return "{nome} - {data}".format(nome=self.nome_como_citado,data=self.nascimento)

class Livro():
	def __init__(self,titulo,ano,autores=[]):
		self._titulo = titulo
		self.ano = ano
		self.autores = autores
	@property
	def titulo(self):
		if(self._titulo is None):
			raise ValueError("Erro: não é possível livro sem título")
		return self._titulo

autor = Autor("26/09/1995","Augusto","Costa","Monteiro")
print(autor.nome_como_citado())
print(autor)

livro = Livro(None,1995)
print(livro.titulo)