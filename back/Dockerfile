# Starting from an alpine image would save us 50 MB, but it would also
# considerably slow the install process
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# The requirements.txt file is small so we could write the dependencies
# directly, like `pip install --no-cache-dir fastapi ...`
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
# Note that we copy the file requirements.txt twice. The reason is,
# everything that stays constant from a docker build to another is cached,
# and therefore not done again.

EXPOSE 8000

CMD ["python", "chat_api.py"]
