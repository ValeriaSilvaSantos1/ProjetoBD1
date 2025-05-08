import sqlite3

conn = sqlite3.connect('zoo.db')
cursor = conn.cursor()

# Executa o script de criação das tabelas a partir do arquivo
with open('tabelas.sql', 'r') as f:
    script = f.read()

cursor.executescript(script)

# Inserindo habitats
cursor.execute("INSERT INTO Habitat (nome, tipo) VALUES ('Savana Africana', 'Terrestre')")
cursor.execute("INSERT INTO Habitat (nome, tipo) VALUES ('Floresta Amazônica', 'Terrestre')")
cursor.execute("INSERT INTO Habitat (nome, tipo) VALUES ('Aquário Tropical', 'Aquático')")
cursor.execute("INSERT INTO Habitat (nome, tipo) VALUES ('Deserto do Saara', 'Terrestre')")
cursor.execute("INSERT INTO Habitat (nome, tipo) VALUES ('Pantanal', 'Aquático')")

# Inserindo animais
cursor.execute("INSERT INTO Animal (nome, especie, idade, habitat_id) VALUES ('Simba', 'Leão', 5, 1)")
cursor.execute("INSERT INTO Animal (nome, especie, idade, habitat_id) VALUES ('Zazu', 'Arara Azul', 3, 2)")
cursor.execute("INSERT INTO Animal (nome, especie, idade, habitat_id) VALUES ('Nemo', 'Peixe-palhaço', 2, 3)")
cursor.execute("INSERT INTO Animal (nome, especie, idade, habitat_id) VALUES ('Rafiki', 'Babuíno', 7, 4)")
cursor.execute("INSERT INTO Animal (nome, especie, idade, habitat_id) VALUES ('Piranha', 'Pygocentrus nattereri', 1, 5)")

# Inserindo cuidadores
cursor.execute("INSERT INTO Cuidador (nome, animal_id) VALUES ('Carlos Silva', 1)")
cursor.execute("INSERT INTO Cuidador (nome, animal_id) VALUES ('Ana Souza', 2)")
cursor.execute("INSERT INTO Cuidador (nome, animal_id) VALUES ('Pedro Lima', 3)")
cursor.execute("INSERT INTO Cuidador (nome, animal_id) VALUES ('Juliana Castro', 4)")
cursor.execute("INSERT INTO Cuidador (nome, animal_id) VALUES ('Marcos Ribeiro', 5)")

conn.commit()
conn.close()
