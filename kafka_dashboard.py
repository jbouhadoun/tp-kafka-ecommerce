import time
import json
import os

def clear_screen():
    """Efface l'écran"""
    # TODO 3

def get_topic_message_count(admin, topic_name):
    """Estime le nombre de messages dans un topic"""
    try:
        # TODO 4
        if topic_name in metadata.topics:
            partitions = len(metadata.topics[topic_name].partitions)
            return f"{partitions} partitions"
        return "0"
    except:
        return "Erreur"

def monitor_topics():
    """Surveille l'activité des topics"""
    # TODO 5
    # TODO 6
    
    while True:
        clear_screen()
        print("🏪 TECHSHOP - KAFKA DASHBOARD")
        print("=" * 60)
        print(f"⏰ Mise à jour: {time.strftime('%H:%M:%S')}")
        print()
        
        # Statut des topics
        print("📊 STATUT DES TOPICS:")
        print("-" * 40)
        for topic in topics_to_monitor:
            partitions = # TODO 7
            status = "🟢 Actif" if partitions != "Erreur" else "🔴 Erreur"
            print(f"   {topic:15} | {partitions:12} | {status}")
        
        print()
        
        # Consumer groups
        print("👥 CONSUMER GROUPS:")
        print("-" * 40)
        try:
            # TODO 8
            # TODO 9
            if group_list:
                for group in group_list[:5]:  # Top 5
                    print(f"   • {group.group_id}")
            else:
                print("   Aucun groupe actif")
        except Exception as e:
            print(f"   ❌ Erreur: {e}")
        
        print()
        
        # Métriques simulées
        print("📈 MÉTRIQUES TEMPS RÉEL:")
        print("-" * 40)
        print(f"   Commandes/min: ~{time.time() % 10:.0f}")
        print(f"   Taux d'erreur: {time.time() % 5:.1f}%")
        print(f"   Lag moyen: {time.time() % 3:.0f}ms")
        
        print()
        print("Ctrl+C pour arrêter")
        # TODO 10

def check_consumer_lag():
    """Vérifie le lag des consumers (version simplifiée)"""
    print("⏱️ Vérification du lag des consumers...")
    
    # Dans un vrai monitoring, on utiliserait l'Admin API
    # pour récupérer les offsets committed vs high water mark
    lag_alerts = []
    
    # Simulation de lag
    simulated_lags = {
        'notification-service': 2,
        'error-handler': 0,
        'analytics-processor': 5
    }
    
    for group, lag in simulated_lags.items():
        if lag > 3:
            lag_alerts.append(f"🚨 {group}: {lag} messages en retard")
        else:
            print(f"✅ {group}: {lag} messages de lag (OK)")
    
    if lag_alerts:
        print("\n⚠️ ALERTES LAG:")
        for alert in lag_alerts:
            print(f"   {alert}")

# TODO 11
