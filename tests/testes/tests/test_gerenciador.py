"""
Testes unitários para o módulo GerenciadorTarefas.
Testa todas as operações CRUD e funcionalidades principais.
"""
import pytest
import os
import sys

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.gerenciador import ...
   from src.tarefa import ...


@pytest.fixture
def gerenciador_limpo():
    """
    Fixture que cria um gerenciador limpo para cada teste.
    Usa um arquivo temporário para não interferir nos dados reais.
    """
    arquivo_teste = "data/tarefas_teste.json"
    gerenciador = GerenciadorTarefas(arquivo_teste)
    gerenciador.tarefas = []  # Limpa qualquer tarefa existente
    gerenciador.proximo_id = 1
    yield gerenciador
    # Cleanup: remove arquivo de teste após cada teste
    if os.path.exists(arquivo_teste):
        os.remove(arquivo_teste)


class TestCriarTarefa:
    """Testes para a criação de tarefas."""
    
    def test_criar_tarefa_basica(self, gerenciador_limpo):
        """Testa criação de tarefa básica."""
        tarefa = gerenciador_limpo.criar_tarefa("Tarefa Teste")
        
        assert tarefa.id == 1
        assert tarefa.titulo == "Tarefa Teste"
        assert tarefa.status == "To Do"
        assert len(gerenciador_limpo.tarefas) == 1
    
    def test_criar_tarefa_com_descricao(self, gerenciador_limpo):
        """Testa criação de tarefa com descrição."""
        tarefa = gerenciador_limpo.criar_tarefa(
            "Tarefa Completa",
            "Descrição detalhada",
            "Alta"
        )
        
        assert tarefa.titulo == "Tarefa Completa"
        assert tarefa.descricao == "Descrição detalhada"
        assert tarefa.prioridade == "Alta"
    
    def test_criar_tarefa_incrementa_id(self, gerenciador_limpo):
        """Testa se o ID é incrementado automaticamente."""
        t1 = gerenciador_limpo.criar_tarefa("Tarefa 1")
        t2 = gerenciador_limpo.criar_tarefa("Tarefa 2")
        t3 = gerenciador_limpo.criar_tarefa("Tarefa 3")
        
        assert t1.id == 1
        assert t2.id == 2
        assert t3.id == 3
    
    def test_criar_tarefa_sem_titulo_falha(self, gerenciador_limpo):
        """Testa que criar tarefa sem título lança exceção."""
        with pytest.raises(ValueError):
            gerenciador_limpo.criar_tarefa("")
        
        with pytest.raises(ValueError):
            gerenciador_limpo.criar_tarefa("   ")


