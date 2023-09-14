Version Française
-----------------

Pour utiliser ce programme, suivez attentivement ces étapes :

1. Installation et configuration de Confluent Cloud Kafka

    1.1 Créez un compte Confluent Cloud
        - Accédez à https://confluent.cloud/signup pour créer un compte.

    1.2 Connectez-vous à votre compte Confluent Cloud
        - Accédez à https://login.confluent.io/login?state=hKFo2SBrYVBBZHFxNTlGRVRWcURaa2x0OHRWOS13RDFpWnhYbqFupWxvZ2luo3RpZNkgTFlYQXNmcFpHdDZxOVV5VUdnX3cxNHNhYVN2YWRDMWmjY2lk2SBsMmhPcDBTMHRrU0IwVEZ0dklZZlpaOUVhS0Z2clNjNg&client=l2hOp0S0tkSB0TFtvIYfZZ9EaKFvrSc6&protocol=oauth2&cache=%5Bobject%20Object%5D&redirect_uri=https%3A%2F%2Fconfluent.cloud%2Fauth_callback&redirect_path=%2F&last_org_resource_id_map=%7B%7D&segment_anon_id=e447ddac-73be-420c-8956-ea2079ea99db&scope=openid%20profile%20email%20offline_access&response_type=code&response_mode=query&nonce=eWt0QVdya0pXUEhKTkRGMUNyQkVRa2NtZjVFaVRHRUJKa1lTekRCM0J4cg%3D%3D&code_challenge=rfZ0NoJb6oFQYwIJ-W6gUWrA4Zuy32cJ1kwxso03DTU&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtcmVhY3QiLCJ2ZXJzaW9uIjoiMS4xMi4xIn0%3D
    
    1.3 Créez un nouvel environnement
        - Cliquez sur "Nouvel environnement" et sélectionnez "Commencer la configuration" (Begin configuration).
    
    1.4 Configuration de l'environnement
        - Sur la page de configuration, choisissez "AWS" comme fournisseur de cloud (cloud provider) et "Ohio" comme région, puis cliquez sur "Activer" (enable).
    
    1.5 Créez un cluster
        - Sur la page de votre environnement, cliquez sur "Créer un cluster par vous-même" => "Commencer la configuration".
        - Choisissez à nouveau "AWS" comme fournisseur de cloud, "Ohio" comme région et "Single Zone" comme "Disponibilité" (Availability).
        - Cliquez sur "Continuer" (Continue).
    
    1.6 Générez une clé API
        - Accédez à votre cluster et cliquez sur "Clés API" (API Keys) => "Créer une clé" (Create Key).
        - Sélectionnez "Accès global" (Global Access) puis "Suivant" (Next).
        - Cliquez sur "Télécharger et Continuer" (Download and Continue). Conservez ce fichier en sécurité, car vous en aurez besoin pour configurer le projet.
    
    1.7 Configurez les API Credentials
       - Cliquez sur "Download and Continue" pour télécharger le fichier contenant la clé API. Conservez ce fichier en lieu sûr, car vous en aurez besoin pour configurer le projet.

    1.8 Configuration de la gestion des flux
        - Sur l'interface de votre environnement, accédez à "Stream Governance API" => "Credentials" => "Add Key."

    1.9 Création d'une clé API pour la gestion des flux
        - Sur l'interface "API Credentials," cliquez sur "Create Key" puis "Download and Continue."

    1.10 Configuration d'un Topic Kafka
        - Sur l'interface de votre environnement, sélectionnez votre cluster, puis cliquez sur "Topics" => "Create Topic."
        - Donnez un nom au Topic et remplissez le champ "Partitions" avec 3.
        - Cliquez sur "Create with default" et ignorez la définition du contrat de données.

    1.11 Configuration du fichier kafka_config.json
        - Dans le projet, accédez au fichier "kafka_config.json" dans le dossier "config" et remplissez les informations suivantes :
        - sasl.username : le nom de votre API (API Key*)
        - sasl.password : le mot de passe de votre API (API Secret*)
        - bootstrap.servers : Serveur d'amorçage de votre API (Bootstrap server*)

    * Vous trouverez ces informations dans le fichier .txt que vous avez téléchargé lors de la création de l'API Key.

2. Installation et configuration de Jenkins

    2.1 Installation de Jenkins
        - Installez Jenkins en suivant les instructions fournies dans la documentation officielle : https://www.jenkins.io/doc/book/installing/windows/
        - Si vous rencontrez des problèmes lors de l'étape 3 (Identifiants de connexion au service), suivez les étapes indiquées ici : https://phoenixnap.com/kb/install-jenkins-on-windows#ftoc-heading-1:~:text=Note%3A%20When,the%20Properties%20window.

    2.2 Configuration de Jenkins
        - Après l'installation, accédez au tableau de bord Jenkins.
        - Cliquez sur "Nouveau Item" et saisissez un nom.
        - Sélectionnez "Construire un projet free-style" et cliquez sur "OK."

    2.3 Planification des builds
        - Dans la section "Ce qui déclenche le build," choisissez "Construire périodiquement" et saisissez la ligne suivante :
            TZ=Africa/Casablanca
            00 12 * * *

    2.4 Configuration des étapes de build
        - Sous "Build Steps," choisissez "Exécuter une ligne de commande batch Windows" et entrez la commande suivante :
            python3 C:\chemin\vers\le\projet\3D\main.py

    2.5 Enregistrement des paramètres
        - Cliquez sur "Sauver."

