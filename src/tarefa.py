"""
Módulo que define a classe Tarefa.
Representa uma tarefa individual no sistema de gerenciamento.
"""
from datetime import datetime


class Tarefa:
    """
    Classe que representa uma tarefa no sistema Kanban.

    Atributos:
    id (int): Identificador único da tarefa
    titulo (str): Título da tarefa
    descricao (str): Descrição detalhada
    prioridade (str): Prioridade (Alta, Média, Baixa)
    status (str): Status atual (To Do, In Progress, Done)
    data_criacao (str): Data de criação da tarefa
    """

    PRIORIDADES_VALIDAS = ["Alta", "Média", "Baixa"]
    STATUS_VALIDOS = ["To Do", "In Progress", "Done"]

    def __init__(self, id, titulo, descricao="", prioridade="Média"):
        """
        Inicializa uma nova tarefa.

        Args:
            id (int): ID único da tarefa
            titulo (str): Título da tarefa
            descricao (str): Descrição da tarefa
            prioridade (str): Prioridade da tarefa
        """
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade if prioridade in self.PRIORIDADES_VALIDAS else "Média"
        self.status = "To Do"
        self.data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data_conclusao = None

    def atualizar_status(self, novo_status):
        """
        Atualiza o status da tarefa.

        Args:
            novo_status (str): Novo status

        Returns:
            bool: True se atualizado com sucesso
        """
        if novo_status in self.STATUS_VALIDOS:
            self.status = novo_status
            # Se marcar como concluído, registra data
            if novo_status == "Done" and self.data_conclusao is None:
                self.data_conclusao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        return False

    # --- MÉTODO ADICIONADO PARA CORRIGIR O ATTRIBUTE ERROR ---
    def atualizar_prioridade(self, nova_prioridade):
        """
        Atualiza a prioridade da tarefa.

        Args:
            nova_prioridade (str): Nova prioridade

        Returns:
            bool: True se atualizado com sucesso
        """
        if nova_prioridade in self.PRIORIDADES_VALIDAS:
            self.prioridade = nova_prioridade
            return True
        return False
    # ---------------------------------------------------------

    def to_dict(self):
        """
        Converte a tarefa para dicionário (para salvar em JSON).

        Returns:
            dict: Dicionário com dados da tarefa
        """
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "status": self.status,
            "data_criacao": self.data_criacao,
            "data_conclusao": self.data_conclusao
        }

    @classmethod
    def from_dict(cls, dados):
        """
        Cria uma tarefa a partir de um dicionário.

        Args:
            dados (dict): Dicionário com dados da tarefa

        Returns:
            Tarefa: Nova instância de Tarefa
        """
        tarefa = cls(
            dados["id"],
            dados["titulo"],
            dados.get("descricao", ""),
            dados.get("prioridade", "Média")
        )
        tarefa.status = dados.get("status", "To Do")
        tarefa.data_criacao = dados.get("data_criacao", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        tarefa.data_conclusao = dados.get("data_conclusao")
        return tarefa

    def __str__(self):
        """Representação em string da tarefa."""
        return f"[{self.id}] {self.titulo} | {self.status} | Prioridade: {self.prioridade}"

    def __repr__(self):
        """Representação técnica da tarefa."""
        return f"Tarefa(id={self.id}, titulo='{self.titulo}', status='{self.status}')"
