## Backend Web API Case – FastAPI

Bu proje, bir teknik case kapsamında geliştirilmiş basit bir Backend Web API uygulamasıdır.
Kullanıcı kayıt ve giriş işlemlerini güvenli şekilde gerçekleştirmeyi amaçlar.

## 🚀 Kullanılan Teknolojiler

-Python 3.11

-FastAPI

-SQLAlchemy

-Pydantic

-PostgreSQL (NeonDB)

-Passlib + bcrypt

## 📁 Proje Yapısı

app/

├── main.py        # API endpoint'leri

├── database.py    # Veritabanı bağlantısı

├── models.py     # ORM modelleri

├── schemas.py    # Request / response şemaları

├── crud.py       # Veritabanı işlemleri

├── security.py   # Şifre hash & doğrulama

## ⚙️ Kurulum

pip install -r requirements.txt
uvicorn app.main:app --reload


Swagger:

http://127.0.0.1:8000/docs

## 🔐 Ortam Değişkenleri

.env dosyası:

DATABASE_URL=postgresql+psycopg2://<user>:<password>@<host>/<database>?sslmode=require

## 📌 API Endpoint’leri

-Kullanıcı Kayıt

-POST /register

{
  "email": "user@example.com",
  "password": "123456",
  "password_repeat": "123456"
}

-Kullanıcı Giriş

-POST /login

{
  "email": "user@example.com",
  "password": "123456"
}


Başarılı:

{
  "status": "login successful"
}


Hatalı:

{
  "detail": "Invalid email or password"
}

## 🔒 Güvenlik

-Şifreler plain text olarak saklanmaz

-bcrypt ile hash’lenir

-Login sırasında hash doğrulaması yapılır

## 🧠 Mimari

-Validation → schemas

-Veritabanı işlemleri → crud

-Güvenlik → security

-HTTP katmanı → main


## Canlı API

Base URL:
https://apicase-1.onrender.com/

Swagger:
https://apicase-1.onrender.com/docs
