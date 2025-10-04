from flask import Flask, render_template, request, redirect, session, url_for, abort
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__)
# Используем PostgreSQL, если есть переменная окружения (например, на Render)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'sqlite:///app.db'  # fallback для локального запуска
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    try:
        db.create_all()
        print("✅ Database and tables created (if not exist).")
    except Exception as e:
        print("⚠️ Database initialization failed:", e)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@app.route('/index')
@app.route('/')
def index():
    latest_posts = Post.query.order_by(Post.id.desc()).limit(20).all()
    return render_template('index.html', posts=latest_posts)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        post = Post(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('posts'))
        except:
            return "An error occurred while adding the article."
    else:
        return render_template('create.html')


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        # Admin-only delete by ID from the top form
        if session.get('role') != 'admin':
            abort(403)
        post_id = request.form.get('idpost')
        if post_id:
            try:
                post_id_int = int(post_id)
                post = db.session.get(Post, post_id_int)
                if post:
                    db.session.delete(post)
                    db.session.commit()
                    return redirect(url_for('posts'))
            except ValueError:
                pass  # Ignore invalid input and just re-render
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)


@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    if session.get('role') != 'admin':
        abort(403)

    post = db.session.get(Post, post_id)
    if not post:
        abort(404)

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            return "Username already exists."

        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        return render_template('register.html')


app.secret_key = "secret_key_for_session"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['role'] = user.role
            return redirect('/')
        else:
            return "Invalid username or password."
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=False)
