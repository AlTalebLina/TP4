import os

# Définitions en dur des commits "good" et "bad"
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
badhash = "c1a4be04b972b6c17db242fc37752ad517c29402"

# Démarrer le bisect avec les commits indiqués
os.system(f"git bisect start {badhash} {goodhash}")

# Lancer automatiquement la commande de test sur chaque commit
os.system("git bisect run python manage.py test")
