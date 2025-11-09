"""
Testes unitários para o módulo tarefa.py
Testa a classe Tarefa e seus métodos.
"""
import pytest
import os
import sys

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.tarefa import Tarefa


class TestCriacaoTarefa:
    """Testes para criação de tarefas."""
    
    def test_criar_tarefa_basica(self):
        """Testa criação de tarefa com dados básicos."""
        tarefa = Tarefa(1, "Minha Tarefa")
        
        assert tarefa.id == 1
        assert tarefa.titulo == "Minha Tarefa"
        assert tarefa.status == "To Do"
        assert tarefa.prioridade == "Média"
        assert tarefa.descricao == ""
        assert tarefa.data_criacao is not None
        assert tarefa.data_conclusao is None
    
    def test_criar_tarefa_completa(self):
        """Testa criação de tarefa com todos os campos."""
        tarefa = Tarefa(
            id=5,
            titulo="Tarefa Completa",
            descricao="Descrição detalhada da tarefa",
            prioridade="Alta"
        )
        
        assert tarefa.id == 5
        assert tarefa.titulo == "Tarefa Completa"
        assert tarefa.descricao == "Descrição detalhada da tarefa"
        assert tarefa.prioridade == "Alta"
    
    def test_tarefa_inicia_com_status_to_do(self):
        """Testa que toda tarefa nova começa com status 'To Do'."""
        tarefa = Tarefa(1, "Teste")
        assert tarefa.status == "To Do"


class TestAtualizarStatus:
    """Testes para atualização de status."""
    
    def test_atualizar_para_in_progress(self):
        """Testa atualização de status para 'In Progress'."""
        tarefa = Tarefa(1, "Tarefa Teste")
        resultado = tarefa.atualizar_status("In Progress")
        
        assert resultado is True
        assert tarefa.status == "In Progress"
    
    def test_atualizar_para_done(self):
        """Testa atualização de status para 'Done'."""
        tarefa = Tarefa(1, "Tarefa Teste")
        resultado = tarefa.atualizar_status("Done")
        
        assert resultado is True
        assert tarefa.status == "Done"
        assert tarefa.data_conclusao is not None
    
    def test_atualizar_para_status_invalido(self):
        """Testa que status inválido não é aceito."""
        tarefa = Tarefa(1, "Tarefa Teste")
        resultado = tarefa.atualizar_status("Status Invalido")
        
        assert resultado is False
        assert tarefa.status == "To Do"  # Permanece no status original
    
    def test_data_conclusao_apenas_quando_done(self):
        """Testa que data_conclusao só é preenchida quando status é 'Done'."""
        tarefa = Tarefa(1, "Tarefa Teste")
        
        tarefa.atualizar_status("In Progress")
        assert tarefa.data_conclusao is None
        
        tarefa.atualizar_status("Done")
        assert tarefa.data_conclusao is not None
    
    def test_todos_status_validos(self):
        """Testa que todos os status válidos funcionam."""
        tarefa = Tarefa(1, "Tarefa Teste")
        
        assert tarefa.atualizar_status("To Do") is True
        assert tarefa.atualizar_status("In Progress") is True
        assert tarefa.atualizar_status("Done") is True


class TestAtualizarPrioridade:
    """Testes para atualização de prioridade."""
    
    def test_atualizar_para_alta(self):
        """Testa atualização de prioridade para 'Alta'."""
        tarefa = Tarefa(1, "Tarefa Teste")
        resultado = tarefa.atualizar_prioridade("Alta")
        
        assert resultado is True
        assert tarefa.prioridade == "Alta"
    
    def test_atualizar_para_baixa(self):
        """Testa atualização de prioridade para 'Baixa'."""
        tarefa = Tarefa(1, "Tarefa Teste")
        resultado = tarefa.atualizar_prioridade("Baixa")
        
        assert resultado is True
        assert tarefa.prioridade == "Baixa"
    
    def test_atualizar_para_prioridade_invalida(self):
        """Testa que prioridade inválida não é aceita."""
        tarefa = Tarefa(1, "Tarefa Teste", prioridade="Média")
        resultado = tarefa.atualizar_prioridade("Urgente")
        
        assert resultado is False
        assert tarefa.prioridade == "Média"  # Permanece na prioridade original
    
    def test_todas_prioridades_validas(self):
        """Testa que todas as prioridades válidas funcionam."""
        tarefa = Tarefa(1, "Tarefa Teste")
        
        assert tarefa.atualizar_prioridade("Alta") is True
        assert tarefa.atualizar_prioridade("Média") is True
        assert tarefa.atualizar_prioridade("Baixa") is True


