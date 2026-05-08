#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(username='subhash').exists() or User.objects.create_superuser('subhash', 'dhaniyalasubhash@gmail.com', 'Subhash@123')" | python manage.py shell