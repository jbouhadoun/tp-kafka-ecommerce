# setup_topics.py - Exercice

**TODO 1 :** Importez AdminClient et NewTopic depuis confluent_kafka.admin

**TODO 2 :** Créez un AdminClient qui se connecte à 'localhost:9093'

**TODO 3 :** Créez un NewTopic 'orders' avec 3 partitions et replication_factor=1

**TODO 4 :** Créez un NewTopic 'inventory' avec 3 partitions et replication_factor=1

**TODO 5 :** Créez un NewTopic 'notifications' avec 3 partitions et replication_factor=1

**TODO 6 :** Créez un NewTopic 'analytics' avec 3 partitions et replication_factor=1

**TODO 7 :** Créez un NewTopic 'errors' avec 1 partition et replication_factor=1

**TODO 8 :** Appelez create_topics() sur l'admin avec la liste des topics

**TODO 9 :** Appelez future.result() pour attendre la création

**TODO 10 :** Affichez "✅ Topic '{topic_name}' créé"

**TODO 11 :** Affichez "❌ '{topic_name}': {e}"

**TODO 12 :** Affichez "🎉 Setup des topics terminé !"

**TODO 13 :** Ajoutez if __name__ == "__main__": create_ecommerce_topics()


# order_producer.py - Exercice


**TODO 1 :** Importez Producer depuis confluent_kafka

**TODO 2 :** Choisissez un client aléatoirement dans la liste CUSTOMERS

**TODO 3 :** Choisissez un product_id aléatoirement parmi les clés de PRODUCTS

**TODO 4 :** Générez une quantité aléatoire entre 1 et 3

**TODO 5 :** Créez un order_id au format "ORD-XXXX" avec un nombre aléatoire entre 1000 et 9999

**TODO 6 :** Calculez le total (price × quantity)

**TODO 7 :** Obtenez le timestamp actuel au format ISO

**TODO 8 :** Créez un Producer qui se connecte à 'localhost:9093'

**TODO 9 :** Décodez le message JSON reçu depuis msg.value()

**TODO 10 :** Spécifiez le topic 'orders'

**TODO 11 :** Utilisez order['order_id'] comme clé

**TODO 12 :** Convertissez l'order en JSON avec json.dumps()

**TODO 13 :** Appelez producer.poll(0) pour déclencher les delivery reports

**TODO 14 :** Ajoutez un délai aléatoire entre 0.5 et 2 secondes avec time.sleep()

**TODO 15 :** Appelez producer.flush() pour s'assurer que tous les messages sont envoyés

**TODO 16 :** Ajoutez if __name__ == "__main__": simulate_orders()




# order_processor.py - Exercice

**TODO 1 :** Importez faust

**TODO 2 :** Créez une application faust nommée

**TODO 3 :** Nom de l'application : 'order-processor'

**TODO 4 :** Broker : 'kafka://localhost:9093'

**TODO 5 :** Serializer : 'json'

**TODO 6 :** Port web : 6067

**TODO 7 :** Créez le topic 'orders' avec app.topic()

**TODO 8 :** Créez le topic 'inventory' avec app.topic()

**TODO 9 :** Créez le topic 'notifications' avec app.topic()

**TODO 10 :** Créez le topic 'analytics' avec app.topic()

**TODO 11 :** Créez le topic 'errors' avec app.topic()

**TODO 12 :** Stock pour "P001": 50

**TODO 13 :** Stock pour "P002": 20

**TODO 14 :** Stock pour "P003": 100

**TODO 15 :** Stock pour "P004": 200

**TODO 16 :** Stock pour "P005": 500

**TODO 17 :** Décorez la fonction avec @app.agent(orders_topic)

**TODO 18 :** Bouclez sur les commandes avec async for order in orders:

**TODO 19 :** Récupérez le stock actuel avec stock.get(product_id, 0)

**TODO 20 :** Mettez à jour le stock : current_stock - quantity_needed

**TODO 21 :** Statut de la commande : 'confirmed'

**TODO 22 :** Envoyez vers notifications_topic avec await notifications_topic.send(value=order)

**TODO 23 :** Envoyez vers analytics_topic avec await analytics_topic.send(value=order)

**TODO 24 :** Envoyez inventory_update vers inventory_topic

**TODO 25 :** Statut d'erreur : 'out_of_stock'

**TODO 26 :** Envoyez l'order vers errors_topic

**TODO 27 :** Décorez avec @app.agent(inventory_topic)

**TODO 28 :** Bouclez avec async for update in inventory_updates:

**TODO 29 :** Ajoutez if __name__ == '__main__': app.main()


# analytics_processor.py - Exercice

**TODO 1 :** Importez faust

**TODO 2 :** Créez une application faust

**TODO 3 :** Nom de l'application : 'analytics-processor'

**TODO 4 :** Broker : 'kafka://localhost:9093'

**TODO 5 :** Serializer : 'json'

**TODO 6 :** Port web : 6068

**TODO 7 :** Créez le topic 'analytics' avec app.topic()

**TODO 8 :** Initialisez 'total_orders' à 0

**TODO 9 :** Initialisez 'total_revenue' à 0.0

**TODO 10 :** Initialisez 'regions' à un dictionnaire vide {}

**TODO 11 :** Initialisez 'categories' à un dictionnaire vide {}

**TODO 12 :** Initialisez 'vip_sales' à 0.0

**TODO 13 :** Initialisez 'non_vip_sales' à 0.0

**TODO 14 :** Décorez la fonction avec @app.agent(analytics_topic)

**TODO 15 :** Bouclez sur les commandes avec async for order in orders:

**TODO 16 :** Incrémentez le compteur de 1

**TODO 17 :** Ajoutez order['total'] au chiffre d'affaires

