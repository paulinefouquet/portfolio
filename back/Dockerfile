# Starting from an alpine image would save us 50 MB, but it would also
# considerably slow the install process
FROM python:3.11-slim

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
