# Temel hafif Python imajı
FROM python:3.13-slim

# Çalışma dizinini ayarla
WORKDIR /app

# AutoGluon'un ihtiyaç duyduğu sistem bağımlılıklarını kur (OpenMP için libgomp1)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Gereksinimleri kopyala ve kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Model klasörü, app.py ve diğer tüm dosyaları konteynere kopyala
COPY . .

# API'nin dışarıya açılacağı port
EXPOSE 8000

# FastAPI sunucusunu (uvicorn) başlat
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]