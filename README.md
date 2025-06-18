# TP NOTÉ - KAFKA E-COMMERCE TECHSHOP

**Durée :** 4 heures  
**Modalité :** GROUPE  (4 MAX)  

---

## 📋 **CONTEXTE MÉTIER**

Vous êtes développeur chez **TechShop**, une startup e-commerce en forte croissance. L'architecture monolithique actuelle ne tient plus la charge et génère des goulots d'étranglement.

Votre mission : **Migrer vers une architecture événementielle** basée sur Apache Kafka pour traiter les commandes en temps réel.

### **Besoins fonctionnels :**
- 🛒 **Traitement des commandes** avec gestion de stock temps réel
- 📧 **Notifications automatiques** (Email + SMS VIP)
- 📊 **Analytics en temps réel** (CA, régions, catégories)
- 🚨 **Gestion d'erreurs** (ruptures de stock)
- 📈 **Monitoring** des flux et performances

### **Contraintes techniques :**
- **1000+ commandes/heure** en pic
- **Latence < 100ms** pour la validation de commande
- **Zéro perte** de message
- **Haute disponibilité** (tolérance aux pannes)

---

## 🏗️ **ARCHITECTURE CIBLE**


```
📱 Order Producer  →  📦 [orders]     →  🧠 Order Processor (Faust)
   (Simulation)         Topic              Port 6067
                           ↓
                    ┌─────────────────────────────────┐
                    ▼                                 ▼
           📧 [notifications]                 📊 [analytics]
              Topic                            Topic
                    ↓                                 ▼
        Notification Service            Analytics Processor
           (Consumer)                     (Faust - Port 6068)

                          📋 [inventory]    ❌ [errors]
                             Topic           Topic
                                ↓              ↓
                         Inventory Log    Error Handler
```

### Topics Kafka requis
- **`orders`** : 3 partitions - Commandes entrantes
- **`notifications`** : 3 partitions - Messages email/SMS
- **`analytics`** : 3 partitions - Données pour métriques
- **`inventory`** : 3 partitions - Mises à jour stock
- **`errors`** : 1 partition - Commandes en échec

---

## 📂 FICHIERS FOURNIS

Vous recevrez **7 fichiers Python** avec des TODO numérotés à compléter :

### 1. **setup_topics.py** (13 TODO)
Configuration automatique des topics Kafka
```python
# TODO 1-2 : Import AdminClient et configuration
# TODO 3-7 : Création des 5 topics avec NewTopic
# TODO 8-13 : Exécution et gestion d'erreurs
```

### 2. **order_producer.py** (16 TODO)  
Générateur de commandes e-commerce
```python
# TODO 1-7 : Génération données aléatoires (client, produit, quantité)
# TODO 8-16 : Configuration Producer et envoi vers topic 'orders'
```

### 3. **order_processor.py** (29 TODO)
Cœur du système - Stream processing avec Faust
```python
# TODO 1-11 : Configuration app Faust et topics
# TODO 12-16 : Initialisation stock en mémoire  
# TODO 17-29 : Logique validation commandes et routage
```

### 4. **analytics_processor.py** (23 TODO)
Calcul de métriques temps réel
```python
# TODO 1-7 : Configuration Faust analytics
# TODO 8-13 : Variables métriques (CA, régions, VIP)
# TODO 14-23 : Agent calcul et affichage stats
```

### 5. **notification_service.py** (14 TODO)
Service d'envoi email/SMS
```python
# TODO 1-6 : Configuration Consumer groups
# TODO 7-14 : Boucle consommation et notifications
```

### 6. **error_handler.py** (13 TODO)
Gestion des commandes en échec
```python
# TODO 1-5 : Configuration Consumer erreurs
# TODO 6-13 : Traitement spécialisé ruptures stock
```

### 7. **metrics_api.py** (29 TODO)
Dashboard web temps réel
```python
# TODO 1-29 : API Flask + Consumer analytics + interface HTML
```

### 8. **kafka_dashboard.py** (11 TODO)
Monitoring Kafka en temps réel
```python
# TODO 1-11 : AdminClient + surveillance topics + consumer groups
```

