import json
import tkinter as tk
from tkinter import messagebox, ttk  # ttk para o dropdown

# salvar os dados no JSON
def salvar_dados(jogadores, arquivo="jogadores.json"):
    with open(arquivo, 'w') as f:
        json.dump(jogadores, f)

# carregar dados JSON
def carregar_dados(arquivo="jogadores.json"):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# janela principal
class JanelaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Jogadores de Futebol")

        # menu
        tk.Button(master, text="Adicionar Jogador", command=self.abrir_adicionar_jogador).pack(pady=10)
        tk.Button(master, text="Exibir Jogador", command=self.abrir_exibir_jogador).pack(pady=10)
        tk.Button(master, text="Atualizar Dados do Jogador", command=self.abrir_atualizar_dados).pack(pady=10)
        tk.Button(master, text="Atualizar Estatísticas do Jogador", command=self.abrir_atualizar_estatisticas).pack(pady=10)
        tk.Button(master, text="Remover Jogador", command=self.abrir_remover_jogador).pack(pady=10)

    def abrir_adicionar_jogador(self):
        JanelaAdicionarJogador(self.master)

    def abrir_exibir_jogador(self):
        JanelaExibirJogador(self.master)

    def abrir_atualizar_dados(self):
        JanelaAtualizarDados(self.master)

    def abrir_atualizar_estatisticas(self):
        JanelaAtualizarEstatisticas(self.master)

    def abrir_remover_jogador(self):
        JanelaRemoverJogador(self.master)

# adicionar jogador
class JanelaAdicionarJogador:
    def __init__(self, master):
        self.janela = tk.Toplevel(master)
        self.janela.title("Adicionar Jogador")

        tk.Label(self.janela, text="Nome do Jogador:").grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.janela)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(self.janela, text="Idade:").grid(row=1, column=0)
        self.idade_entry = tk.Entry(self.janela)
        self.idade_entry.grid(row=1, column=1)

        tk.Label(self.janela, text="Posição:").grid(row=2, column=0)
        self.posicao_entry = tk.Entry(self.janela)
        self.posicao_entry.grid(row=2, column=1)

        tk.Label(self.janela, text="Número da Camisa:").grid(row=3, column=0)
        self.numero_camisa_entry = tk.Entry(self.janela)
        self.numero_camisa_entry.grid(row=3, column=1)

        tk.Button(self.janela, text="Adicionar", command=self.adicionar_jogador).grid(row=4, columnspan=2)

    def adicionar_jogador(self):
        nome = self.nome_entry.get().strip().lower()
        idade = self.idade_entry.get()
        posicao = self.posicao_entry.get()
        numero_camisa = self.numero_camisa_entry.get()

        if nome and idade and posicao and numero_camisa:
            jogadores[nome] = {
                'idade': int(idade),
                'posição': posicao,
                'número da camisa': int(numero_camisa),
                'gols': 0,
                'assistências': 0,
                'partidas': 0
            }
            messagebox.showinfo("Sucesso", f"Jogador {nome.title()} adicionado!")
            salvar_dados(jogadores)
            self.janela.destroy()  
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")

# exibir jogador
class JanelaExibirJogador:
    def __init__(self, master):
        self.janela = tk.Toplevel(master)
        self.janela.title("Exibir Jogador")

        tk.Label(self.janela, text="Selecione o Jogador:").grid(row=0, column=0)
        self.combo_jogadores = ttk.Combobox(self.janela, values=list(jogadores.keys()))
        self.combo_jogadores.grid(row=0, column=1)

        tk.Button(self.janela, text="Exibir", command=self.exibir_jogador).grid(row=1, columnspan=2)

    def exibir_jogador(self):
        nome = self.combo_jogadores.get().strip().lower()
        if nome in jogadores:
            jogador = jogadores[nome]
            info = (f"Nome: {nome.title()}\n"
                    f"Idade: {jogador['idade']}\n"
                    f"Posição: {jogador['posição']}\n"
                    f"Número da camisa: {jogador['número da camisa']}\n"
                    f"Gols: {jogador['gols']}\n"
                    f"Assistências: {jogador['assistências']}\n"
                    f"Partidas jogadas: {jogador['partidas']}")
            messagebox.showinfo("Estatísticas do Jogador", info)
            self.janela.destroy()  # Fecha a janela após exibir
        else:
            messagebox.showwarning("Atenção", "Jogador não encontrado!")

