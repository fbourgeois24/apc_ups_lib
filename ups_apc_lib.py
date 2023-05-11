import subprocess
from datetime import datetime as dt

def ups_apc_read_data():	
	ups_data_raw = subprocess.run("apcaccess status", shell=True, capture_output=True, text=True)

	if ups_data_raw.returncode != 0:
		# Erreur de lecture des infos de l'ups
		return None

	# Création d'un dictionnaire avec les infos
	ups_data = {}
	for row in ups_data_raw.stdout.split("\n"):
		if row == "":
			# On passe les lignes vides
			continue
		nom_paramètre = row[:9].strip()
		valeur_paramètre = row[11:].strip()
		unité = ""
		
		if nom_paramètre in ('DATE', 'STARTTIME', 'END APC'):
			# Le paramètre est un date et heure, on l'interprête comme tel
			valeur_paramètre = dt.strptime(valeur_paramètre, "%Y-%m-%d %H:%M:%S %z")
		elif nom_paramètre in ('LINEV', 'LOADPCT', 'BCHARGE', 'TIMELEFT', 'MBATTCHG', 'MINTIMEL','MAXTIME','OUTPUTV','DWAKE','DSHUTD','LOTRANS',
			'HITRANS','RETPCT','ITEMP','ALARMDEL','BATTV','LINEFREQ','TONBATT','CUMONBATT','STESTI','NOMOUTV','NOMBATTV',):
			# Le paramètre est une valeur numérique suivie de son unité, on l'interprête comme tel
			valeurs = valeur_paramètre.split(" ")
			unité = valeurs[1]
			valeur_paramètre = float(valeurs[0])

		ups_data[nom_paramètre] = {"valeur": valeur_paramètre, "unité": unité}

	return ups_data