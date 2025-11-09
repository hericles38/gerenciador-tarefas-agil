"""
Módulo principal do sistema de gerenciamento de tarefas.
Implementa operações CRUD (Create, Read, Update, Delete).
"""
import json
import os
from src.tarefa import Tarefa

class GerenciadorTarefas:
    """
    Classe responsável por gerenciar todas as operações com tarefas.
    
    Atributos:
        tarefas (list): Lista de tarefas do sistema
        arquivo_dados (str): Caminho do arquivo de persistência
        proximo_id (int): Próximo ID disponível para nova tarefa
    """
    
    def __init__(self, arquivo_dados="data/tarefas.json"):
        """
        Inicializa o gerenciador de tarefas.
        
        Args:
            arquivo_dados (str): Caminho do arquivo JSON para persistência
        """
        self.tarefas = []
        self.arquivo_dados = arquivo_dados
        self.proximo_id = 1
        self._criar_diretorio_dados()
        self.carregar_tarefas()
    
    def _criar_diretorio_dados(self):
        """Cria o diretório de dados se não existir."""
        diretorio = os.path.dirname(self.arquivo_dados)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio)
    
    def criar_tarefa(self, titulo, descricao="", prioridade="Média"):
        """
        Cria uma nova tarefa (CREATE).
        
        Args:
            titulo (str): Título da tarefa
            descricao (str): Descrição da tarefa
            prioridade (str): Prioridade (Alta, Média, Baixa)
        
        Returns:
            Tarefa: Tarefa criada
        """
        if not titulo or titulo.strip() == "":
            raise ValueError("O título da tarefa não pode ser vazio")
        
        tarefa = Tarefa(self.proximo_id, titulo, descricao, prioridade)
        self.tarefas.append(tarefa)
        self.proximo_id += 1
        self.salvar_tarefas()
        return tarefa
    
    def listar_tarefas(self, filtro_status=None, filtro_prioridade=None):
        """
        Lista todas as tarefas com filtros opcionais (READ).
        
        Args:
            filtro_status (str): Filtrar por status (opcional)
            filtro_prioridade (str): Filtrar por prioridade (opcional)
        
        Returns:
            list: Lista de tarefas filtradas
        """
        tarefas_filtradas = self.tarefas
        
        if filtro_status:
            tarefas_filtradas = [t for t in tarefas_filtradas if t.status == filtro_status]
        
        if filtro_prioridade:
            tarefas_filtradas = [t for t in tarefas_filtradas if t.prioridade == filtro_prioridade]
        
        return tarefas_filtradas
    
    def buscar_tarefa(self, id_tarefa):
        """
        Busca uma tarefa pelo ID.
        
        Args:
            id_tarefa (int): ID da tarefa
        
        Returns:
            Tarefa: Tarefa encontrada ou None
        """
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                return tarefa
        return None
    
    def atualizar_status(self, id_tarefa, novo_status):
        """
        Atualiza o status de uma tarefa (UPDATE).
        
        Args:
            id_tarefa (int): ID da tarefa
            novo_status (str): Novo status
        
        Returns:
            bool: True se atualizado com sucesso
        """
        tarefa = self.buscar_tarefa(id_tarefa)
        if tarefa:
            if tarefa.atualizar_status(novo_status):
                self.salvar_tarefas()
                return True
        return False
    
    def atualizar_prioridade(self, id_tarefa, nova_prioridade):
        """
        Atualiza a prioridade de uma tarefa (UPDATE).
        
        Args:
            id_tarefa (int): ID da tarefa
            nova_prioridade (str): Nova prioridade
        
        Returns:
            bool: True se atualizado com sucesso
        """
        tarefa = self.buscar_tarefa(id_tarefa)
        if tarefa:
            if tarefa.atualizar_prioridade(nova_prioridade):
                self.salvar_tarefas()
                return True
        return False
    
    def deletar_tarefa(self, id_tarefa):
        """
        Deleta uma tarefa (DELETE).
        
        Args:
            id_tarefa (int): ID da tarefa a ser deletada
        
        Returns:
            bool: True se deletada com sucesso
        """
        tarefa = self.buscar_tarefa(id_tarefa)
        if tarefa:
            self.tarefas.remove(tarefa)
            self.salvar_tarefas()
            return True
        return False
    
    def salvar_tarefas(self):
        """Salva todas as tarefas no arquivo JSON."""
        try:
            with open(self.arquivo_dados, 'w', encoding='utf-8') as arquivo:
                dados = {
                    "proximo_id": self.proximo_id,
                    "tarefas": [t.to_dict() for t in self.tarefas]
                }
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar tarefas: {e}")
    
    def carregar_tarefas(self):
        """Carrega as tarefas do arquivo JSON."""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    self.proximo_id = dados.get("proximo_id", 1)
                    self.tarefas = [Tarefa.from_dict(t) for t in dados.get("tarefas", [])]
            except Exception as e:
                print(f"Erro ao carregar tarefas: {e}")
                self.tarefas = []
    
    def obter_estatisticas(self):
        """
        Retorna estatísticas sobre as tarefas.
        
        Returns:
            dict: Dicionário com estatísticas
        """
        total = len(self.tarefas)
        por_status = {
            "To Do": len([t for t in self.tarefas if t.status == "To Do"]),
            "In Progress": len([t for t in self.tarefas if t.status == "In Progress"]),
            "Done": len([t for t in self.tarefas if t.status == "Done"])
        }
        por_prioridade = {
            "Alta": len([t for t in self.tarefas if t.prioridade == "Alta"]),
            "Média": len([t for t in self.tarefas if t.prioridade == "Média"]),
            "Baixa": len([t for t in self.tarefas if t.prioridade == "Baixa"])
        }
        
        return {
            "total": total,
            "por_status": por_status,
            "por_prioridade": por_prioridade
        }


# Exemplo de uso (para testar manualmente)
if __name__ == "__main__":
    print("=== Sistema de Gerenciamento de Tarefas ===\n")
    
    gerenciador = GerenciadorTarefas()
    
    # Criar algumas tarefas de exemplo
    t1 = gerenciador.criar_tarefa("Configurar ambiente", "Instalar Python e dependências", "Alta")
    t2 = gerenciador.criar_tarefa("Criar modelos", "Implementar classes principais", "Alta")
    t3 = gerenciador.criar_tarefa("Escrever testes", "Criar testes unitários", "Média")
    
    print("Tarefas criadas:")
    for tarefa in gerenciador.listar_tarefas():
        print(f"  {tarefa}")
    
    print("\n=== Estatísticas ===")
    stats = gerenciador.obter_estatisticas()
    print(f"Total de tarefas: {stats['total']}")
    print(f"Por status: {stats['por_status']}")
    print(f"Por prioridade: {stats['por_prioridade']}")
