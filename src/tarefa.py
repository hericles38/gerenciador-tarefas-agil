from datetime import datetime

class Tarefa:
    PRIORIDADES_VALIDAS = ["Alta", "Média", "Baixa"]
    STATUS_VALIDOS = ["A Fazer", "Em Progresso", "Concluído"]

    def __init__(self, id, titulo, descricao="", prioridade="Média"):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade if prioridade in self.PRIORIDADES_VALIDAS else "Média"
        self.status = "A Fazer"
        self.data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data_conclusao = None

    def atualizar_status(self, novo_status):
        if novo_status in self.STATUS_VALIDOS:
            self.status = novo_status
            if novo_status == "Concluído" and self.data_conclusao is None:
                self.data_conclusao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        return False

    def atualizar_prioridade(self, nova_prioridade):
        if nova_prioridade in self.PRIORIDADES_VALIDAS:
            self.prioridade = nova_prioridade
            return True
        return False

    def to_dict(self):
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
        tarefa = cls(
            dados["id"],
            dados["titulo"],
            dados.get("descricao", ""),
            dados.get("prioridade", "Média")
        )
        tarefa.status = dados.get("status", "A Fazer")
        tarefa.data_criacao = dados.get("data_criacao", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        tarefa.data_conclusao = dados.get("data_conclusao")
        return tarefa

    def __str__(self):
        return f"[{self.id}] {self.titulo} | {self.status} | Prioridade: {self.prioridade}"

    def __repr__(self):
        return f"Tarefa(id={self.id}, titulo='{self.titulo}', status='{self.status}')"
