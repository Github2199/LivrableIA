# Importer les modules Flask nécessaires
from flask import Flask, render_template, request, redirect, url_for

# Initialiser l'application Flask
app = Flask(__name__)

# Liste des plats disponibles au restaurant (exemple)
menu_items = [
    {"id": 1, "name": "Pizza", "price": 10.99},
    {"id": 2, "name": "Burger", "price": 8.99},
    {"id": 3, "name": "Salade", "price": 5.99},
]

# Panier de commande (exemple)
order_cart = []

# Route principale pour afficher le menu et gérer la commande
@app.route('/')
def menu():
    return render_template('menu.html', menu_items=menu_items)

# Ajouter un plat au panier
@app.route('/add_to_cart/<int:item_id>')
def add_to_cart(item_id):
    for item in menu_items:
        if item['id'] == item_id:
            order_cart.append(item)
            break
    return redirect(url_for('menu'))

# Afficher le panier de commande
@app.route('/view_cart')
def view_cart():
    return render_template('cart.html', order_cart=order_cart)

# Supprimer un plat du panier
@app.route('/remove_from_cart/<int:item_id>')
def remove_from_cart(item_id):
    for item in order_cart:
        if item['id'] == item_id:
            order_cart.remove(item)
            break
    return redirect(url_for('view_cart'))

# Passer une commande (cette étape peut être plus élaborée selon les besoins)
@app.route('/place_order')
def place_order():
    total_amount = sum(item['price'] for item in order_cart)
    # Ici, vous pouvez intégrer des fonctionnalités de paiement, de confirmation, etc.
    order_cart.clear()
    return render_template('order_confirmation.html', total_amount=total_amount)

# Point d'entrée de l'application
if __name__ == '__main__':
    app.run(debug=True)
