# TODO 1
import json

# TODO 2
app = faust.App(
    # TODO 3,
    # TODO 4,
    # TODO 5,
    # TODO 6
)

# Topics
orders_topic = # TODO 7
inventory_topic = # TODO 8
notifications_topic = # TODO 9
analytics_topic = # TODO 10
errors_topic = # TODO 11

# Stock en mémoire simple (dictionnaire Python - PAS de Table Faust)
stock = {
    # TODO 12
    # TODO 13
    # TODO 14
    # TODO 15
    # TODO 16
}

# TODO 17
async def process_orders(orders):
    """Traite les commandes entrantes"""
    print("📦 Stock initialisé:", stock)
    
    # TODO 18
        print(f"\n📦 Traitement commande {order['order_id']}")
        print(f"   Produit: {order['product_name']} x{order['quantity']}")
        
        product_id = order['product_id']
        quantity_needed = order['quantity']
        current_stock = # TODO 19
        
        if current_stock >= quantity_needed:
            # Stock OK - Confirmer la commande
            stock[product_id] = # TODO 20
            order['status'] = # TODO 21
            
            print(f"   ✅ Commande confirmée - Stock restant: {stock[product_id]}")
            
            # Envoyer vers notifications et analytics
            # TODO 22
            # TODO 23
            
            # Mise à jour inventaire
            inventory_update = {
                "product_id": product_id,
                "old_stock": current_stock,
                "new_stock": stock[product_id],
                "operation": "sale",
                "quantity": quantity_needed,
                "timestamp": order['timestamp']
            }
            # TODO 24
            
        else:
            # Stock insuffisant
            order['status'] = # TODO 25
            order['error_reason'] = f"Stock insuffisant: {current_stock} disponible, {quantity_needed} demandé"
            
            print(f"   ❌ Stock insuffisant: {current_stock} < {quantity_needed}")
            
            # Envoyer vers les erreurs
            # TODO 26

# TODO 27
async def log_inventory_changes(inventory_updates):
    """Log les changements d'inventaire"""
    # TODO 28
        print(f"📊 Inventaire mis à jour: {update['product_id']} → {update['new_stock']}")

# TODO 29