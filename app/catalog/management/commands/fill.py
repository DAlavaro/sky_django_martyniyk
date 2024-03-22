from django.core.management import BaseCommand
from app.catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Clear existing records from the models
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_one = Category.objects.create(
            name='Банковский сектор',
            description='Банковский сектор – это ключевая составляющая финансовой системы любой страны, включающая в себя банки различных типов и специализаций. Банки выполняют разнообразные функции, такие как прием вкладов, предоставление кредитов, операции с ценными бумагами, обмен валюты, расчетно-кассовое обслуживание клиентов и многое другое. Банковский сектор регулируется национальным банком или финансовым регулятором и может включать частные, государственные, корпоративные и международные банковские учреждения. Он играет важную роль в экономике, обеспечивая мобилизацию и распределение финансовых ресурсов.'
        )

        category_two = Category.objects.create(
            name='Нефтегазовый сектор',
            description='Нефтегазовый сектор – это отрасль экономики, которая занимается разведкой, добычей, переработкой, транспортировкой и продажей нефти, природного газа и сопутствующих продуктов. Эта отрасль включает компании, работающие на различных этапах производственной цепочки, от поиска и разработки месторождений до реализации нефтепродуктов и газа конечным потребителям.'
        )

        product_list = [
            {
                'name': 'Сбербанк',
                'description': 'СберБанк — крупнейший банк в России, Центральной и Восточной Европе, один из ведущих международных финансовых институтов. Сбер также является системно значимым банком и одной из крупнейших экосистем страны.',
                'image': 'sber.png',
                'category': category_one,
                'price': 293,
            },
            {
                'name': 'Лукойл',
                'description': 'ЛУКОЙЛ — одна из крупнейших нефтегазовых компаний в мире, на ее долю приходится 2% мировой добычи нефти и 1% доказанных запасов углеводородов. Компания представлена более чем в 30 странах, а в России ее деятельность охватывает около 70% регионов.',
                'image': 'lukoil.png',
                'category': category_two,
                'price': 8500,
            },
        ]

        products_for_create = []

        for product_item in product_list:
            product, created = Product.objects.get_or_create(
                name=product_item['name'],
                description=product_item['description'],
                category=product_item['category'],
                image=f'products/{product_item["image"]}',
                price=product_item['price'],
            )
            if created:
                products_for_create.append(product)
