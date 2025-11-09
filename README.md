# 📋 Sistema de Gerenciamento de Tarefas Ágil

## Sobre o Projeto

Sistema de gerenciamento de tarefas desenvolvido para a **TechFlow Solutions**, aplicando metodologias ágeis para controle de fluxo de trabalho em tempo real. Projeto acadêmico da disciplina de Engenharia de Software.

## 🎯 Objetivo

Permitir que equipes possam:
- ✅ Criar e gerenciar tarefas
- 📊 Acompanhar status em tempo real
- 🎯 Priorizar atividades críticas
- 📈 Monitorar progresso da equipe

## 🚀 Metodologia Ágil Utilizada

**Kanban** - Sistema visual de gestão de trabalho com três colunas:
- 📝 **To Do** (A Fazer) - Tarefas pendentes
- ⚙️ **In Progress** (Em Progresso) - Tarefas sendo executadas
- ✅ **Done** (Concluído) - Tarefas finalizadas

### Por que Kanban?
- Visualização clara do fluxo de trabalho
- Flexibilidade para mudanças
- Limite de trabalho em progresso (WIP)
- Melhoria contínua do processo

## 🛠️ Tecnologias

- **Python 3.8+** - Linguagem principal
- **JSON** - Armazenamento de dados
- **Pytest** - Testes automatizados
- **GitHub Actions** - Integração contínua (CI/CD)
- **GitHub Projects** - Kanban visual

## 📦 Estrutura do Projeto

```
gerenciador-tarefas-agil/
│
├── src/
│   ├── gerenciador.py      # Classe principal do sistema
│   ├── tarefa.py            # Modelo de dados da tarefa
│   └── utils.py             # Funções auxiliares
│
├── tests/
│   ├── test_gerenciador.py  # Testes do gerenciador
│   └── test_tarefa.py       # Testes da tarefa
│
├── docs/
│   ├── diagrama_casos_uso.png
│   └── diagrama_classes.png
│
├── .github/
│   └── workflows/
│       └── tests.yml        # Pipeline CI/CD
│
├── data/
│   └── tarefas.json         # Banco de dados local
│
├── README.md
├── requirements.txt         # Dependências Python
└── .gitignore
```

## 🔧 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/hericles38/gerenciador-tarefas-agil.git

# Entre no diretório
cd gerenciador-tarefas-agil

# Instale as dependências
pip install -r requirements.txt

# Execute o sistema
python src/gerenciador.py
```

### Executar Testes

```bash
# Rodar todos os testes
pytest tests/

# Rodar com relatório de cobertura
pytest --cov=src tests/
```

## 📋 Funcionalidades

### CRUD Completo
- **Create** - Criar nova tarefa
- **Read** - Listar todas as tarefas
- **Update** - Atualizar status/dados da tarefa
- **Delete** - Remover tarefa

### Recursos Adicionais
- Filtrar tarefas por status
- Definir prioridade (Alta, Média, Baixa)
- Adicionar descrição detalhada
- Sistema de timestamps

## 🔄 Mudanças no Escopo

### Mudança Implementada: Sistema de Prioridades

**Data:** [09/11/2024]

**Justificativa:** Durante o desenvolvimento, identificamos através de reuniões com o cliente que equipes de logística frequentemente precisam diferenciar tarefas urgentes de atividades rotineiras. A ausência de um sistema de priorização estava gerando conflitos na ordem de execução das atividades. O Product Owner aprovou a implementação do sistema de prioridades (Alta, Média, Baixa) sem impacto no prazo de entrega do MVP.

**Impacto no Projeto:**
- Adição do atributo "prioridade" no modelo de dados Tarefa
- Implementação de 8 novos testes unitários específicos para prioridades
- Atualização da interface de criação e listagem de tarefas
- Novo filtro por prioridade no método listar_tarefas()
- Documentação atualizada no README.md

**Atualização no Kanban:**
A tarefa "Implementar sistema de prioridades" foi adicionada ao quadro e movida para "Done" após conclusão dos testes.
  

## 🧪 Controle de Qualidade

### Testes Automatizados
- **Testes Unitários** - Validação de funções individuais
- **Testes de Integração** - Validação do fluxo completo
- **Cobertura de Código** - Meta: >80%

### Pipeline CI/CD
O GitHub Actions executa automaticamente:
1. Instalação de dependências
2. Execução de todos os testes
3. Verificação de qualidade do código
4. Relatório de cobertura

## 👥 Contribuindo

Este é um projeto acadêmico, mas sugestões são bem-vindas!

1. Fork o projeto
2. Crie sua branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT.

## 👨‍💻 Autor

Desenvolvido como projeto da disciplina de Engenharia de Software.

**GitHub:** [@hericles38](https://github.com/hericles38)

---

⭐ Se este projeto te ajudou, deixe uma estrela!