# atualizar dados 
class JanelaAtualizarDados:
    def __init__(self, master):
        self.janela = tk.Toplevel(master)
        self.janela.title("Atualizar Dados do Jogador")

        tk.Label(self.janela, text="Selecione o Jogador:").grid(row=0, column=0)
        self.combo_jogadores = ttk.Combobox(self.janela, values=list(jogadores.keys()))
        self.combo_jogadores.grid(row=0, column=1)

        tk.Label(self.janela, text="Nova Idade:").grid(row=1, column=0)
        self.idade_entry = tk.Entry(self.janela)
        self.idade_entry.grid(row=1, column=1)

        tk.Label(self.janela, text="Nova Posição:").grid(row=2, column=0)
        self.posicao_entry = tk.Entry(self.janela)
        self.posicao_entry.grid(row=2, column=1)

        tk.Label(self.janela, text="Novo Número da Camisa:").grid(row=3, column=0)
        self.numero_camisa_entry = tk.Entry(self.janela)
        self.numero_camisa_entry.grid(row=3, column=1)

        tk.Button(self.janela, text="Atualizar", command=self.atualizar_dados_jogador).grid(row=4, columnspan=2)

    def atualizar_dados_jogador(self):
        nome = self.combo_jogadores.get().strip().lower()
        if nome in jogadores:
            idade = self.idade_entry.get()
            posicao = self.posicao_entry.get()
            numero_camisa = self.numero_camisa_entry.get()

            if idade and posicao and numero_camisa:
                jogadores[nome].update({
                    'idade': int(idade),
                    'posição': posicao,
                    'número da camisa': int(numero_camisa)
                })
                messagebox.showinfo("Sucesso", f"Dados do jogador {nome.title()} atualizados!")
                salvar_dados(jogadores)
                self.janela.destroy()  
            else:
                messagebox.showwarning("Atenção", "Preencha todos os campos para atualizar.")
        else:
            messagebox.showwarning("Atenção", "Jogador não encontrado!")

# atualizar estatísticas
class JanelaAtualizarEstatisticas:
    def __init__(self, master):
        self.janela = tk.Toplevel(master)
        self.janela.title("Atualizar Estatísticas do Jogador")

        tk.Label(self.janela, text="Selecione o Jogador:").grid(row=0, column=0)
        self.combo_jogadores = ttk.Combobox(self.janela, values=list(jogadores.keys()))
        self.combo_jogadores.grid(row=0, column=1)

        tk.Label(self.janela, text="Gols:").grid(row=1, column=0)
        self.gols_entry = tk.Entry(self.janela)
        self.gols_entry.grid(row=1, column=1)

        tk.Label(self.janela, text="Assistências:").grid(row=2, column=0)
        self.assistencias_entry = tk.Entry(self.janela)
        self.assistencias_entry.grid(row=2, column=1)

        tk.Label(self.janela, text="Partidas Jogadas:").grid(row=3, column=0)
        self.partidas_entry = tk.Entry(self.janela)
        self.partidas_entry.grid(row=3, column=1)

        tk.Button(self.janela, text="Atualizar", command=self.atualizar_estatisticas_jogador).grid(row=4, columnspan=2)

    def atualizar_estatisticas_jogador(self):
        nome = self.combo_jogadores.get().strip().lower()
        if nome in jogadores:
            gols = self.gols_entry.get()
            assistencias = self.assistencias_entry.get()
            partidas = self.partidas_entry.get()

            if gols and assistencias and partidas:
                jogadores[nome].update({
                    'gols': int(gols),
                    'assistências': int(assistencias),
                    'partidas': int(partidas)
                })
                messagebox.showinfo("Sucesso", f"Estatísticas do jogador {nome.title()} atualizadas!")
                salvar_dados(jogadores)
                self.janela.destroy()  
            else:
                messagebox.showwarning("Atenção", "Preencha todos os campos para atualizar.")
        else:
            messagebox.showwarning("Atenção", "Jogador não encontrado!")

# remover jogador
class JanelaRemoverJogador:
    def __init__(self, master):
        self.janela = tk.Toplevel(master)
        self.janela.title("Remover Jogador")

        tk.Label(self.janela, text="Selecione o Jogador:").grid(row=0, column=0)
        self.combo_jogadores = ttk.Combobox(self.janela, values=list(jogadores.keys()))
        self.combo_jogadores.grid(row=0, column=1)

        tk.Button(self.janela, text="Remover", command=self.remover_jogador).grid(row=1, columnspan=2)

    def remover_jogador(self):
        nome = self.combo_jogadores.get().strip().lower()
        if nome in jogadores:
            del jogadores[nome]
            messagebox.showinfo("Sucesso", f"Jogador {nome.title()} removido!")
            salvar_dados(jogadores)
            self.janela.destroy()  
        else:
            messagebox.showwarning("Atenção", "Jogador não encontrado!")

# inicializando os dados
jogadores = carregar_dados()

# interface 
root = tk.Tk()
app = JanelaPrincipal(root)
root.mainloop()