3. Lancement d'un test

    - Assurez que vous avez configurer les fichiers de configuration, et que vous avez bien définie la variable "path" dans les fichiers main.py et sendMail.py.
    - Pour lancer un test, cliquez sur "Lancer un build" depuis le tableau de bord Jenkins. Vous pouvez ensuite cliquer sur le nombre ou la date du test pour afficher les détails, ou cliquer sur "Sortie de la console" pour voir les détails du lancement dans la console.
    - Vous pouvez également lancer un test depuis un terminal (cmd de Windows, etc.) en utilisant la commande suivante :
        python3 C:\chemin\vers\le\projet\3D\main.py

Assurez-vous de conserver ce guide à portée de main pour référence future, et gardez en sécurité toutes les clés API et informations sensibles.

------------------------------------------------------------------------

English Version
---------------

To use this program, carefully follow these steps:

1. Installation and Configuration of Confluent Cloud Kafka

    1.1 Create a Confluent Cloud Account
        - Visit https://confluent.cloud/signup to create an account.

    1.2 Log into Your Confluent Cloud Account
        - Go to https://login.confluent.io/login?state=hKFo2SBrYVBBZHFxNTlGRVRWcURaa2x0OHRWOS13RDFpWnhYbqFupWxvZ2luo3RpZNkgTFlYQXNmcFpHdDZxOVV5VUdnX3cxNHNhYVN2YWRDMWmjY2lk2SBsMmhPcDBTMHRrU0IwVEZ0dklZZlpaOUVhS0Z2clNjNg&client=l2hOp0S0tkSB0TFtvIYfZZ9EaKFvrSc6&protocol=oauth2&cache=%5Bobject%20Object%5D&redirect_uri=https%3A%2F%2Fconfluent.cloud%2Fauth_callback&redirect_path=%2F&last_org_resource_id_map=%7B%7D&segment_anon_id=e447ddac-73be-420c-8956-ea2079ea99db&scope=openid%20profile%20email%20offline_access&response_type=code&response_mode=query&nonce=eWt0QVdya0pXUEhKTkRGMUNyQkVRa2NtZjVFaVRHRUJKa1lTekRCM0J4cg%3D%3D&code_challenge=rfZ0NoJb6oFQYwIJ-W6gUWrA4Zuy32cJ1kwxso03DTU&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtcmVhY3QiLCJ2ZXJzaW9uIjoiMS4xMi4xIn0%3D
    
    1.3 Create a New Environment
        - Click on "New Environment" and select "Begin configuration."

    1.4 Environment Configuration
        - On the configuration page, choose "AWS" as the cloud provider and "Ohio" as the region, then click "Enable."

    1.5 Create a Cluster
        - On your environment's page, click on "Create a cluster on your own" => "Begin configuration."
        - Choose "AWS" as the cloud provider again, "Ohio" as the region, and "Single Zone" as "Availability."
        - Click "Continue."

    1.6 Generate an API Key
        - Go to your cluster and click on "API Keys" => "Create Key."
        - Select "Global Access" and then "Next."
        - Click "Download and Continue." Keep this file secure, as you will need it to configure the project.

    1.7 Configure API Credentials
        - Click on "Download and Continue" to download the file containing the API key. Keep this file safe.

    1.8 Stream Governance Configuration
        - On your environment's interface, access "Stream Governance API" => "Credentials" => "Add Key."

    1.9 Create an API Key for Stream Governance
        - On the "API Credentials" interface, click on "Create Key" and then "Download and Continue."

    1.10 Configure a Kafka Topic
        - On your environment's interface, select your cluster, then click on "Topics" => "Create Topic."
        - Give the Topic a name and fill in the "Partitions" field with 3.
        - Click "Create with default" and skip the data contract definition.

    1.11 Configure the kafka_config.json file
        - In the project, access the "kafka_config.json" file in the "config" folder and fill in the following information:
        - sasl.username: Your API name (API Key*)
        - sasl.password: Your API password (API Secret*)
        - bootstrap.servers: Bootstrap server of your API

        * You will find this information in the .txt file you downloaded when creating the API Key.

2. Installation and Configuration of Jenkins

    2.1 Install Jenkins
        - Install Jenkins following the instructions provided in the official documentation: https://www.jenkins.io/doc/book/installing/windows/
        - If you encounter issues in step 3 (Service Logon Credentials), follow the steps outlined here: https://phoenixnap.com/kb/install-jenkins-on-windows#ftoc-heading-1:~:text=Note%3A%20When,the%20Properties%20window.

    2.2 Jenkins Configuration
        - After installation, access the Jenkins dashboard.
        - Click on "New Item" and enter a name.
        - Select "Build a free-style project" and click "OK."

    2.3 Schedule Builds
        - In the "Build Triggers" section, choose "Build periodically" and enter the following line:
            TZ=Africa/Casablanca
            00 12 * * *

    2.4 Configure Build Steps
        - Under "Build Steps," choose "Execute Windows batch command" and enter the following command:
            python3 C:\path\to\your\project\3D\main.py

    2.5 Save Settings
        - Click "Save".

3. Running a Test

    - Make sure you have configured the configuration files, and that you have defined the "path" variable in the main.py and sendMail.py files.
    - To run a test, click "Build Now" from the Jenkins dashboard. You can then click on the build number or date to view details, or click "Console Output" to see the launch details in the console.
    - You can also run a test from a terminal (Windows cmd, etc.) using the following command:
        python3 C:\path\to\your\project\3D\main.py

Make sure to keep this guide handy for future reference, and keep all API keys and sensitive information secure.