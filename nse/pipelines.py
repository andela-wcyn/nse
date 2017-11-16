# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from nse.app.spreadsheet import GoogleSpreadSheets


class NsePipeline(object):
    def process_item(self, item, spider):
        spread_sheet = GoogleSpreadSheets()
        data_list = [item.get('date'), item.get('name'), item.get('volume'),
                     item.get('high'), item.get('low'),
                     item.get('last_traded_price'), item.get('prev_price'),
                     item.get('change')]
        spread_sheet.append_row(data_list)
        return item
