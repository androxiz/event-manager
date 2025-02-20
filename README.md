# event-manager REST-API
Django REST-Api for Event Management

---
## Як запустити
1. Клонуйте репозиторій та перейдіть до директорії проекта:
   ```sh
   git clone https://github.com/androxiz/event-manager/
   cd event-manager
2. Створіть файл .env і вкажіть в ньому змінні оточення.
    ```
    DJANGO_SECRET_KEY=секретний ключ
    DJANGO_DEBUG=True (дефолтне)
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=почта
    EMAIL_HOST_PASSWORD=ваш пароль від почти (Використовуйте пароль застосунку)
    EMAIL_USE_TLS=True (дефолтне)
3. Запустіть проект командою
   ```
   docker-compose up --build -d
---
## Документація
Документація доступна по (після запуску проекта):
- [Swagger UI](api/schema/swagger-ui/)
- [Redoc](api/schema/redoc/)
- [Завантажити файл документації](api/schema/)
---
## PS
- Щоб війти в акаунт користувача необхідно робити запити с Basic Auth (наприклад в Postman)
- Для реєстрації нового акаунту необхідно відправити POST request на auth/user/ . Приклад:
  ```sh
  {
        "username": "username",
        "password": "password",
        "email": "email" (не обов'язково, але тоді не спрацює відправка повідомлення на пошту)
  }
- Я вирішив залишити бд в проекті, щоб було зручніше протестувати API.
    ```
      Адмінка:
          login: admin
          pass: 123
      Користувач без імейлу:
          login: created_user
          pass: 12345678AAA