**TODO 18 :** Ajoutez order['total'] au total de la région : stats['regions'].get(region, 0) + order['total']

**TODO 19 :** Ajoutez order['total'] au total de la catégorie : stats['categories'].get(category, 0) + order['total']

**TODO 20 :** Ajoutez order['total'] aux ventes VIP

**TODO 21 :** Ajoutez order['total'] aux ventes non-VIP

**TODO 22 :** Appelez show_analytics_summary()

**TODO 23 :** Ajoutez if __name__ == '__main__': app.main()


# notification_service.py - Exercice

**TODO 1 :** Importez Consumer depuis confluent_kafka

**TODO 2 :** Configuration bootstrap.servers : 'localhost:9093'

**TODO 3 :** Configuration group.id : 'notification-service'

**TODO 4 :** Configuration auto.offset.reset : 'earliest'

**TODO 5 :** Configuration enable.auto.commit : False

**TODO 6 :** Créez un Consumer avec la configuration

**TODO 7 :** Abonnez le consumer au topic 'notifications' avec subscribe()

**TODO 8 :** Récupérez un message avec consumer.poll(1.0)

**TODO 9 :** Décodez le message JSON : json.loads(msg.value().decode('utf-8'))

**TODO 10 :** Appelez send_email_notification(order)

**TODO 11 :** Appelez send_sms_notification(order)

**TODO 12 :** Commitez le message avec consumer.commit(msg)

**TODO 13 :** Fermez le consumer avec consumer.close()

**TODO 14 :** Ajoutez if __name__ == "__main__": notification_consumer()


# error_handler.py - Exercice

**TODO 1 :** Importez Consumer depuis confluent_kafka

**TODO 2 :** Configuration bootstrap.servers : 'localhost:9093'

**TODO 3 :** Configuration group.id : 'error-handler'

**TODO 4 :** Configuration auto.offset.reset : 'earliest'

**TODO 5 :** Créez un Consumer avec la configuration

**TODO 6 :** Abonnez le consumer au topic 'errors' avec subscribe()

**TODO 7 :** Récupérez un message avec consumer.poll(1.0)

**TODO 8 :** Décodez le message JSON : json.loads(msg.value().decode('utf-8'))

**TODO 9 :** Vérifiez le statut 'out_of_stock'

**TODO 10 :** Appelez handle_out_of_stock(order)

**TODO 11 :** Commitez le message avec consumer.commit(msg)

**TODO 12 :** Fermez le consumer avec consumer.close()

**TODO 13 :** Ajoutez if __name__ == "__main__": error_consumer()



# metrics_api.py - Exercice

**TODO 1 :** Importez Flask, jsonify, render_template_string depuis flask

**TODO 2 :** Importez Consumer depuis confluent_kafka

**TODO 3 :** Créez une instance Flask(__name__)

**TODO 4 :** Initialisez "total_orders" à 0

**TODO 5 :** Initialisez "total_revenue" à 0.0

**TODO 6 :** Initialisez "orders_by_region" à un dictionnaire vide {}

**TODO 7 :** Initialisez "top_products" à un dictionnaire vide {}

**TODO 8 :** Initialisez "error_count" à 0

**TODO 9 :** Initialisez "last_update" avec time.time()

**TODO 10 :** Configuration bootstrap.servers : 'localhost:9093'

**TODO 11 :** Configuration group.id : 'metrics-collector'

**TODO 12 :** Configuration auto.offset.reset : 'latest'

**TODO 13 :** Créez un Consumer(conf)

**TODO 14 :** Abonnez aux topics ['analytics', 'errors']

**TODO 15 :** Récupérez un message avec consumer.poll(1.0)

**TODO 16 :** Décodez le JSON : json.loads(msg.value().decode('utf-8'))

**TODO 17 :** Récupérez le topic avec msg.topic()

**TODO 18 :** Incrémentez de 1

**TODO 19 :** Ajoutez data['total']

**TODO 20 :** Incrémentez : metrics['orders_by_region'].get(region, 0) + 1

**TODO 21 :** Incrémentez : metrics['top_products'].get(product, 0) + 1

**TODO 22 :** Incrémentez de 1

**TODO 23 :** Mettez à jour avec time.time()

**TODO 24 :** Décorez avec @app.route('/')

**TODO 25 :** Décorez avec @app.route('/metrics')

**TODO 26 :** Retournez jsonify(metrics)

**TODO 27 :** Décorez avec @app.route('/health')

**TODO 28 :** Démarrez le thread : threading.Thread(target=consume_analytics, daemon=True).start()

**TODO 29 :** Lancez l'app : app.run(debug=True, port=5000, threaded=True)


# kafka_dashboard.py - Exercice

**TODO 1 :** Importez AdminClient depuis confluent_kafka.admin

**TODO 2 :** Importez Consumer depuis confluent_kafka

**TODO 3 :** Appelez os.system('clear' if os.name == 'posix' else 'cls')

**TODO 4 :** Récupérez les métadonnées avec admin.list_topics(topic=topic_name, timeout=5)

**TODO 5 :** Créez un AdminClient avec {'bootstrap.servers': 'localhost:9093'}

**TODO 6 :** Définissez topics_to_monitor = ['orders', 'notifications', 'analytics', 'inventory', 'errors']

**TODO 7 :** Appelez get_topic_message_count(admin, topic)

**TODO 8 :** Récupérez les groupes avec admin.list_consumer_groups(timeout=5)

**TODO 9 :** Convertissez en liste avec list(groups.result())

**TODO 10 :** Attendez 10 secondes avec time.sleep(10)

**TODO 11 :** Ajoutez la logique principale :
```python
if __name__ == "__main__":
    try:
        monitor_topics()
    except KeyboardInterrupt:
        print("\n👋 Dashboard arrêté")
```