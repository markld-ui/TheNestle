// ...existing code...
# TheNestle — Полный стек (Backend + Frontend)

Монорепозиторий проекта TheNestle: FastAPI-бэкенд и SPA-фронтенд. Предназначен для запуска локально в режиме разработки и в контейнерах через Docker / Docker Compose для production.

## Кратко
- Backend: FastAPI, Uvicorn, PostgreSQL, Alembic (миграции)
- Frontend: React (Vite) / TypeScript (или выбранный стек), CSS-фреймворк (Tailwind/Bootstrap) по желанию
- Контейнеризация: Docker + Docker Compose
- Тесты: pytest на бекенде, jest/vitest на фронтенде (если настроено)

## Стек технологий
- Backend: Python 3.11+, FastAPI, SQLAlchemy / databases, Alembic, Uvicorn
- Frontend: React + Vite, TypeScript (рекомендуется), axios / fetch, Tailwind / CSS
- DB: PostgreSQL
- Dev: Docker, docker-compose, pytest, httpx (интеграционные тесты)

## Быстрый старт (Docker Compose)
1. Скопировать пример env-файлов:
   cp .env.example .env
   cp frontend/.env.example frontend/.env
2. Настроить значения (DATABASE_URL, VITE_API_URL, SECRET_KEY и т.д.)
3. Запустить все сервисы:
   docker compose up --build
4. Открыть в браузере:
   - Фронтенд: http://localhost:3000 (или порт, указанный в docker-compose)
   - API docs: http://localhost:1221/docs
   - Health: http://localhost:1221/health

В фоне:
   docker compose up -d --build

Остановить и удалить:
   docker compose down

## Backend (существенное)
- Запуск локально:
   python -m venv .venv
   .venv\Scripts\activate  (Windows)
   source .venv/bin/activate  (Linux/macOS)
   pip install -r requirements-dev.txt
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
- Миграции:
   alembic revision --autogenerate -m "описание"
   alembic upgrade head
- Основные эндпойнты:
   - GET /health — простой healthcheck
   - GET /ready — readiness (проверка БД)

## Frontend (существенное)
- Переменные окружения: frontend/.env (пример .env.example)
  - VITE_API_URL=http://localhost:8000/api
- Локальная разработка (пример для npm):
   cd frontend
   npm install
   npm run dev
- Сборка для продакшн:
   npm run build
- Запуск собранного фронтенда в Docker:
   - В docker-compose обычно_service `web` собирает фронтенд-статические файлы и отдаёт через nginx или встроенный static-server.

## Переменные окружения (пример)
Backend:
- DATABASE_URL=postgresql://user:pass@db:5432/the_nestle
- FASTAPI_ENV=production|development
- SECRET_KEY=изменить_на_секрет
- PORT=8000
- WORKERS=2

Frontend (frontend/.env):
- VITE_API_URL=http://localhost:8000

## Docker / Docker Compose (рекомендации)
- docker-compose.yml должен определять минимум сервисов:
  - api — бекенд (build из /backend)
  - web — фронтенд (build из /frontend или отдача статичных файлов через nginx)
  - db — postgres
  - optional: migrate (выполнение alembic при старте)
- В production используйте multi-stage Dockerfile для фронтенда и бекенда.

## Локальная разработка (совместно)
- Запуск бекенда локально и фронтенда через Vite: фронтенд должен направлять запросы на VITE_API_URL (proxy при dev).
- Для интеграционных тестов можно поднять docker-compose с тестовой БД и запускать pytest с переменной окружения TEST_DATABASE_URL.

## Тестирование
- Backend: pytest, httpx для тестовых запросов
- Frontend: jest/vitest (в зависимости от стека)
Запуск:
   pytest
   npm test (в фронтенде)

## CI / CD
- Шаги: lint -> test -> build -> migrate -> deploy
- В CI: использовать отдельную тестовую БД, кеширование зависимостей и multi-stage сборку образов.

## Форматирование и линтинг
- Backend: black, isort, flake8
- Frontend: prettier, eslint
Примеры:
   black .
   isort .
   flake8
   npm run lint (во frontend)

## Структура проекта (пример)
- backend/  (или app/)
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
- frontend/
  - package.json
  - src/
  - public/
  - Dockerfile
- docker-compose.yml
- .env.example
- requirements.txt
- README.md
- LICENSE

## Рекомендации по безопасности
- Не хранить секреты в репозитории
- Использовать секреты Docker / переменные окружения на CI/CD
- Ограничить CORS и включить HTTPs в продакшне (reverse-proxy)

## Вклад
- Использовать ветвевую стратегию (GitFlow/feature-branches)
- Писать тесты для новых фич
- Малые и осмысленные PR

## Лицензия
Указать лицензию в файле LICENSE репозитория.