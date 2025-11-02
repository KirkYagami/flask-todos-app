# Flask Todo App  
![Python](https://img.shields.io/badge/python-3.8%2B-blue)  
![Flask](https://img.shields.io/badge/flask-2.0%2B-green)  
![License](https://img.shields.io/badge/license-MIT-blue)

A **clean, modular, and production-ready** Todo application built with **Flask**, **SQLAlchemy**, **SQLite**, and **Bootstrap 5**. Features **full CRUD**, **singleton pattern** for config & logging, **custom error pages**, and **smart error handling**.

---

## Features

| Feature | Description |
|-------|-----------|
| **CRUD Operations** | Create, Read, Update, Delete todos |
| **SQLAlchemy ORM** | SQLite database with clean model |
| **Singleton Pattern** | One config, one logger — no duplicates |
| **Smart Logging** | Console + rotating file logs (`logs/app.log`) |
| **Custom Error Pages** | Beautiful 404 & 500 pages |
| **Flash Messages** | User feedback on actions |
| **Responsive UI** | Bootstrap 5 + clean cards |
| **Redirect on 404** | Invalid todo → redirect home with flash |
| **Blueprint Architecture** | Scalable and organized |

---

## Project Structure

```
todo_app/
├── app.py              # Main app factory
├── config.py           # Singleton: App configuration
├── logger.py           # Singleton: Rotating logger
├── models.py           # SQLAlchemy models
├── routes.py           # Blueprint: All routes + error handlers
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│   ├── 404.html
│   └── 500.html
├── logs/               # Auto-created: app.log
└── todos.db            # Auto-created: SQLite DB
```

---

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/yourname/flask-todo-app.git
cd flask-todo-app
```

```bash
pip install flask flask-sqlalchemy
```

### 2. Run the App

```bash
python app.py
```

Open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## How It Works

### Singleton Pattern

- **`Config()`**: One config instance → clean DB path, secret key
- **`Logger()`**: One logger → no duplicate handlers, rotating files

```python
config = Config()      # Always same instance
logger = Logger().get_logger()  # Always same logger
```

### Error Handling Strategy

| Error | Where Handled | Behavior |
|------|---------------|---------|
| Invalid URL (`/asdf`) | `app.py` | → `404.html` |
| Invalid Todo ID (`/edit/999`) | `routes.py` | → Flash + redirect home (`302`) |
| Server Crash | `app.py` | → `500.html` + DB rollback |

> **Blueprint 404 overrides app 404** when error is inside blueprint.

---

## Routes

| Route | Method | Action |
|------|--------|-------|
| `/` | GET | List all todos |
| `/add` | GET/POST | Add new todo |
| `/edit/<id>` | GET/POST | Edit todo |
| `/toggle/<id>` | GET | Toggle complete |
| `/delete/<id>` | GET | Delete todo |

---

## Database

- **SQLite**: `todos.db` in project root
- **Model**: `Todo(id, title, description, completed)`

Auto-created on first run.

---

## Logging

- **File**: `logs/app.log` (rotating, max 10MB, 5 backups)
- **Console**: Real-time feedback
- **Levels**: INFO, WARNING, ERROR

```log
2025-11-02 14:29:55 - TodoApp - INFO - Fetched all todos
2025-11-02 14:29:55 - TodoApp - WARNING - 404 Not Found: /edit/999
```

---

## Development Tips

### Test Redirects

```python
client = app.test_client()
resp = client.get('/edit/999')
assert resp.status_code == 302
assert 'text/html' in resp.headers['Content-Type']
```

### Add More Blueprints

```python
# api/routes.py
api_bp = Blueprint('api', __name__, url_prefix='/api')
app.register_blueprint(api_bp)
```

---

## Production Ready?

**Almost!** For production:

```bash
# Use Gunicorn + eventlet
gunicorn -w 4 -k eventlet "app:create_app()"
```

- Replace `debug=True` → `False`
- Use **PostgreSQL** in production
- Set `SECRET_KEY` via environment

---

## Contributing

1. Fork it
2. Create your feature branch
3. Commit changes
4. Push & open a Pull Request

---

## License

[MIT License](LICENSE) – Free to use, modify, and distribute.

---

## Made with Love

Built to teach **clean Flask architecture**, **singleton patterns**, and **smart error handling**.

> **Star this repo** if you learned something!

---

```bash
You just built a scalable Flask app. Now go deploy it!
```

---

**Happy Coding!**  
