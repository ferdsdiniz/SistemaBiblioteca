import tkinter as tk
from tkinter import messagebox
import datetime
import os

class Livro:
    contador_id = 1  # Contador para o ID do livro

    def __init__(self, titulo, autor):
        self.id_livro = Livro.contador_id
        Livro.contador_id += 1
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False
        self.data_devolucao = None

class Usuario:
    contador_id = 1  # Contador para o ID do usuário

    def __init__(self, nome):
        self.id_usuario = Usuario.contador_id
        Usuario.contador_id += 1
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.multa_por_atraso = 2.0  # Valor da multa por dia de atraso

    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")

        livro = Livro(titulo, autor)
        self.livros.append(livro)
        print("Livro cadastrado com sucesso!")

    def cadastrar_usuario(self):
        nome = input("Digite o nome do usuário: ")

        usuario = Usuario(nome)
        self.usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    def emprestar_livro(self):
        id_livro = int(input("Digite o ID do livro a ser emprestado: "))
        id_usuario = int(input("Digite o ID do usuário: "))

        livro = self.encontrar_livro(id_livro)
        usuario = self.encontrar_usuario(id_usuario)

        if not livro:
            print("Livro não encontrado.")
            return

        if not usuario:
            print("Usuário não encontrado.")
            return

        if livro.emprestado:
            print("O livro já está emprestado.")
            return

        livro.emprestado = True
        livro.data_devolucao = datetime.date.today() + datetime.timedelta(days=7)  # Prazo de 7 dias
        usuario.livros_emprestados.append(livro)
        print("Livro emprestado com sucesso!")

    def devolver_livro(self):
        id_livro = int(input("Digite o ID do livro a ser devolvido: "))
        id_usuario = int(input("Digite o ID do usuário: "))

        livro = self.encontrar_livro(id_livro)
        usuario = self.encontrar_usuario(id_usuario)

        if not livro:
            print("Livro não encontrado.")
            return

        if not usuario:
            print("Usuário não encontrado.")
            return

        if livro in usuario.livros_emprestados:
            livro.emprestado = False
            livro.data_devolucao = None
            usuario.livros_emprestados.remove(livro)
            print("Livro devolvido com sucesso!")
        else:
            print("O livro não está em posse deste usuário.")

    def calcular_multa(self):
        id_livro = int(input("Digite o ID do livro: "))

        livro = self.encontrar_livro(id_livro)

        if not livro:
            print("Livro não encontrado.")
            return

        if livro.emprestado and livro.data_devolucao < datetime.date.today():
            dias_atraso = (datetime.date.today() - livro.data_devolucao).days
            multa = self.multa_por_atraso * dias_atraso
            print("Multa por atraso: R$", multa)
        else:
            print("Não há multa para este livro.")

    def mostrar_livro_emprestado(self):
        id_livro = int(input("Digite o ID do livro: "))

        livro = self.encontrar_livro(id_livro)

        if not livro:
            print("Livro não encontrado.")
            return

        if livro.emprestado:
            print("Livro emprestado:")
            print("ID: ", livro.id_livro)
            print("Título: ", livro.titulo)
            print("Autor: ", livro.autor)
            print("Emprestado para:")
            for usuario in self.usuarios:
                if livro in usuario.livros_emprestados:
                    print("ID: ", usuario.id_usuario)
                    print("Nome: ", usuario.nome)
        else:
            print("O livro não está emprestado.")

    def mostrar_livros_disponiveis(self):
        print("Livros disponíveis:")
        for livro in self.livros:
            if not livro.emprestado:
                print("ID:", livro.id_livro)
                print("Título:", livro.titulo)
                print("Autor:", livro.autor)
                print("--------------------")
        if all(livro.emprestado for livro in self.livros):
            print("Não há livros disponíveis no momento.")

    def encontrar_livro(self, id_livro):
        for livro in self.livros:
            if livro.id_livro == id_livro:
                return livro
        return None

    def encontrar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def usuarios_cadastrados(self):
        print("Usuários cadastrados:")
        for usuario in self.usuarios:
            print("ID: ", usuario.id_usuario)
            print("Nome: ", usuario.nome)
            print("--------------------")
        if not self.usuarios:
            print("Não há usuários cadastrados.")

    def calcular_multa_total(self):
        total_multa = 0.0
        for usuario in self.usuarios:
            for livro in usuario.livros_emprestados:
                if livro.emprestado and livro.data_devolucao < datetime.date.today():
                    dias_atraso = (datetime.date.today() - livro.data_devolucao).days
                    multa = self.multa_por_atraso * dias_atraso
                    total_multa += multa

        if total_multa > 0:
            print("Multa total por atraso: R$", total_multa)
        else:
            print("Não há multa em atraso.")

# Restante do código...

biblioteca = Biblioteca()

while True:
    print("\n--- Menu ---")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuário")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Calcular multa")
    print("6. Mostrar livro emprestado")
    print("7. Mostrar livros disponíveis")
    print("8. Usuários cadastrados")
    print("9. Calcular multa total")
    print("0. Sair\n")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        os.system("cls")
        biblioteca.cadastrar_livro()
    elif opcao == "2":
        os.system("cls")
        biblioteca.cadastrar_usuario()
    elif opcao == "3":
        os.system("cls")
        biblioteca.emprestar_livro()
    elif opcao == "4":
        os.system("cls")
        biblioteca.devolver_livro()
    elif opcao == "5":
        os.system("cls")
        biblioteca.calcular_multa()
    elif opcao == "6":
        os.system("cls")
        biblioteca.mostrar_livro_emprestado()
    elif opcao == "7":
        os.system("cls")
        biblioteca.mostrar_livros_disponiveis()
    elif opcao == "8":
        os.system("cls")
        biblioteca.usuarios_cadastrados()
    elif opcao == "9":
        os.system("cls")
        biblioteca.calcular_multa_total()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Biblioteca")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Label
        lbl_title = tk.Label(self, text="Biblioteca", font=("Helvetica", 18))
        lbl_title.pack(pady=10)

        # Buttons
        btn_cadastrar_livro = tk.Button(self, text="Cadastrar Livro", command=self.cadastrar_livro)
        btn_cadastrar_livro.pack(pady=5)

        btn_cadastrar_usuario = tk.Button(self, text="Cadastrar Usuário", command=self.cadastrar_usuario)
        btn_cadastrar_usuario.pack(pady=5)

        btn_emprestar_livro = tk.Button(self, text="Emprestar Livro", command=self.emprestar_livro)
        btn_emprestar_livro.pack(pady=5)

        btn_devolver_livro = tk.Button(self, text="Devolver Livro", command=self.devolver_livro)
        btn_devolver_livro.pack(pady=5)

    def cadastrar_livro(self):
        # Implementar a lógica para cadastrar um livro
        messagebox.showinfo("Cadastrar Livro", "Funcionalidade em desenvolvimento")

    def cadastrar_usuario(self):
        # Implementar a lógica para cadastrar um usuário
        messagebox.showinfo("Cadastrar Usuário", "Funcionalidade em desenvolvimento")

    def emprestar_livro(self):
        # Implementar a lógica para emprestar um livro
        messagebox.showinfo("Emprestar Livro", "Funcionalidade em desenvolvimento")

    def devolver_livro(self):
        # Implementar a lógica para devolver um livro
        messagebox.showinfo("Devolver Livro", "Funcionalidade em desenvolvimento")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
