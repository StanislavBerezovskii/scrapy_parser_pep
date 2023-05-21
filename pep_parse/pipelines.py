from scrapy.exceptions import DropItem

import csv
from collections import Counter
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, FILENAME, RESULTS_DIR, TIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.total = Counter()
        self.time = dt.now().strftime(TIME_FORMAT)

    def process_item(self, item, spider):
        self.total[item['status']] += 1
        if 'status' not in item:
            raise DropItem('Status не найден')
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR
        file_path = results_dir / FILENAME.format(self.time)
        with open(file_path, 'w', encoding='utf-8') as file:
            writer = csv.writer(
                file, dialect='unix',
                quoting=csv.QUOTE_NONE
            )
            writer.writerow(['Статус', 'Количество'])
            self.total['Total'] = sum(self.total.values())
            writer.writerows(self.total.items())
