from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        category_list = [
            {'title': 'Планшеты', 'description': 'Графические планшеты'},
            {'title': 'Мониторы', 'description': 'Графические мониторы'},
            {'title': 'B2B', 'description': 'Планшеты для электронных подписей'},
            {'title': 'Аксессуары', 'description': 'Аксессуары'}
        ]
        Category.objects.all().delete()

        categories_for_create = []

        for categories in category_list:
            categories_for_create.append(
                Category(**categories)
            )
        Category.objects.bulk_create(categories_for_create)
        