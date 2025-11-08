
"""
Módulo que define o modelo de dados para uma Tarefa.
"""
from datetime import datetime


class Tarefa:
    """
    Classe que representa uma tarefa no sistema de gerenciamento.
    
    Atributos:
        id (int): Identificador único da tarefa
        titulo (str): Título da tarefa
        descricao (str): Descrição detalhada da tarefa
        status (str): Status atual (To Do, In Progress, Done)
        prioridade (str): Prioridade (Alta, Média, Baixa)
        data_criacao (str): Data de criação da tarefa
        data_conclusao (str): Data de conclusão (se concluída)
    """
    
    def __init__(self, id, titulo, descricao="", prioridade="Média"):
        """
        Inicializa uma nova tarefa.
        
        Args:
            id (int): Identificador único
            titulo (str): Título da tarefa
            descricao (str): Descrição da tarefa
            prioridade (str): Prioridade (Alta, Média, Baixa)
        """
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = "To Do"
        self.prioridade = prioridade
        self.data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data_conclusao = None
    
    def atualizar_status(self, novo_status):
        """
        Atualiza o status da tarefa.
        
        Args:
            novo_status (str): Novo status (To Do, In Progress, Done)
        
        Returns:
            bool: True se atualizado com sucesso
        """
        status_validos = ["To Do", "In Progress", "Done"]
        if novo_status in status_validos:
            self.status = novo_status
            if novo_status == "Done":
                self.data_conclusao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        return False
    
    def atualizar_prioridade(self, nova_prioridade):
        """
        Atualiza a prioridade da tarefa.
        
        Args:
            nova_prioridade (str): Nova prioridade (Alta, Média, Baixa)
        
        Returns:
            bool: True se atualizado com sucesso
        """
        prioridades_validas = ["Alta", "Média", "Baixa"]
        if nova_prioridade in prioridades_validas:
            self.prioridade = nova_prioridade
            return True
        return False
    
    def to_dict(self):
        """
        Converte a tarefa para dicionário.
        
        Returns:
            dict: Dicionário com os dados da tarefa
        """
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "prioridade": self.prioridade,
            "data_criacao": self.data_criacao,
            "data_conclusao": self.data_conclusao
        }
    
    @staticmethod
    def from_dict(data):
        """
        Cria uma tarefa a partir de um dicionário.
        
        Args:
            data (dict): Dicionário com dados da tarefa
        
        Returns:
            Tarefa: Objeto Tarefa criado
        """
        tarefa = Tarefa(
            id=data["id"],
            titulo=data["titulo"],
            descricao=data.get("descricao", ""),
            prioridade=data.get("prioridade", "Média")
        )
        tarefa.status = data.get("status", "To Do")
        tarefa.data_criacao = data.get("data_criacao")
        tarefa.data_conclusao = data.get("data_conclusao")
        return tarefa
    
    def __str__(self):
        """Representação em string da tarefa."""
        return f"[{self.id}] {self.titulo} - {self.status} - Prioridade: {self.prioridade}"
    
    def __repr__(self):
        """Representação para debug."""
        return f"Tarefa(id={self.id}, titulo='{self.titulo}', status='{self.status}')"
