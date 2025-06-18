# TODO 1
import json

def handle_out_of_stock(order):
    """Gère les ruptures de stock"""
    print(f"\n⚠️ RUPTURE DE STOCK DÉTECTÉE")
    print(f"   Commande: {order['order_id']}")
    print(f"   Produit: {order['product_name']}")
    print(f"   Quantité demandée: {order['quantity']}")
    print(f"   Client: {order['customer_email']}")
    print(f"   Raison: {order.get('error_reason', 'Stock insuffisant')}")
    
    # Notification client
    print(f"📧 Envoi email d'excuse à {order['customer_email']}")
    
    # Alerte équipe logistique
    print(f"🚨 Alerte équipe logistique: Réapprovisionner {order['product_name']}")
    
    # Log pour analytics
    print(f"📊 Log erreur pour dashboard")

def error_consumer():
    """Consumer pour la gestion d'erreurs"""
    print("🚨 Service de gestion d'erreurs démarré")
    
    conf = {
        # TODO 2,
        # TODO 3,
        # TODO 4
    }
    
    # TODO 5
    # TODO 6
    
    try:
        while True:
            # TODO 7
            
            if msg is None:
                continue
                
            if msg.error():
                print(f"❌ Erreur consumer: {msg.error()}")
                continue
            
            try:
                # TODO 8
                
                if order['status'] == # TODO 9:
                    # TODO 10
                
                # TODO 11
                
            except Exception as e:
                print(f"❌ Erreur traitement erreur: {e}")
                
    except KeyboardInterrupt:
        print("\n⏹️ Arrêt du service d'erreurs")
    finally:
        # TODO 12

# TODO 13
