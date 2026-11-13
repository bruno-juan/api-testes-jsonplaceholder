# Testes automatizados da API JSONPlaceholder

Projeto de automação de testes de API, criado para praticar testes funcionais em um serviço público de exemplo. Cobre as operações do recurso `/posts`: listar, buscar, criar, atualizar e remover.

## Tecnologias

- Python 3 (somente biblioteca padrão: `unittest`, `urllib`, `json`)
- API alvo: [JSONPlaceholder](https://jsonplaceholder.typicode.com)

## Como rodar

```bash
git clone <url-do-repositorio>
cd api-testes-jsonplaceholder
python -m unittest discover -s tests -v
```

Não é preciso instalar dependências.

## O que é testado

| Operação | Cenário | Resultado esperado |
|---|---|---|
| GET /posts | Listagem | Status 200 e 100 posts |
| GET /posts | Estrutura dos dados | Cada post tem `id`, `title`, `body`, `userId` com os tipos corretos |
| GET /posts/{id} | Post existente | Status 200 |
| GET /posts/{id} | Post inexistente | Status 404 |
| POST /posts | Criação | Status 201, com `id` e os dados enviados |
| PUT /posts/{id} | Atualização | Status 200 com os dados alterados |
| DELETE /posts/{id} | Remoção | Status 200 |

## Observações

A API é um serviço de teste: ela aceita as requisições, mas não salva nada de verdade. Por isso, um POST retorna um novo `id`, mas o post não aparece depois numa listagem. Os testes levam isso em conta e checam só a resposta de cada operação.

Os achados sobre o comportamento da API estão em [BUGS.md](BUGS.md).
