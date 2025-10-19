# TheNestle — Backend

FastAPI-бэкенд для проекта TheNestle. Проект рассчитан на запуск в Docker (production) и локально для разработки. Предоставляет REST API с документацией OpenAPI, миграции БД и готовые настройки для контейнеризации.

## Стек технологий
- Python 3.11+
- FastAPI
- Uvicorn (ASGI)
- SQLAlchemy / databases / Alembic
- PostgreSQL (production)
- Docker & Docker Compose
- Pytest, httpx для тестов

## Возможности
- JSON REST API с автогенерируемой документацией (/docs, /redoc)
- Миграции через Alembic
- Контейнеризация через Docker + Compose
- Health и readiness endpoints
- Конфигурация через переменные окружения

## Требования
- Docker >= 20.x
- Docker Compose (v2) или встроенный compose в Docker CLI
- (опционально) Python 3.11, pip, virtualenv для локальной разработки

## Быстрый старт (Docker Compose)
1. Скопировать пример env:
   cp .env.example .env
2. Отредактировать `.env` (DATABASE_URL, SECRET_KEY и т.д.).
3. Запустить сервисы:
   docker compose up --build
4. Открыть в браузере:
   - Документация: http://localhost:8000/docs
   - OpenAPI JSON: http://localhost:8000/openapi.json
   - Health: http://localhost:8000/health

Запустить в фоне:
   docker compose up -d --build

Остановить и удалить контейнеры:
   docker compose down

## Запуск одного контейнера (Docker)
Сборка образа:
   docker build -t thenestle-backend:latest .

Пример запуска:
   docker run --env-file .env -p 8000:8000 thenestle-backend:latest

## Переменные окружения (пример)
Рекомендуется иметь `.env.example` в репозитории:
- DATABASE_URL=postgresql://user:pass@db:5432/the_nestle
- FASTAPI_ENV=production|development
- SECRET_KEY=изменить_на_секрет
- PORT=8000
- WORKERS=2

## База данных и миграции
- Миграции управляются Alembic.
- Создать ревизию:
   alembic revision --autogenerate -m "описание"
- Применить миграции:
   alembic upgrade head

В Compose миграции обычно выполняются через entrypoint-скрипт или через Makefile (`make migrate`).

## Локальная разработка
Windows (cmd/powershell):
   python -m venv .venv
   .venv\Scripts\activate
Linux/macOS:
   python -m venv .venv
   source .venv/bin/activate

Установка зависимостей:
   pip install -r requirements-dev.txt

Запуск приложения в режиме разработки:
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

## Тестирование
Запуск тестов:
   pytest

Используйте отдельную тестовую БД (переменные окружения) чтобы не повредить данные продакшна.

## Форматирование и линтинг
- Форматирование: black, isort
- Линтинг: flake8

Примеры:
   black .
   isort .
   flake8

## Healthcheck и Readiness
Рекомендуется иметь минимальные эндпойнты:
- GET /health — возвращает 200 OK
- GET /ready — проверяет доступность БД и других зависимостей

## Логирование и мониторинг
- В production рекомендуется структурированное логирование (JSON).
- При необходимости — экспорт метрик Prometheus.

## Структура проекта (пример)
- app/
  - main.py
  - api/
  - core/
  - models/
  - schemas/
  - crud/
  - db/
  - tests/
- alembic/
- Dockerfile
- docker-compose.yml
- .env.example
- requirements.txt

## CI / CD
Рекомендации:
- Сборка образа, запуск тестов, применение миграций, деплой
- Мультистадийный Dockerfile для уменьшения размера образа
- Сканы безопасности зависимостей и образов

## Вклад и правила
- Следовать принятой ветвевой стратегии (GitFlow или аналог)
- Добавлять тесты для новых фич
- Держать PR небольшими и сфокусированными

## Лицензия
Указать лицензию в файле LICENSE репозитория.