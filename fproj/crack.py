import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fproj.settings')
django.setup()

from django.contrib.auth.hashers import check_password

hash_to_crack = 'pbkdf2_sha256$1200000$yrhfy7ZiswDKknFS6WSC9E$400LJeZp9KdMNQQnS8zr3RpoCQpYaE299KecYwrVwdo='

passwords = [
    '123456', 'password', 'qwerty', 'admin123',
    'qwe123qwe123', '1q2w3e4r','admin', 'letmein', 'welcome'
]

print('🔍 Начинаем подбор...')
for pwd in passwords:
    if check_password(pwd, hash_to_crack):
        print(f'✅ ПАРОЛЬ НАЙДЕН: {pwd}')
        break
else:
    print('❌ Пароль не найден в списке.')