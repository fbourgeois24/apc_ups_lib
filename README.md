# Récupération des données d'un ups APC en usb

## Installation
Le packet `apcupsd` est nécessaire pour lire les données de l'ups. Installer avec `sudo apt-get install apcupsd`

## Utilisation
Pour récupérer les données de l'ups, lancer la commande suivante `sudo /sbin/apcaccess status`

Si l'ups est connecté il est possible de faire un check avec `apctest` (Il faut au préalable arrêter le service apcupsd)

Si l'ups est connecté les données suivantes sont renvoyées :

```
APC      : 0010431027
DATE     : 2020-11-20 20:39:02 +0100  
HOSTNAME : RaspberryPIDjango
VERSION  : 3.14.14 (31 May 2016) debian
UPSNAME  : RaspberryPIDjango
CABLE    : USB Cable
DRIVER   : USB UPS Driver
UPSMODE  : Stand Alone
STARTTIME: 2020-11-20 19:23:42 +0100  
MODEL    : Smart-UPS 1000 
STATUS   : ONLINE 
LINEV    : 233.2 Volts
LOADPCT  : 17.5 Percent
BCHARGE  : 100.0 Percent
TIMELEFT : 60.0 Minutes
MBATTCHG : 5 Percent
MINTIMEL : 3 Minutes
MAXTIME  : 0 Seconds
OUTPUTV  : 233.2 Volts
SENSE    : High
DWAKE    : -1 Seconds
DSHUTD   : 90 Seconds
LOTRANS  : 208.0 Volts
HITRANS  : 253.0 Volts
RETPCT   : 0.0 Percent
ITEMP    : 23.8 C
ALARMDEL : 30 Seconds
BATTV    : 27.7 Volts
LINEFREQ : 50.0 Hz
LASTXFER : No transfers since turnon
NUMXFERS : 0
TONBATT  : 0 Seconds
CUMONBATT: 0 Seconds
XOFFBATT : N/A
SELFTEST : NO 
STESTI   : 14 days
STATFLAG : 0x05000008
MANDATE  : 2008-12-18
SERIALNO : AS0851131933
BATTDATE : 2008-12-18
NOMOUTV  : 230 Volts
NOMBATTV : 24.0 Volts
FIRMWARE : 652.18.I USB FW:7.3
END APC  : 2020-11-20 20:39:20 +0100  
```

Si l'ups n'est pas connecté, les données suivantes sont renvoyées :

```
APC      : 001,022,0593
DATE     : 2020-11-27 07:37:07 +0000  
HOSTNAME : pihole
VERSION  : 3.14.14 (31 May 2016) debian
UPSNAME  : pihole
CABLE    : USB Cable
DRIVER   : USB UPS Driver
UPSMODE  : Stand Alone
STARTTIME: 2020-11-21 15:14:48 +0000  
STATUS   : COMMLOST 
MBATTCHG : 5 Percent
MINTIMEL : 3 Minutes
MAXTIME  : 0 Seconds
LASTXFER : No transfers since turnon
NUMXFERS : 1
XONBATT  : 2020-11-26 09:03:47 +0000  
TONBATT  : 0 Seconds
CUMONBATT: 12 Seconds
XOFFBATT : 2020-11-26 09:03:59 +0000  
LASTSTEST: 2020-11-26 09:03:47 +0000  
SELFTEST : NO
STATFLAG : 0x05000108
END APC  : 2020-11-27 07:37:21 +0000
```

Le statut peut avoir les valeurs :
- ONLINE : communication avec l'up OK et présence du secteur à l'entrée
- ONBATT : communication avec l'up OK mais absence du secteur à l'entrée (sur batterie)
- COMMLOST : pas de communication avec l'ups

## Utilisation de la bibliothèque

```python
import ups_apc_lib
ups_data = ups_apc_lib.ups_apc_read_data()
```
La fonction renvoie un dictionnaire avec les informations listées plus haut au format suivant:
```python
"nom_paramètre": {"valeur": valeur, "unité": unité} 
# La clé unité est toujours présente et = "" si pas d'unité
```
Les valeurs date et heure sont au format datetime.datetime
Les valeurs numériques sont au format float