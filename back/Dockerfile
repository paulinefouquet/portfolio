# Starting from an alpine image would save us 50 MB, but it would also
# considerably slow the install process
FROM python:3.11-slim

# Installation des dépendances système pour PyMuPDF
RUN apt-get update && apt-get install -y \
    build-essential \
    libx11-dev \
    libxtst-dev \
    libjpeg-dev \
    libpng-dev \
    zlib1g-dev \
    libffi-dev \
    poppler-utils \
    pkg-config

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .
# Note that we copy the file requirements.txt twice. The reason is,
# everything that stays constant from a docker build to another is cached,
# and therefore not done again.

EXPOSE 8000

CMD ["python", "chat_api.py"]