class TestListarTarefas:
    """Testes para listagem de tarefas."""
    
    def test_listar_tarefas_vazio(self, gerenciador_limpo):
        """Testa listagem quando não há tarefas."""
        tarefas = gerenciador_limpo.listar_tarefas()
        assert len(tarefas) == 0
    
    def test_listar_todas_tarefas(self, gerenciador_limpo):
        """Testa listagem de todas as tarefas."""
        gerenciador_limpo.criar_tarefa("Tarefa 1")
        gerenciador_limpo.criar_tarefa("Tarefa 2")
        gerenciador_limpo.criar_tarefa("Tarefa 3")
        
        tarefas = gerenciador_limpo.listar_tarefas()
        assert len(tarefas) == 3
    
    def test_filtrar_por_status(self, gerenciador_limpo):
        """Testa filtro por status."""
        gerenciador_limpo.criar_tarefa("Tarefa 1")
        gerenciador_limpo.criar_tarefa("Tarefa 2")
        gerenciador_limpo.atualizar_status(1, "In Progress")
        
        tarefas_todo = gerenciador_limpo.listar_tarefas(filtro_status="To Do")
        tarefas_progress = gerenciador_limpo.listar_tarefas(filtro_status="In Progress")
        
        assert len(tarefas_todo) == 1
        assert len(tarefas_progress) == 1
    
    def test_filtrar_por_prioridade(self, gerenciador_limpo):
        """Testa filtro por prioridade."""
        gerenciador_limpo.criar_tarefa("Tarefa Alta", prioridade="Alta")
        gerenciador_limpo.criar_tarefa("Tarefa Média", prioridade="Média")
        gerenciador_limpo.criar_tarefa("Tarefa Baixa", prioridade="Baixa")
        
        tarefas_alta = gerenciador_limpo.listar_tarefas(filtro_prioridade="Alta")
        tarefas_media = gerenciador_limpo.listar_tarefas(filtro_prioridade="Média")
        
        assert len(tarefas_alta) == 1
        assert len(tarefas_media) == 1
    
    def test_filtrar_status_e_prioridade(self, gerenciador_limpo):
        """Testa filtro combinado de status e prioridade."""
        gerenciador_limpo.criar_tarefa("T1", prioridade="Alta")
        gerenciador_limpo.criar_tarefa("T2", prioridade="Alta")
        gerenciador_limpo.atualizar_status(1, "Done")
        
        tarefas = gerenciador_limpo.listar_tarefas(
            filtro_status="Done",
            filtro_prioridade="Alta"
        )
        
        assert len(tarefas) == 1
        assert tarefas[0].titulo == "T1"


class TestBuscarTarefa:
    """Testes para busca de tarefas."""
    
    def test_buscar_tarefa_existente(self, gerenciador_limpo):
        """Testa busca de tarefa que existe."""
        gerenciador_limpo.criar_tarefa("Tarefa Teste")
        tarefa = gerenciador_limpo.buscar_tarefa(1)
        
        assert tarefa is not None
        assert tarefa.id == 1
        assert tarefa.titulo == "Tarefa Teste"
    
    def test_buscar_tarefa_inexistente(self, gerenciador_limpo):
        """Testa busca de tarefa que não existe."""
        tarefa = gerenciador_limpo.buscar_tarefa(999)
        assert tarefa is None


class TestAtualizarTarefa:
    """Testes para atualização de tarefas."""
    
    def test_atualizar_status_sucesso(self, gerenciador_limpo):
        """Testa atualização de status com sucesso."""
        gerenciador_limpo.criar_tarefa("Tarefa Teste")
        resultado = gerenciador_limpo.atualizar_status(1, "In Progress")
        
        assert resultado is True
        tarefa = gerenciador_limpo.buscar_tarefa(1)
        assert tarefa.status == "In Progress"
    
    def test_atualizar_status_tarefa_inexistente(self, gerenciador_limpo):
        """Testa atualização de status de tarefa inexistente."""
        resultado = gerenciador_limpo.atualizar_status(999, "Done")
        assert resultado is False
    
    def test_atualizar_prioridade_sucesso(self, gerenciador_limpo):
        """Testa atualização de prioridade com sucesso."""
        gerenciador_limpo.criar_tarefa("Tarefa Teste")
        resultado = gerenciador_limpo.atualizar_prioridade(1, "Alta")
        
        assert resultado is True
        tarefa = gerenciador_limpo.buscar_tarefa(1)
        assert tarefa.prioridade == "Alta"
    
    def test_atualizar_status_para_done_registra_data(self, gerenciador_limpo):
        """Testa que ao marcar como Done, registra data de conclusão."""
        gerenciador_limpo.criar_tarefa("Tarefa Teste")
        gerenciador_limpo.atualizar_status(1, "Done")
        
        tarefa = gerenciador_limpo.buscar_tarefa(1)
        assert tarefa.data_conclusao is not None


