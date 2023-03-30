# Bank Bottom

Bank Bottom - это проект, агрегирующий статистику по негативным отзывам о банках из сети.
Пока банки из РФ. 
Это проект монолитной архитектуры, разработанный на Python. Ядро - Flask + DB SQLlite. Сбор статистики осуществляется по расписанию, через очередь задач в hash-value db Redis с размещением в Docker.
Состоит из web-части, отображающей графики статистики негативных отзвовов за неделю, статистику по категориям банковских продуктов. У проекта есть REST-API, для получения общей статистики негативных и статистики по категориям за неделю. Для проекта создан бот @bank_bottom_bot, возвращающий раз в неделю статистику по отзывам, которую запрашивает через REST-API.
Опционально добавлена возможность публикации отзывов с сохранением отзыва в БД.

Bank Bottom is a project that aggregates statistics on negative reviews about banks from the internet, currently focusing on banks in Russia. It is a monolithic architecture project developed in Python, with Flask + DB SQLlite as the core. Statistics collection is performed on a schedule, through a task queue in the hash-value db Redis, deployed in Docker. It consists of a web component that displays graphs of negative review statistics for the week and statistics on categories of banking products. The project has a REST API for obtaining overall negative statistics and weekly statistics by categories. Additionally, a bot @bank_bottom_bot was created for the project, which returns weekly statistics on reviews requested via the REST API. Optionally, the ability to publish reviews with the preservation of the review in the database has been added.

## Истрия проекта
Это Pat-Project. Создан так как многие сайты с банковскими отзывами не публикую статистику по отзывам, искажая информацию о качестве банковских услуг. На этапе MVP собираются негативные отзывы по основным банковским продуктам: Кредиты, Депозиты, Карты, Сервис и т.д.

This is Pat-Project. It was created because many websites with bank reviews do not publish statistics on reviews, distorting information about the quality of banking services. At the MVP stage, negative reviews are collected for the main banking products: Credits, Deposits, Cards, Services, etc.

## Архитектура решения
![Архитектура решения](.bank_bottom_proj/Arch Solution.png)

## Интерфейсы

### Bot
![bot](.bank_bottom_proj/tg.png)

### UI
![UI](.bank_bottom_proj/ui.png)