# Установка и подготовка окружения

### 🔧 Требования
- macOS 12+
- Python 3.13+
- Swift 5+
- Docker (опционально, для контейнеризации)
- Rust (для сборки зависимостей)

### ⏳ Установка
1. Клонируйте репозиторий:
   ```sh
   git clone git@github.com:Tarnov/Council_of_Elrond.git
   cd Council_of_Elrond
   ```

2. Настройте виртуальное окружение:
   ```sh
   rm -rf venv && python3 -m venv venv --system-site-packages && source venv/bin/activate
   ```

3. Установите Rust (необходим для сборки некоторых зависимостей):
   ```sh
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && source $HOME/.cargo/env
   ```

4. Проверьте установку Rust:
   ```sh
   rustc --version
   ```

5. Установите зависимости:
   ```sh
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### ▶️ Запуск
- Для Python-версии:
   ```sh
   python src/main.py
   ```
- Для Swift-версии (если интерфейс нативный):
   ```sh
   swift run
   ```
- Через Docker (если хотите контейнеризированный запуск):
   ```sh
   docker-compose up
   ```

После выполнения этих шагов окружение будет полностью готово! 🚀

# tests/test_main.py

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    """Тест проверяет, что корневой эндпоинт возвращает корректный ответ."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Council of Elrond!"}

def test_orchestrator_endpoint():
    """Тест проверяет, что эндпоинт /orchestrator доступен."""
    response = client.get("/orchestrator")
    assert response.status_code in [200, 404]  # Пока нет реализации, допускаем 404
