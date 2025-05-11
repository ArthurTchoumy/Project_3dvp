# 3DVP Project

## Description

API REST créée avec FastAPI. Elle permet de gérer des items avec des opérations CRUD.

## Endpoints

- `GET /items`
- `GET /items/{id}`
- `POST /items`
- `PUT /items/{id}`
- `DELETE /items/{id}`

## Tests

Lancer les tests avec :
```bash
pytest
```

## CI/CD

GitHub Actions est utilisé pour lancer les tests et le lint automatiquement.

## Déploiement

L'application est déployée automatiquement sur Render après chaque `push` sur `main`.