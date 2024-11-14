from flask import Blueprint, render_template
from app.model.category import Category
from app.model.product import Product

home_bp = Blueprint('home', __name__)

categories = [Category(1, "Ação"), Category(2, "Aventura"), Category(3, "RPG"), Category(4, "Simulação"), Category(5, "Estratégia"), Category(6, "Esporte")]
products = [
    Product(1, "Elden Ring", 359.99, 1, "Câmera digital de alta resolução.", [
        "https://image.api.playstation.com/vulcan/ap/rnd/202107/0902/8ew9QqHI1eLFFq5XdIOhN2Q2.jpg",
    ]),

    Product(2, "Sekiro Shadow Die Twice", 249.99, 2, "Sekiro Shadow Die Twice", [
        "https://image.api.playstation.com/vulcan/img/rnd/202010/2723/knxU5uU5aKvQChKX5OvWtSGC.png",
    ]),

    Product(3, "Dark Souls Remastered", 299.95, 3, "Dark Souls Remastered", [
        "https://image.api.playstation.com/cdn/UP0700/CUSA08692_00/JxilRmpXkS3CCXUnr0gZTBOlqso3plaw.png",
    ]),

    Product(4, "Dark Souls II", 99.99, 3, "Dark Souls II", [
        "https://image.api.playstation.com/vulcan/img/rnd/202010/0919/KsbzaxvzYc4rhCpU5XcewIfn.png",
    ]),

    Product(5, "Dark Souls III", 149.99, 3, "Dark Souls III", [
        "https://image.api.playstation.com/cdn/UP0700/CUSA03388_00/v8JlD8KcQUtTqaLBmpFnj1ESRR5zMkLk.png",
    ]),

    Product(6, "Hollow Knight", 89.99, 3, "Hollow Knight", [
        "https://image.api.playstation.com/cdn/UP1822/CUSA13632_00/GuFQKWlrIVODEA1su20fCOrNZEYX5CB9.png",
    ]),

    Product(7, "Baldurs gate III", 289.99, 3, "Baldurs gate III", [
        "https://image.api.playstation.com/vulcan/ap/rnd/202308/2413/968ed1401bf14df79ac0af83e41cfe1f41dd06dec1ecd6bd.png",
    ]),

    Product(8, "World of Warcraft", 79.99, 3, "World of Warcraft", [
        "https://bdjogos.com.br/capas/5854-World-of-WarCraft-PC-capa-1.jpg",
    ]),

    Product(9, "Torchlight III", 189.99, 3, "Torchlight III", [
        "https://image.api.playstation.com/vulcan/ap/rnd/202009/1619/dGluovYE8C90XBw1qN2TosDy.png",
    ]),
    
    Product(10, "Forager", 39.99, 3, "Forager", [
        "https://store-images.s-microsoft.com/image/apps.49517.13796714672158376.aa1c19be-0d47-46ac-9fb3-74c8d6d9fdf8.061b6ecc-7883-45e5-be31-fb740679ad70",
    ])
]

@home_bp.route('/')
def home():
    return render_template('index.html', categories=categories, products=Product.all_products)
