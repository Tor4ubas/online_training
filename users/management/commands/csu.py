from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import User


class Command(BaseCommand):
    help = 'Создает фикстуру для созданных групп'
    def handle(self, *args, **options):
        # Создание группы модераторов
        moderator_group, created = Group.objects.get_or_create(name='Модераторы')

        # Создание пользователя и добавление в группы
        user = User.objects.create(
            email='alex1029@yandex.ru',
            first_name='Admin',
            last_name='Adminov',
            is_staff=True,
            is_active=True
        )
        user.set_password('123qwe456rty')
        user.save()
        user.groups.add(moderator_group)
