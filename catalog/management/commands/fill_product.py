from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        pen_tablets = Category.objects.get(title='Планшеты')
        pen_displays = Category.objects.get(title='Мониторы')
        b2b_displays = Category.objects.get(title='B2B')
        accessories = Category.objects.get(title='Аксессуары')

        products_list = [
            {'title': 'Inspiroy 2S', 'description': 'Графический планшет с новым пером Pentech 3.0',
             'image': 'media/Inspiroy2S_pink.jpg', 'category': pen_tablets, 'price': 15590.0},
            {'title': 'Kamvas 24 Plus', 'description': 'Графический монитор с экраном 2,5K IPS, c пером PW517',
             'image': 'media/k24p-3-1.png', 'category': pen_displays, 'price': 25000.0},
            {'title': 'HUION DS510', 'description': 'Дисплей для электронной подписи',
             'image': 'media/HUION DS510.png', 'category': b2b_displays, 'price': 17590.0},
            {'title': 'Pen Display Stand ST300', 'description': 'Подставка для графического монитора',
             'image': 'media/foldable-stand-st300.jpg', 'category': accessories, 'price': 6000.0}
        ]

        Product.objects.all().delete()

        products_for_create = []

        for product in products_list:
            products_for_create.append(
                Product(**product)
            )
        Product.objects.bulk_create(products_for_create)