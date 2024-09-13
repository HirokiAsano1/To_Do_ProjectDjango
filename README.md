# Django To-do List

Este é um projeto de To-do List construído com Django, que permite ao usuário adicionar, editar, excluir e marcar tarefas como concluídas. O sistema ordena as tarefas pela data de entrega e inclui a possibilidade de acompanhar o progresso das tarefas.

## Funcionalidades

- **Adicionar Tarefas**: Crie novas tarefas com título e data de entrega.
- **Editar Tarefas**: Atualize informações das tarefas existentes.
- **Excluir Tarefas**: Remova tarefas da lista.
- **Marcar como Concluída**: Ao marcar uma tarefa como concluída, a data de finalização é automaticamente registrada.
- **Ordenação por Data de Entrega**: As tarefas são exibidas em ordem de prioridade com base na data de entrega.

## Estrutura dos Atributos

- **Título**: Descrição da tarefa.
- **Criado em**: Data em que a tarefa foi criada.
- **Data de Entrega**: Prazo para concluir a tarefa.
- **Finalizado em**: Data em que a tarefa foi marcada como concluída (preenchido automaticamente).

## Rotas (URLs)

- `/`: Página inicial, onde todas as tarefas são listadas.
- `/create`: Página para adicionar uma nova tarefa.
- `/update/<id>`: Página para editar uma tarefa existente.
- `/delete/<id>`: Endpoint para deletar uma tarefa.
- `/complete/<id>`: Endpoint para marcar uma tarefa como concluída.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para o desenvolvimento do back-end.
- **HTML/CSS**: Utilizado para a criação do front-end.
- **SQLite**: Banco de dados padrão do Django.

## Como Rodar o Projeto

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/django-todo-list.git
2. Acesse a pasta do projeto:

   ```bash
   cd django-todo-list
   
3. Crie um ambiente virtual:

   ```bash
   python -m venv venv

4. Ative o ambiente virtual:

   ```bash
   venv\Scripts\activate

5. Instale as dependências:

   ```bash
   pip install -r requirements.txt

6. python manage.py migrate

   ```bash
   python manage.py migrate

7. Inicie o servidor:
   
   ```bash
   python manage.py runserver

8. Acesse a aplicação em http://127.0.0.1:8000.