class TestConversaoDicionario:
    """Testes para conversão de/para dicionário."""
    
    def test_to_dict(self):
        """Testa conversão de tarefa para dicionário."""
        tarefa = Tarefa(10, "Tarefa Teste", "Descrição teste", "Alta")
        dicionario = tarefa.to_dict()
        
        assert isinstance(dicionario, dict)
        assert dicionario["id"] == 10
        assert dicionario["titulo"] == "Tarefa Teste"
        assert dicionario["descricao"] == "Descrição teste"
        assert dicionario["status"] == "To Do"
        assert dicionario["prioridade"] == "Alta"
        assert "data_criacao" in dicionario
        assert "data_conclusao" in dicionario
    
    def test_from_dict(self):
        """Testa criação de tarefa a partir de dicionário."""
        dados = {
            "id": 20,
            "titulo": "Tarefa do Dict",
            "descricao": "Descrição do dict",
            "status": "In Progress",
            "prioridade": "Baixa",
            "data_criacao": "2024-01-01 10:00:00",
            "data_conclusao": None
        }
        
        tarefa = Tarefa.from_dict(dados)
        
        assert tarefa.id == 20
        assert tarefa.titulo == "Tarefa do Dict"
        assert tarefa.descricao == "Descrição do dict"
        assert tarefa.status == "In Progress"
        assert tarefa.prioridade == "Baixa"
        assert tarefa.data_criacao == "2024-01-01 10:00:00"
    
    def test_ciclo_completo_dict(self):
        """Testa conversão to_dict -> from_dict mantém dados."""
        tarefa_original = Tarefa(5, "Teste Ciclo", "Descrição", "Alta")
        tarefa_original.atualizar_status("In Progress")
        
        dicionario = tarefa_original.to_dict()
        tarefa_reconstruida = Tarefa.from_dict(dicionario)
        
        assert tarefa_reconstruida.id == tarefa_original.id
        assert tarefa_reconstruida.titulo == tarefa_original.titulo
        assert tarefa_reconstruida.descricao == tarefa_original.descricao
        assert tarefa_reconstruida.status == tarefa_original.status
        assert tarefa_reconstruida.prioridade == tarefa_original.prioridade


class TestRepresentacaoString:
    """Testes para representações em string."""
    
    def test_str_representation(self):
        """Testa método __str__."""
        tarefa = Tarefa(1, "Tarefa Teste", prioridade="Alta")
        string = str(tarefa)
        
        assert "1" in string
        assert "Tarefa Teste" in string
        assert "To Do" in string
        assert "Alta" in string
    
    def test_repr_representation(self):
        """Testa método __repr__."""
        tarefa = Tarefa(1, "Tarefa Teste")
        repr_string = repr(tarefa)
        
        assert "Tarefa" in repr_string
        assert "id=1" in repr_string
        assert "Tarefa Teste" in repr_string


class TestValidacaoDados:
    """Testes de validação de dados."""
    
    def test_diferentes_ids(self):
        """Testa que tarefas podem ter IDs diferentes."""
        t1 = Tarefa(1, "Tarefa 1")
        t2 = Tarefa(100, "Tarefa 2")
        t3 = Tarefa(999, "Tarefa 3")
        
        assert t1.id == 1
        assert t2.id == 100
        assert t3.id == 999
    
    def test_titulo_vazio_permitido_na_classe(self):
        """Testa que a classe Tarefa permite título vazio (validação é no gerenciador)."""
        tarefa = Tarefa(1, "")
        assert tarefa.titulo == ""
    
    def test_descricao_opcional(self):
        """Testa que descrição é opcional."""
        tarefa = Tarefa(1, "Teste")
        assert tarefa.descricao == ""
        
        tarefa2 = Tarefa(2, "Teste", "Com descrição")
        assert tarefa2.descricao == "Com descrição"


class TestFluxoCompleto:
    """Testes de fluxo completo de uma tarefa."""
    
    def test_ciclo_vida_tarefa(self):
        """Testa o ciclo de vida completo de uma tarefa."""
        # Criação
        tarefa = Tarefa(1, "Implementar funcionalidade", "Descrição detalhada", "Alta")
        assert tarefa.status == "To Do"
        assert tarefa.data_conclusao is None
        
        # Em progresso
        tarefa.atualizar_status("In Progress")
        assert tarefa.status == "In Progress"
        assert tarefa.data_conclusao is None
        
        # Alteração de prioridade
        tarefa.atualizar_prioridade("Média")
        assert tarefa.prioridade == "Média"
        
        # Conclusão
        tarefa.atualizar_status("Done")
        assert tarefa.status == "Done"
        assert tarefa.data_conclusao is not None
