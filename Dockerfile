FROM python:3.10-slim
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Pre-download NLTK data to avoid runtime downloads
RUN python -m nltk.downloader stopwords >/dev/null 2>&1 || true

ENV PORT=8080
EXPOSE 8080

CMD ["gunicorn", "app:APP", "--bind", "0.0.0.0:8080", "--workers", "2"]
