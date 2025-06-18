# TODO 1
import json
import random
import time
from datetime import datetime

# Données de test
PRODUCTS = {
    "P001": {"name": "iPhone 15", "price": 999, "stock": 50, "category": "Electronics"},
    "P002": {"name": "MacBook Pro", "price": 2499, "stock": 20, "category": "Electronics"},
    "P003": {"name": "Nike Air Max", "price": 149, "stock": 100, "category": "Fashion"},
    "P004": {"name": "Livre Python", "price": 29, "stock": 200, "category": "Books"},
    "P005": {"name": "Café Premium", "price": 15, "stock": 500, "category": "Food"}
}

CUSTOMERS = [
    {"id": "alice.martin", "email": "alice@email.com", "vip": True, "region": "Paris"},
    {"id": "bob.durand", "email": "bob@email.com", "vip": False, "region": "Lyon"},
    {"id": "carol.bernard", "email": "carol@email.com", "vip": True, "region": "Marseille"},
    {"id": "david.petit", "email": "david@email.com", "vip": False, "region": "Nice"},
    {"id": "emma.lopez", "email": "emma@email.com", "vip": True, "region": "Paris"}
]

def generate_order():
    """Génère une commande aléatoire"""
    customer = # TODO 2
    product_id = # TODO 3
    product = PRODUCTS[product_id]
    quantity = # TODO 4
    
    order = {
        "order_id": # TODO 5,
        "customer_id": customer["id"],
        "customer_email": customer["email"],
        "customer_vip": customer["vip"],
        "customer_region": customer["region"],
        "product_id": product_id,
        "product_name": product["name"],
        "product_category": product["category"],
        "price": product["price"],
        "quantity": quantity,
        "total": # TODO 6,
        "timestamp": # TODO 7,
        "status": "pending"
    }
    
    return order

def simulate_orders():
    """Simule un flux de commandes"""
    print("🛒 Démarrage simulation de commandes...")
    
    # TODO 8
    
    def delivery_callback(err, msg):
        if err:
            print(f"❌ Erreur: {err}")
        else:
            order = # TODO 9
            print(f"✅ Commande {order['order_id']} envoyée - {order['product_name']} x{order['quantity']}")
    
    try:
        for i in range(50):  # 50 commandes
            order = generate_order()
            
            # Envoyer la commande vers le topic 'orders'
            producer.produce(
                topic=# TODO 10,
                key=# TODO 11,
                value=# TODO 12,
                callback=delivery_callback
            )
            
            # TODO 13  # Trigger delivery reports
            # TODO 14  # Délai réaliste
            
    except KeyboardInterrupt:
        print("\n⏹️ Arrêt de la simulation")
    finally:
        # TODO 15
        print("📦 Toutes les commandes envoyées !")

# TODO 16