# Парсер документов PEP на базе Scrapy

[Описание](#описание) /
[Развернуть локально](#развернуть-локально) /
[Документация](#документация) /
[Автор](#автор) /


## Описание

Парсер [scrapy_parser_pep](https://github.com/StanislavBerezovskii/scrapy_parser_pep) собирает документы PEP с ресурса [https://peps.python.org/](https://peps.python.org/) и формирует результат двух типов:

* pep_{datetime}.csv - список всех PEP (номер, название и статус)
* status_summary_{datetime}.csv - сводка по статусам PEP, сколько найдено документов в каждом статусе (статус, количество)


## Развернуть локально

Склонировать проект, создать виртуальное окружение и проинициализировать зависимости:

```bash
git clone https://github.com/StanislavBerezovskii/scrapy_parser_pep.git
cd scrapy_parser_pep
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## Документация

Парсер запускается из root-директории проекта командой

```bash
scrapy crawl pep
```

## Автор

https://github.com/StanislavBerezovskii