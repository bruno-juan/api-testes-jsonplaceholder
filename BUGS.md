# Achados sobre o comportamento da API

Testes feitos manualmente em 2026-11-13 contra https://jsonplaceholder.typicode.com.

## 1. POST não persiste os dados

**Passos:** enviar `POST /posts` com um novo post.
**Esperado (para uma API real):** o post passa a existir e pode ser consultado depois.
**Obtido:** a API responde com status 201 e um `id` novo, mas `GET /posts/101` retorna 404.
**Observação:** pode ser o comportamento esperado de um serviço de teste. Vale registrar como limitação ao usar a API para testes de regressão.

## 2. PUT em post inexistente retorna 404

**Passos:** enviar `PUT /posts/9999`.
**Obtido:** 404, o que é coerente com o comportamento esperado.
**Observação:** confirmado, sem problema. Foi incluído para registrar que o caso foi verificado.

## 3. DELETE de post existente retorna 200

**Passos:** enviar `DELETE /posts/1`.
**Obtido:** 200, mas o post continua disponível em `GET /posts/1` nas requisições seguintes.
**Observação:** confirma o achado 1, já que a API não guarda alterações.
