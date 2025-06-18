
# TODO 1
import json

def send_email_notification(order):
    """Simule l'envoi d'un email"""
    print(f"📧 Email → {order['customer_email']}")
    print(f"   Sujet: Commande {order['order_id']} confirmée")
    print(f"   Produit: {order['product_name']} x{order['quantity']}")
    print(f"   Total: {order['total']}€")

def send_sms_notification(order):
    """Simule l'envoi d'un SMS pour les VIP"""
    if order['customer_vip']:
        print(f"📱 SMS VIP → {order['customer_id']}")
        print(f"   🎉 Votre commande {order['order_id']} est en préparation!")
        print(f"   Livraison prioritaire en cours...")

def notification_consumer():
    """Consumer pour les notifications"""
    conf = {
        # TODO 2,
        # TODO 3,
        # TODO 4,
        # TODO 5
    }
    
    # TODO 6
    # TODO 7
    
    print("📧 Service de notifications démarré")
    
    try:
        while True:
            # TODO 8
            
            if msg is None:
                continue
                
            if msg.error():
                print(f"❌ Erreur: {msg.error()}")
                continue
            
            try:
                # TODO 9
                
                # Envoyer email pour toutes les commandes
                # TODO 10
                
                # Envoyer SMS pour les clients VIP
                # TODO 11
                
                # Commit manuel
                # TODO 12
                
                print("   ✅ Notifications envoyées\n")
                
            except Exception as e:
                print(f"❌ Erreur traitement notification: {e}")
                
    except KeyboardInterrupt:
        print("\n⏹️ Arrêt du service de notifications")
    finally:
        # TODO 13

# TODO 14
