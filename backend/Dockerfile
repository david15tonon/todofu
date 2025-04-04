FROM python:3.9

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    gcc \
    libc-dev \
    libffi-dev \
    libssl-dev \
    ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN update-ca-certificates --fresh

COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 3001

CMD ["python", "./src/server.py"]