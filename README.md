# English Version:

# PasNevesht

A Django-based web application that allows users to schedule and automatically send emails at a future time. The system runs a background scheduler that continuously checks for pending messages and delivers them when their scheduled time arrives.

---

## Features

* User authentication system
* Create and manage scheduled email messages
* Automatic email delivery using a background scheduler
* Message status tracking (`scheduled`, `not_scheduled`, `sent`, `failed`)
* Contact auto-generation from recipients
* Account settings (username/email/password management)
* Account deletion with confirmation
* Responsive dashboard UI

---

## How It Works

When a user creates a message:

1. The message is saved in the database with a scheduled time.
2. A background scheduler (APScheduler) runs every few seconds.
3. It checks for messages where:

   * status = `scheduled`
   * scheduled_date <= current time
4. Matching messages are sent via email using Django’s `send_mail`.
5. After successful delivery:

   * status is updated to `sent`
   * sent time is recorded

---

## ⚙️ Tech Stack

* Python 3
* Django 6
* SQLite (default database)
* APScheduler (background task execution)
* SMTP (Gmail) for email delivery
* HTML / CSS (Django templates)
* JavaScript (UI interactions)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MaedehSoleymani/PasNevesht.git
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / Mac:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py makemigration
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Run development server

```bash
python manage.py runserver
```

---

## 📧 Email Configuration

Update your environment variables or settings file:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "your_app_password"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

---

## Scheduler System

The system uses **APScheduler (BackgroundScheduler)**:

* Runs inside Django app lifecycle
* Starts automatically via `AppConfig.ready()`
* Executes every few seconds
* Checks database for pending messages

⚠️ Note: This approach is suitable for development and small-scale projects. For production, use Celery + Redis or a system-level scheduler like Cron.

---

## ⚠️ Important Notes

* Scheduler runs in memory → it resets on server restart
* Do NOT run multiple server instances in production (can cause duplicate sending)
* Use proper production setup (Gunicorn + Celery recommended)
* Timezone consistency is important for scheduled delivery

---

## Project Structure (Core Parts)

```
accounts/
letters/
website/
blog/
pasnevesht/
    settings.py
    wsgi.py
    urls.py
```

# نسخه فارسی

# پس‌نوشت (PasNevesht)

یک وب‌اپلیکیشن مبتنی بر Django که به کاربران اجازه می‌دهد ایمیل‌ها را زمان‌بندی کنند و به‌صورت خودکار در آینده ارسال شوند. سیستم شامل یک زمان‌بند پس‌زمینه است که به‌طور مداوم پیام‌های در انتظار را بررسی کرده و در زمان مشخص‌شده آن‌ها را ارسال می‌کند.

---

## ویژگی‌ها

* سیستم احراز هویت کاربران
* ایجاد و مدیریت پیام‌های ایمیل زمان‌بندی‌شده
* ارسال خودکار ایمیل با استفاده از scheduler پس‌زمینه
* پیگیری وضعیت پیام‌ها (`scheduled`, `not_scheduled`, `sent`, `failed`)
* ساخت خودکار مخاطب از گیرندگان ایمیل
* تنظیمات حساب کاربری (تغییر نام کاربری، ایمیل و رمز عبور)
* حذف حساب کاربری همراه با تأیید
* رابط کاربری ریسپانسیو برای داشبورد

---

## نحوه عملکرد سیستم

زمانی که کاربر یک پیام ایجاد می‌کند:

1. پیام در دیتابیس ذخیره می‌شود همراه با زمان ارسال آینده
2. یک scheduler پس‌زمینه (APScheduler) هر چند ثانیه اجرا می‌شود
3. بررسی می‌کند پیام‌هایی که:

   * وضعیت آن‌ها `scheduled` است
   * زمان ارسالشان کمتر یا مساوی زمان فعلی است
4. پیام‌های مطابق شرایط از طریق `send_mail` جنگو ارسال می‌شوند
5. بعد از ارسال موفق:

   * وضعیت پیام به `sent` تغییر می‌کند
   * زمان ارسال ثبت می‌شود

---

## ⚙️ تکنولوژی‌های استفاده‌شده

* Python 3
* Django 6
* SQLite (پایگاه داده پیش‌فرض)
* APScheduler (اجرای وظایف پس‌زمینه)
* SMTP (Gmail) برای ارسال ایمیل
* HTML / CSS (قالب‌های Django)
* JavaScript (تعاملات UI)

---

## نصب و راه‌اندازی

### 1. کلون کردن پروژه

```bash
git clone https://github.com/MaedehSoleymani/PasNevesht.git
```

---

### 2. ساخت محیط مجازی

```bash
python -m venv venv
```

---

### 3. فعال‌سازی محیط مجازی

**ویندوز:**

```bash
venv\Scripts\activate
```

**لینوکس / مک:**

```bash
source venv/bin/activate
```

---

### 4. نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

---

### 5. اجرای مهاجرت‌ها

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. ساخت ادمین

```bash
python manage.py createsuperuser
```

---

### 7. اجرای سرور

```bash
python manage.py runserver
```

---

## 📧 تنظیمات ایمیل

تنظیمات SMTP را در فایل تنظیمات یا متغیرهای محیطی وارد کنید:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "your_app_password"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

---

## سیستم Scheduler

این پروژه از **APScheduler (BackgroundScheduler)** استفاده می‌کند:

* داخل چرخه اجرای Django اجرا می‌شود
* به‌صورت خودکار از طریق `AppConfig.ready()` فعال می‌شود
* هر چند ثانیه اجرا می‌شود
* دیتابیس را برای پیام‌های زمان‌بندی‌شده بررسی می‌کند

⚠️ نکته مهم: این روش برای توسعه و پروژه‌های کوچک مناسب است. برای محیط production بهتر است از Celery + Redis یا Cron استفاده شود.

---

## ⚠️ نکات مهم

* Scheduler در حافظه اجرا می‌شود → با ریستارت سرور از بین می‌رود
* اجرای چند نمونه سرور می‌تواند باعث ارسال دوبل ایمیل شود
* در production باید از معماری مناسب (مثل Gunicorn + Celery) استفاده شود
* هماهنگی timezone برای ارسال صحیح پیام‌ها ضروری است

---

## ساختار پروژه (هسته اصلی)

```
accounts/
letters/
website/
blog/
pasnevesht/
    settings.py
    wsgi.py
    urls.py
```