---

## 📝 TRAVAIL À RÉALISER

### **PARTIE 1 - Complétion des TODO**

**Vous devez compléter TOUS les TODO dans l'ordre des fichiers :**

#### **1.1 Infrastructure**
- Complétez `setup_topics.py` (TODO 1-13) [Consignes](./TODO.md#setup_topicspy)
- Créez les 5 topics avec configurations correctes
- Gérez les erreurs de création

#### **1.2 Production de données**  
- Complétez `order_producer.py` (TODO 1-16)[Consignes](./TODO.md#order_producerpy---exercice)
- Générez des commandes JSON réalistes
- Implémentez les callbacks de delivery

#### **1.3 Traitement des commandes**
- Complétez `order_processor.py` (TODO 1-29) [Consignes](./TODO.md#order_processorpy---exercice)
- Configurez Faust avec topics et stock
- Implémentez la logique de validation et routage

#### **1.4 Analytics temps réel**
- Complétez `analytics_processor.py` (TODO 1-23) [Consignes](./TODO.md#analytics_processorpy---exercice)
- Calculez métriques globales et segmentées
- Affichez résultats formatés

#### **1.5 Services annexes **
- Complétez `notification_service.py` (TODO 1-14) [Consignes](./TODO.md#notification_servicepy---exercice)
- Complétez `error_handler.py` (TODO 1-13) [Consignes](./TODO.md#error_handlerpy---exercice)
- Configurez Consumer Groups correctement

#### **1.6 Dashboard et monitoring**
- Complétez `metrics_api.py` (TODO 1-29)[Consignes](./TODO.md#metrics_apirpy---exercice)
- Complétez `kafka_dashboard.py` (TODO 1-11)[Consignes](./TODO.md#kafka_dashboardpy---exercice)
- Implémentez API REST et monitoring Kafka

### **PARTIE 2 - Tests**

#### **2.1 Tests de fonctionnement**
1. **Démarrage des services** sans erreur
2. **Génération de  commandes** test
3. **Vérification des flux** dans AKHQ (localhost:8080)
4. **Affichage des métriques** analytics
5. **Dashboard web** accessible sur localhost:5000

#### **2.2 Dashboard monitoring**
- ✅ **Interface web** fonctionnelle sur localhost:5000
- ✅ **Métriques temps réel** actualisées

---


## 🚀 Installation

```bash
# Créer l'environnement
python -m venv kafka_tp
source kafka_tp/bin/activate  # Linux/Mac
# ou kafka_tp\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## 🔧 PROCÉDURE DE TEST

### **Ordre d'exécution obligatoire :**

```bash
# 1. Infrastructure Kafka
docker-compose up
python setup_topics.py

# 2. Services (dans des terminaux séparés)
python order_processor.py worker     # Terminal 1
python analytics_processor.py worker # Terminal 2  
python notification_service.py # Terminal 3
python error_handler.py        # Terminal 4
python metrics_api.py           # Terminal 5

# 3. Génération de commandes test
python order_producer.py       # Terminal 6

# 4. Monitoring
# Ouvrir http://localhost:8080 (AKHQ)
# Ouvrir http://localhost:5000 (Dashboard web)
python kafka_dashboard.py      # Terminal 7 (optionnel)
```
---

## ⚠️ CONSIGNES STRICTES

### **Obligatoire :**
- ✅ **Suivre la numérotation** exacte des TODO
- ✅ **Tester chaque fichier** avant de passer au suivant

### **Rendu :**
- **Archive ZIP** : `TP_Kafka.zip`
                     
- **Contenu** : 
  - Un fichier groupe.md contenant les noms des membres du groupe (ou le nom unique si travail individuel).
  - Tous les fichiers .py complétés

- **Deadline** : 18h
---

### ⚠️ **Envoi:**

Merci d’envoyer votre archive par mail à l’adresse :
jboubhadoun@gmail.com

#### **avec l’objet :[TP KAFKA]Nom1_Prenom1_Nom2_Prenom2**

---
### **Debugging :**
- **AKHQ** (localhost:8080) est votre meilleur ami
- **Restart des services** si comportement bizarre
---
