import sqlite3
from tabulate import tabulate

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

#Lista de todos os animais.
def consultar_animais():
    cursor.execute('''
    SELECT a.nome AS animal, a.especie
    FROM Animal a
    ''')
    results = cursor.fetchall()
    headers = ["Animal", "Espécie"]
    print(tabulate(results, headers, tablefmt="fancy_grid"))


# Lista de todos os cuidadores e os animais que cuidam.
def cuidadores_animais():
    cursor.execute('''
    SELECT c.nome AS cuidador, a.nome AS animal, a.especie
    FROM Cuidador c
    JOIN Animal a ON c.animal_id = a.id;
    ''')
    results = cursor.fetchall()
    headers = ["Cuidador", "Animal", "Espécie"]
    print(tabulate(results, headers, tablefmt="fancy_grid"))
                   
#Mostrar todos os habitats e quantos animais vivem em cada.
def habitats_animais():
    cursor.execute('''
    SELECT h.nome AS habitat, COUNT(a.id) AS total_animais
    FROM Habitat h
    LEFT JOIN Animal a ON a.habitat_id = h.id
    GROUP BY h.id;
    ''')
    results = cursor.fetchall()
    headers = ["Habitat", "Total de Animais"]
    print(tabulate(results, headers, tablefmt="fancy_grid"))

#Cuidadores sem animal associado.
def cuidadores_sem_animal():
    cursor.execute('''
    SELECT nome
    FROM Cuidador
    WHERE animal_id IS NULL;
    ''')
    results = cursor.fetchall()
    headers = ["Cuidador sem Animal"]
    print(tabulate(results, headers, tablefmt="fancy_grid"))

#Total de animais por tipo de habitat.
def total_animais_por_tipo_habitat():
    cursor.execute('''
    SELECT h.tipo AS tipo_habitat, COUNT(a.id) AS total_animais
    FROM Habitat h
    LEFT JOIN Animal a ON a.habitat_id = h.id
    GROUP BY h.tipo;
    ''')
    results = cursor.fetchall()
    headers = ["Tipo de Habitat", "Total de Animais"]
    print(tabulate(results, headers, tablefmt="fancy_grid"))


def menu():
    while True:

        print("\n--- MENU DO ZOOLÓGICO ---")
        print("1. Consultar animais")
        print("2. Ver cuidadores e animais")
        print("3. Ver habitats e seus animais")
        print("4. Cuidadores sem animal associado")
        print("5. Total de animais por tipo de habitat")
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
            cuidadores_sem_animal()
        elif opcao == "5":
            total_animais_por_tipo_habitat()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para continuar...")

# Executa o menu
menu()

conn.close()