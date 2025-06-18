
# TODO 1
# TODO 2
import json
import threading
import time

app = # TODO 3

# Variables globales pour les métriques
metrics = {
    # TODO 4,
    # TODO 5,
    # TODO 6,
    # TODO 7,
    # TODO 8,
    # TODO 9
}

def consume_analytics():
    """Consumer en arrière-plan pour collecter les métriques"""
    conf = {
        # TODO 10,
        # TODO 11,
        # TODO 12
    }
    
    # TODO 13
    # TODO 14
    
    print("📊 Collecteur de métriques démarré")
    
    while True:
        try:
            # TODO 15
            
            if msg is None:
                continue
                
            if msg.error():
                continue
            
            # TODO 16
            # TODO 17
            
            if topic == 'analytics' and data.get('status') == 'confirmed':
                # Mettre à jour les métriques
                metrics['total_orders'] += # TODO 18
                metrics['total_revenue'] += # TODO 19
                
                region = data['customer_region']
                metrics['orders_by_region'][region] = # TODO 20
                
                product = data['product_name']
                metrics['top_products'][product] = # TODO 21
                
            elif topic == 'errors':
                metrics['error_count'] += # TODO 22
            
            metrics['last_update'] = # TODO 23
            
        except Exception as e:
            print(f"Erreur collecteur: {e}")
            time.sleep(1)

# TODO 24
def dashboard():
    """Page d'accueil avec dashboard"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TechShop Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .metric { background: #f0f0f0; padding: 10px; margin: 10px 0; border-radius: 5px; }
            .error { color: red; }
            .success { color: green; }
        </style>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <h1>🏪 TechShop - Dashboard Temps Réel</h1>
        
        <div class="metric">
            <h2>📊 Métriques Globales</h2>
            <p>Total Commandes: <span id="totalOrders">0</span></p>
            <p>Chiffre d'affaires: <span id="totalRevenue">0</span>€</p>
            <p class="error">Erreurs: <span id="errorCount">0</span></p>
            <p>Dernière mise à jour: <span id="lastUpdate">-</span></p>
        </div>
        
        <div class="metric">
            <h2>🌍 Commandes par région</h2>
            <div id="regionStats"></div>
        </div>
        
        <div class="metric">
            <h2>🏆 Top Produits</h2>
            <div id="productStats"></div>
        </div>
        
        <script>
            function updateDashboard() {
                fetch('/metrics')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('totalOrders').textContent = data.total_orders;
                        document.getElementById('totalRevenue').textContent = data.total_revenue.toFixed(2);
                        document.getElementById('errorCount').textContent = data.error_count;
                        document.getElementById('lastUpdate').textContent = new Date(data.last_update * 1000).toLocaleTimeString();
                        
                        // Régions
                        let regionHtml = '';
                        for (let [region, count] of Object.entries(data.orders_by_region)) {
                            regionHtml += `<p>${region}: ${count} commandes</p>`;
                        }
                        document.getElementById('regionStats').innerHTML = regionHtml;
                        
                        // Produits
                        let productHtml = '';
                        for (let [product, count] of Object.entries(data.top_products)) {
                            productHtml += `<p>${product}: ${count} ventes</p>`;
                        }
                        document.getElementById('productStats').innerHTML = productHtml;
                    })
                    .catch(err => console.error('Erreur:', err));
            }
            
            setInterval(updateDashboard, 2000);
            updateDashboard();
        </script>
    </body>
    </html>
    """
    return html

# TODO 25
def get_metrics():
    """API pour récupérer les métriques"""
    return # TODO 26

# TODO 27
def health_check():
    """Vérification de santé"""
    return {"status": "healthy", "timestamp": time.time()}

if __name__ == "__main__":
    # Démarrer le consumer en arrière-plan
    # TODO 28
    
    print("🌐 API démarrée sur http://localhost:5000")
    # TODO 29
