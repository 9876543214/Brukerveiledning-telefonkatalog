# Brukerveiledning for oppsett av telefonkatalog i Raspberry Pi

Denne brukerveiledningen antar at du:
- Har ferdig installert ubuntu operativsystem på Raspberry Pi.
- Vet hva CTRL og ALT er.

## 1. oppsett av Raspberry Pi

1. Åpne terminalen i Raspberry Pi.

CTRL + ALT + T

2. Skriv inn i terminalen.

```bash
sudo apt update
```
```bash
sudo apt upgrade
```

3. Sett opp brannmur.

```bash
sudo apt install ufw
```
```bash
sudo ufw enable
```
```bash
sudo ufw allow ssh
```

4. Skru på SSH.

```bash
sudo apt install openshh-server
```
```bash
sudo systemctl enable ssh
```
```bash
sudo systemctl start ssh
```

5. Finn ip-adressen din.

```bash
ip a
```

Hvis du har kablet nettverk, vil IP vises ved eth0: linje. Hvis du kun har trådløst, vil ip vises ved wlan0: linje.  
Husk på denne ip-adressen.

6. Installer nødvendige programmer.

- Python
```bash
sudo apt install python3-pip
```
```bash
sudo apt install git
```
```bash
sudo apt install mariadb-server
```
```bash
sudo mysql_secure_installation
```

7. Oppdater igjen.

```bash
sudo apt update
```
```bash
sudo apt upgrade
```

## 2. Styr maskinen fra laptop med SSH

Raspberrry Pi må være skrudd på og koblet til samme nettverk som laptopen. 

1. Åpne terminalen på laptopen.

CTRL + ALT + T

2. Koble sammen maskinene.

```bash
ssh brukernavn@0.0.0.0
```

Fra nå av kan du skrive direkte inn i terminalen på laptopen.

Bytt ut "brukernavn" med ditt brukernavn og "0.0.0.0" med ip-adressen som ble funnet i steg 1.5.

## 3. Sett opp database i mariadb.

1. Åpne mariadb.

```bash
sudo mariadb
```

2. følg instruksene i filen "mariadb-database.sql".

## 4. Last ned og kjør telefonkatalog.

1. last ned filen "telefonkatalog.py".

2. Endre verdier i filen.

- Åpne "telefonkatalog.py"
- Endre brukernavn og passord til brukeren i mariadb.
- Endre IP-adresse til det du har på Raspberry Pi.

3. Kjør filen.
