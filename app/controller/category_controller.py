from flask import Blueprint, render_template

from app.model.category import Category

category_bp = Blueprint('category', __name__)

categories = [Category(1, "Ação"), Category(2, "Aventura"), Category(3, "RPG"), category(4, "Simulação"), category(5, "Estratégia"), category(6, "Esporte")]

@category_bp.route('/categories')
def list_categories():
    return render_template('categories.html', categories=categories)
