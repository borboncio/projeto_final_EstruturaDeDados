from class_listaduplamenteencadeada import DoublyCircularLinkedList
from Class_tree import BinaryTree


class Tarefa:
    def __init__(self, nome, descricao, prioridade):
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = False

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"Nome: {self.nome}, Descrição: {self.descricao}, Prioridade: {self.prioridade}, Status: {status}"


class GerenciadorDeTarefas:
    def __init__(self):
        self.tree = BinaryTree()
        self.tarefas_prioritarias = DoublyCircularLinkedList()

    def adicionar_tarefa(self, tarefa):
        self.tree.insert(tarefa)
        if tarefa.prioridade:
            self.tarefas_prioritarias.append(tarefa)
        print(f"Tarefa '{tarefa.nome}' adicionada.")

    def remover_tarefa(self, nome):
        node = self.tree.search(nome)
        if node:
            self.tree.delete(nome)
            if node.key.prioridade:
                self.tarefas_prioritarias.remove(node.key)
            print(f"Tarefa '{nome}' removida.")
        else:
            print(f"Tarefa '{nome}' não encontrada.")

    def editar_tarefa(self, nome, novo_nome=None, nova_descricao=None, nova_prioridade=None):
        node = self.tree.search(nome)
        if node:
            tarefa = node.key
            if novo_nome:
                self.tree.delete(nome)
                tarefa.nome = novo_nome
                self.tree.insert(tarefa)
            if nova_descricao:
                tarefa.descricao = nova_descricao
            if nova_prioridade is not None:
                if tarefa.prioridade != nova_prioridade:
                    if tarefa.prioridade:
                        self.tarefas_prioritarias.remove(tarefa)
                    tarefa.prioridade = nova_prioridade
                    if nova_prioridade:
                        self.tarefas_prioritarias.append(tarefa)
            print(f"Tarefa '{nome}' editada.")
        else:
            print(f"Tarefa '{nome}' não encontrada.")

    def listar_tarefas(self):
        print("Todas as Tarefas:")
        tarefas = self.tree.inorder()
        for tarefa in tarefas:
            print(tarefa)
        return tarefas

    def marcar_concluida(self, nome):
        node = self.tree.search(nome)
        if node:
            node.key.concluida = True
            print(f"Tarefa '{nome}' marcada como concluída.")
        else:
            print(f"Tarefa '{nome}' não encontrada.")

    def navegar_tarefas_prioritarias(self):
        print("Tarefas Prioritárias:")
        tarefas = self.tarefas_prioritarias.traverse()
        for tarefa in tarefas:
            print(tarefa)


