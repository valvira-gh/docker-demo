# Käytetään viimeisintä Python-imagea
FROM python:3.13.2

# Määritellään paikallinen työhakemisto
WORKDIR /app

# Kopioidaan riippuvuudet ja asennetaan ne
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopioidaan sovelluksen lähdekoodi
COPY app /app

# Asetetaan käynnistyskomento
CMD ["python", "/app/main.py"]