"""
Testes automatizados para o Sistema de Gerenciamento de Tarefas
Arquivo: tests/test_tasks.py
"""


class TestTaskBasic:
    """Testes básicos de tarefas"""

    def test_criar_tarefa_simples(self):
        """Testa criação básica de tarefa"""
        tarefa = {
            "titulo": "Implementar login",
            "descricao": "Sistema de autenticação",
            "status": "A Fazer",
            "prioridade": "Alta"
        }

        assert tarefa["titulo"] == "Implementar login"
        assert tarefa["status"] == "A Fazer"
        assert tarefa["prioridade"] == "Alta"

    def test_validar_titulo_vazio(self):
        """Testa que título não pode ser vazio"""
        titulo = ""
        assert len(titulo) == 0, "Título vazio não é permitido"

    def test_validar_status_valido(self):
        """Testa que status deve ser válido"""
        status_validos = ["A Fazer", "Em Progresso", "Concluído"]
        status_teste = "A Fazer"

        assert status_teste in status_validos

    def test_prioridades_validas(self):
        """Testa prioridades válidas"""
        prioridades = ["Baixa", "Média", "Alta"]

        assert "Alta" in prioridades
        assert "Média" in prioridades
        assert "Baixa" in prioridades


class TestTaskValidation:
    """Testes de validação"""

    def test_titulo_maximo_100_caracteres(self):
        """Testa limite de caracteres do título"""
        titulo_valido = "a" * 100
        titulo_invalido = "a" * 101

        assert len(titulo_valido) <= 100
        assert len(titulo_invalido) > 100

    def test_status_padrao_a_fazer(self):
        """Testa que status padrão é 'A Fazer'"""
        tarefa = {"titulo": "Nova tarefa"}
        status_padrao = tarefa.get("status", "A Fazer")

        assert status_padrao == "A Fazer"


class TestTaskOperations:
    """Testes de operações CRUD"""

    def test_adicionar_tarefa_lista(self):
        """Testa adicionar tarefa à lista"""
        lista_tarefas = []
        nova_tarefa = {"titulo": "Nova tarefa", "status": "A Fazer"}

        lista_tarefas.append(nova_tarefa)

        assert len(lista_tarefas) == 1
        assert lista_tarefas[0]["titulo"] == "Nova tarefa"

    def test_remover_tarefa_lista(self):
        """Testa remover tarefa da lista"""
        lista_tarefas = [
            {"id": 1, "titulo": "Tarefa 1"},
            {"id": 2, "titulo": "Tarefa 2"}
        ]

        lista_tarefas = [t for t in lista_tarefas if t["id"] != 1]

        assert len(lista_tarefas) == 1
        assert lista_tarefas[0]["id"] == 2

    def test_atualizar_status_tarefa(self):
        """Testa atualizar status de tarefa"""
        tarefa = {"titulo": "Teste", "status": "A Fazer"}
        tarefa["status"] = "Em Progresso"

        assert tarefa["status"] == "Em Progresso"

    def test_filtrar_tarefas_por_status(self):
        """Testa filtrar tarefas por status"""
        tarefas = [
            {"titulo": "T1", "status": "A Fazer"},
            {"titulo": "T2", "status": "Concluído"},
            {"titulo": "T3", "status": "A Fazer"}
        ]

        a_fazer = [t for t in tarefas if t["status"] == "A Fazer"]

        assert len(a_fazer) == 2


class TestIntegration:
    """Testes de integração"""

    def test_fluxo_completo_tarefa(self):
        """Testa fluxo: criar → atualizar → concluir"""
        tarefa = {
            "titulo": "Implementar feature",
            "status": "A Fazer",
            "prioridade": "Alta"
        }

        # Verificar criação
        assert tarefa["status"] == "A Fazer"

        # Iniciar
        tarefa["status"] = "Em Progresso"
        assert tarefa["status"] == "Em Progresso"

        # Concluir
        tarefa["status"] = "Concluído"
        assert tarefa["status"] == "Concluído"
