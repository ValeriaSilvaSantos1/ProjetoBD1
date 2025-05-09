import sqlite3

conn = sqlite3.connect('zoo.db')
cursor = conn.cursor()

# Executa o script de criação das tabelas a partir do arquivo
with open('tabelas.sql', 'r') as f:
    script = f.read()

cursor.executescript(script)

# Verifica se os dados já existem
cursor.execute("SELECT COUNT(*) FROM Animal")
total_animais = cursor.fetchone()[0]

if total_animais == 0:


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

#Lista de todos os animais com seu habitat.
def consultar_animais ():
    cursor.execute('''
SELECT a.nome AS animal, a.especie, h.nome AS habitat, h.tipo
FROM Animal a
JOIN Habitat h ON a.habitat_id = h.id
''')
    for row in cursor.fetchall():
         print(row)

#Lista de todos os cuidadores e os animais que cuidam.
def cuidadores_animais ():
    cursor.execute('''
SELECT c.nome AS cuidador, a.nome AS animal, a.especie
FROM Cuidador c
JOIN Animal a ON c.animal_id = a.id;
''')
    for row in cursor.fetchall():
        print(row)
                   
#Mostrar todos os habitats e quantos animais vivem em cada.
def habitats_animais ():
    cursor.execute('''
SELECT h.nome AS habitat, COUNT(a.id) AS total_animais
FROM Habitat h
LEFT JOIN Animal a ON a.habitat_id = h.id
GROUP BY h.id;
''')
    for row in cursor.fetchall():
        print(row)

#Quantidade de animais por habitat.
def animais_habitat ():
    cursor.execute('''
SELECT h.tipo, COUNT(a.id) AS total_animais
FROM Habitat h
LEFT JOIN Animal a ON a.habitat_id = h.id
GROUP BY h.tipo;
''')
    for row in cursor.fetchall():
        print(row)


def menu():
    while True:

        print("\n--- MENU DO ZOOLÓGICO ---")
        print("1. Consultar animais")
        print("2. Ver cuidadores e animais")
        print("3. Ver habitats e seus animais")
        print("4. Ver animais de um habitat")
        print("0. Sair")
        print("--------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            consultar_animais()
        elif opcao == "2":
            cuidadores_animais()
        elif opcao == "3":
            habitats_animais()
        elif opcao == "4":
            animais_habitat()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para continuar...")

# Executa o menu
menu()

conn.close()