class TestDeletarTarefa:
    """Testes para deleção de tarefas."""
    
    def test_deletar_tarefa_sucesso(self, gerenciador_limpo):
        """Testa deleção de tarefa com sucesso."""
        gerenciador_limpo.criar_tarefa("Tarefa Teste")
        resultado = gerenciador_limpo.deletar_tarefa(1)
        
        assert resultado is True
        assert len(gerenciador_limpo.tarefas) == 0
    
    def test_deletar_tarefa_inexistente(self, gerenciador_limpo):
        """Testa deleção de tarefa inexistente."""
        resultado = gerenciador_limpo.deletar_tarefa(999)
        assert resultado is False
    
    def test_deletar_nao_afeta_outras_tarefas(self, gerenciador_limpo):
        """Testa que deletar uma tarefa não afeta outras."""
        gerenciador_limpo.criar_tarefa("Tarefa 1")
        gerenciador_limpo.criar_tarefa("Tarefa 2")
        gerenciador_limpo.criar_tarefa("Tarefa 3")
        
        gerenciador_limpo.deletar_tarefa(2)
        
        assert len(gerenciador_limpo.tarefas) == 2
        assert gerenciador_limpo.buscar_tarefa(1) is not None
        assert gerenciador_limpo.buscar_tarefa(2) is None
        assert gerenciador_limpo.buscar_tarefa(3) is not None


class TestPersistencia:
    """Testes para salvamento e carregamento de dados."""
    
    def test_salvar_e_carregar_tarefas(self, gerenciador_limpo):
        """Testa que tarefas são salvas e carregadas corretamente."""
        gerenciador_limpo.criar_tarefa("Tarefa 1", "Desc 1", "Alta")
        gerenciador_limpo.criar_tarefa("Tarefa 2", "Desc 2", "Baixa")
        
        # Cria novo gerenciador apontando para o mesmo arquivo
        arquivo = gerenciador_limpo.arquivo_dados
        gerenciador2 = GerenciadorTarefas(arquivo)
        
        assert len(gerenciador2.tarefas) == 2
        assert gerenciador2.tarefas[0].titulo == "Tarefa 1"
        assert gerenciador2.tarefas[1].prioridade == "Baixa"
    
    def test_proximo_id_persistido(self, gerenciador_limpo):
        """Testa que o próximo ID é persistido corretamente."""
        gerenciador_limpo.criar_tarefa("Tarefa 1")
        gerenciador_limpo.criar_tarefa("Tarefa 2")
        
        arquivo = gerenciador_limpo.arquivo_dados
        gerenciador2 = GerenciadorTarefas(arquivo)
        
        assert gerenciador2.proximo_id == 3


class TestEstatisticas:
    """Testes para estatísticas do sistema."""
    
    def test_estatisticas_vazio(self, gerenciador_limpo):
        """Testa estatísticas quando não há tarefas."""
        stats = gerenciador_limpo.obter_estatisticas()
        
        assert stats["total"] == 0
        assert stats["por_status"]["To Do"] == 0
        assert stats["por_status"]["In Progress"] == 0
        assert stats["por_status"]["Done"] == 0
    
    def test_estatisticas_completas(self, gerenciador_limpo):
        """Testa estatísticas com várias tarefas."""
        gerenciador_limpo.criar_tarefa("T1", prioridade="Alta")
        gerenciador_limpo.criar_tarefa("T2", prioridade="Alta")
        gerenciador_limpo.criar_tarefa("T3", prioridade="Média")
        gerenciador_limpo.criar_tarefa("T4", prioridade="Baixa")
        
        gerenciador_limpo.atualizar_status(1, "In Progress")
        gerenciador_limpo.atualizar_status(2, "Done")
        
        stats = gerenciador_limpo.obter_estatisticas()
        
        assert stats["total"] == 4
        assert stats["por_status"]["To Do"] == 2
        assert stats["por_status"]["In Progress"] == 1
        assert stats["por_status"]["Done"] == 1
        assert stats["por_prioridade"]["Alta"] == 2
        assert stats["por_prioridade"]["Média"] == 1
        assert stats["por_prioridade"]["Baixa"] == 1
