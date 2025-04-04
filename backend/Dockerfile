FROM python:3.9 
WORKDIR /usr/src/app

# Installer les dépendances système avant les packages Python
RUN apt-get update && apt-get install -y \
    python3-dev \
    gcc \
    libc-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

# Installer pip et les dépendances avec les bons flags
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 3001

CMD ["python", "./src/server.py"]