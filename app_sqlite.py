"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""


#Passo 1 - Conectar/ criar o banco de dados

import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()


# Passo 2 - Criar tabelas

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
idade INTEGER,
email TEXT
               )
''')


# pASSO 3 -iNSERIR DADOS

cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('José', 18, 'jose@gmail.com'))


cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Matheus', 15, 'Maheus@gmail.com'))


cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Hiago', 16, 'Hiago@gmail.com'))


cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Iuri', 17, 'Iuri@gmail.com'))



cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Miguel', 15, 'Miguel@gmail.com'))


conn.commit()

print("Dados inseridos!\n")




# Passo 4 - Listar dados

print("Lista de alunos cadastrados:")
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

 # Passo 5 - Atualizar um registro

cursor.execute('UPDATE alunos SET email = ? WHERE nome = ?',
               ('jose.dev@gmail.com', 'Jose'))
conn.commit('Após atualização do email do José:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()




# Passo 6 - Deletar um registro

cursor.execute('DELET FROM alunos WHERE nome = ?', ('Mathues',))
conn.commit()

print('Após deletar do email do Matheus:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Encerrar conexão
conn.close()
