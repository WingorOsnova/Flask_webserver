# Flask Webserver — Mini Blog

This is a simple Flask + SQLite mini blog with post creation, a home page with latest posts, and basic login/registration. Admin users can delete posts.

- Languages: English • Deutsch • Русский
- Default admin credentials (for local use):
  - Username: `admin`
  - Password: `admin123`
  - Do not use these in production.

## English

Overview
- Mini blog built with Flask and SQLite.
- Home page shows a horizontal slider of the latest posts.
- All posts page displays responsive cards.
- Login and registration with session-based auth.
- Admin can delete posts (buttons on cards and a small ID form on the posts page).

Tech stack
- Python, Flask, Jinja2
- SQLite via Flask-SQLAlchemy
- Bootstrap 5 (CDN) + small custom CSS

Routes
- `/` — Home (latest posts slider)
- `/posts` — List all posts (GET), admin-only delete by ID (POST)
- `/create` — Create a post (GET/POST)
- `/register`, `/login`, `/logout`
- `/posts/<post_id>/delete` — Delete a post (POST; admin only)

Admin access
- Default local admin: `admin` / `admin123`
- If missing in your DB, create it:
  1) Register a user at `/register` with username `admin` and the desired password.
  2) Promote to admin in a Python shell:
     ```bash
     python -c "from app import db, User; u=User.query.filter_by(username='admin').first(); u.role='admin'; db.session.commit()"
     ```

Run locally
- Python 3.10+ recommended.
- Create venv and install deps:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
  pip install -U Flask Flask-SQLAlchemy Werkzeug
  ```
- Initialize DB tables if needed (first run only):
  ```bash
  python -c "from app import db; db.create_all()"
  ```
- Start the app:
  ```bash
  python app.py
  # or
  export FLASK_APP=app.py && flask run
  ```

Notes
- To restrict creating posts to logged-in users, add a simple `login_required` decorator and apply it to the `/create` route.
- The included admin credentials are for local development only.

---

## Deutsch

Überblick
- Ein kleines Blog mit Flask und SQLite.
- Startseite mit einem horizontalen Slider der neuesten Beiträge.
- Alle-Beiträge-Seite mit responsiven Karten.
- Login und Registrierung (Session-basiert).
- Admin kann Beiträge löschen (Buttons auf den Karten und ein kleines ID-Formular auf der Posts-Seite).

Technologien
- Python, Flask, Jinja2
- SQLite über Flask-SQLAlchemy
- Bootstrap 5 (CDN) + etwas eigenes CSS

Routen
- `/` — Startseite (Slider mit neuesten Beiträgen)
- `/posts` — Alle Beiträge (GET), Löschen per ID (POST; nur Admin)
- `/create` — Beitrag erstellen (GET/POST)
- `/register`, `/login`, `/logout`
- `/posts/<post_id>/delete` — Beitrag löschen (POST; nur Admin)

Admin-Zugang
- Standard-Admin (lokal): `admin` / `admin123`
- Falls der Benutzer in der DB fehlt, so anlegen:
  1) Nutzer über `/register` mit Benutzername `admin` registrieren.
  2) In der Python-Shell zum Admin machen:
     ```bash
     python -c "from app import db, User; u=User.query.filter_by(username='admin').first(); u.role='admin'; db.session.commit()"
     ```

Lokal ausführen
- Python 3.10+ empfohlen.
- Virtuelle Umgebung und Abhängigkeiten:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
  pip install -U Flask Flask-SQLAlchemy Werkzeug
  ```
- DB initialisieren (nur beim ersten Start nötig):
  ```bash
  python -c "from app import db; db.create_all()"
  ```
- App starten:
  ```bash
  python app.py
  # oder
  export FLASK_APP=app.py && flask run
  ```

Hinweise
- Um das Erstellen von Beiträgen nur eingeloggten Nutzern zu erlauben, einen `login_required`-Decorator nutzen und auf `/create` anwenden.
- Die Admin-Zugangsdaten gelten nur für lokale Entwicklung.

---

## Русский

Описание
- Мини‑блог на Flask и SQLite.
- Домашняя страница с горизонтальным слайдером последних постов.
- Страница всех постов с адаптивными карточками.
- Логин и регистрация (на сессиях).
- Админ может удалять посты (кнопки на карточках и форма по ID на странице постов).

Технологии
- Python, Flask, Jinja2
- SQLite через Flask-SQLAlchemy
- Bootstrap 5 (CDN) + немного кастомного CSS

Маршруты
- `/` — Домашняя (слайдер последних постов)
- `/posts` — Все посты (GET), удаление по ID (POST; только админ)
- `/create` — Создание поста (GET/POST)
- `/register`, `/login`, `/logout`
- `/posts/<post_id>/delete` — Удаление поста (POST; только админ)

Доступ администратора
- Стандартный локальный админ: `admin` / `admin123`
- Если такого пользователя нет в базе, создайте:
  1) Зарегистрируйте `admin` на `/register`.
  2) Повысьте роль в Python‑шелле:
     ```bash
     python -c "from app import db, User; u=User.query.filter_by(username='admin').first(); u.role='admin'; db.session.commit()"
     ```

Запуск локально
- Рекомендуется Python 3.10+.
- Виртуальное окружение и зависимости:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
  pip install -U Flask Flask-SQLAlchemy Werkzeug
  ```
- Инициализация базы (при первом запуске):
  ```bash
  python -c "from app import db; db.create_all()"
  ```
- Запуск приложения:
  ```bash
  python app.py
  # или
  export FLASK_APP=app.py && flask run
  ```

Заметки
- Чтобы разрешить создание постов только авторизованным, добавьте декоратор `login_required` и примените к маршруту `/create`.
- Данные админа предназначены только для локальной разработки.
