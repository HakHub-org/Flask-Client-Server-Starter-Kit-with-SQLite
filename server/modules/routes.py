"""
Application Routes
"""

from flask import Blueprint, jsonify, request
from database.connection import get_database_connection

api_bp = Blueprint('api', __name__)

@api_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200

@api_bp.route('/users', methods=['GET'])
def get_users():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)

@api_bp.route('/posts', methods=['GET'])
def get_posts():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conn.close()
    return jsonify(posts)

@api_bp.route('/comments', methods=['GET'])
def get_comments():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM comments")
    comments = cursor.fetchall()
    conn.close()
    return jsonify(comments)

@api_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        (data['username'], data['email'], data['password'])
    )
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": user_id}), 201

@api_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)",
        (data['user_id'], data['title'], data['content'])
    )
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": post_id}), 201

@api_bp.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO comments (post_id, user_id, content) VALUES (?, ?, ?)",
        (data['post_id'], data['user_id'], data['content'])
    )
    conn.commit()
    comment_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": comment_id}), 201
