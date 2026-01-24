## CiaoMondoApp

Una semplice app Android scritta in Python con Kivy. Mostra una casella di testo e un pulsante. Quando premi il pulsante, compare il messaggio "Ciao mondo".

## 📱 Screenshot

*(aggiungi uno screenshot qui dopo la compilazione)*

## 🧱 Requisiti

- Python 3.10+
- Kivy
- Buildozer
- Android SDK/NDK (gestiti da Buildozer)

## 🚀 Come compilare l'APK

1. Clona il progetto o copia i file `main.py` e `buildozer.spec`
2. Apri un terminale nella cartella del progetto
3. Esegui:

```bash
buildozer init        # solo se non hai già il file .spec
buildozer -v android debug Prova
Prova
