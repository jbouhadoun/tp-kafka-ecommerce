
# TODO 1

# TODO 2
app = faust.App(
    # TODO 3,
    # TODO 4,
    # TODO 5,
    # TODO 6
)

analytics_topic = # TODO 7

# Variables simples en mémoire (PAS de Tables Faust !)
stats = {
    # TODO 8,
    # TODO 9,
    # TODO 10,
    # TODO 11,
    # TODO 12,
    # TODO 13
}

# TODO 14
async def calculate_analytics(orders):
    """Calcule des métriques en temps réel"""
    # TODO 15
        if order.get('status') == 'confirmed':
            # Compteur total
            stats['total_orders'] += # TODO 16
            stats['total_revenue'] += # TODO 17
            
            # Ventes par région
            region = order['customer_region']
            stats['regions'][region] = # TODO 18
            
            # Ventes par catégorie
            category = order['product_category']
            stats['categories'][category] = # TODO 19
            
            # Ventes VIP
            if order['customer_vip']:
                stats['vip_sales'] += # TODO 20
            else:
                stats['non_vip_sales'] += # TODO 21
            
            print(f"📈 Analytics mis à jour pour commande {order['order_id']}")
            
            # Afficher le résumé toutes les 3 commandes
            if stats['total_orders'] % 3 == 0:
                # TODO 22

def show_analytics_summary():
    """Affiche un résumé des analytics"""
    print("\n🏆 === ANALYTICS SUMMARY ===")
    print(f"📊 Total commandes: {stats['total_orders']}")
    print(f"💰 Chiffre d'affaires: {stats['total_revenue']:.2f}€")
    
    if stats['regions']:
        print("\n🌍 Ventes par région:")
        for region, total in stats['regions'].items():
            print(f"   {region}: {total:.2f}€")
    
    if stats['categories']:
        print("\n📦 Ventes par catégorie:")
        for category, total in stats['categories'].items():
            print(f"   {category}: {total:.2f}€")
    
    print(f"\n👑 VIP: {stats['vip_sales']:.2f}€ | Non-VIP: {stats['non_vip_sales']:.2f}€")
    print("=" * 30)

# TODO 23


