# 20.1 Знакомство с Django домашнее задание
## Задание 1
Подключите СУБД PostgreSQL для работы в проекте. Для этого:
- [x] Создайте базу данных в ручном режиме.
- [x] Внесите изменения в настройки подключения.
## Задание 2
В приложении каталога создайте модели:
- [ ] Product,
- [ ] Category.
Опишите для них начальные настройки.
## Задание 3
Для каждой модели опишите следующие поля:
- [x] Product:
	- [x] наименование,
	- [x] описание,
	- [x] изображение (превью),
	- [x] категория,
	- [x] цена за штуку,
	- [x] дата создания,
	- [x] дата последнего изменения
- [x] Category:
	- [x] наименование,
	- [x] описание.
>Для поля с изображением необходимо добавить соответствующие настройки в проект, а также установить библиотеку для работы с изображениями  `Pillow`.
## Задание 4
Перенесите отображение моделей в базу данных с помощью инструмента миграций. Для этого:
- [x] Создайте миграции для новых моделей.
- [x] Примените миграции.
- [x] Внесите изменения в модель категорий, добавьте поле `created_at`, примените обновление структуры с помощью миграций.
- [x] Откатите миграцию до состояния, когда поле `created_at` для модели категории еще не существовало, и удалите лишнюю миграцию.
## Задание 5
- [ ] Для моделей категории и продукта настройте отображение в административной панели. Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию.
- [ ] При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, а также осуществлять поиск по названию и полю описания
## Задание 6
- [ ] Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот.
- [ ] Сформируйте фикстуры для заполнения базы данных.
- [ ] Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от старых данных.
>Последний пункт можно реализовать в связке с инструментом работы с фикстурами, можно описать вставку данных отдельными запросами.
## *Дополнительное задание*
- [ ] В контроллер отображения главной страницы добавьте выборку последних 5 товаров и вывод их в консоль.
- [ ] Создайте модель для хранения контактных данных и попробуйте вывести данные, заполненные через админку, на страницу с контактами.
> Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.