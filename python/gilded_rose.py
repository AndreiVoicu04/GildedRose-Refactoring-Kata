# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def is_sulfuras(self, item):
        return "Sulfuras" in item.name

    def is_conjured(self, item):
        return item.name.find("Conjured") == 0

    def is_backstage_passes(self, item):
        return item.name.find("Backstage passes") == 0

    def is_aged_brie(self, item):
        return "Aged Brie" in item.name

    def update_quality(self):
        for item in self.items:
            # sulfuras quality&sell_in don't change
            if self.is_sulfuras(item):
                continue

            item_quality_difference = -1
            if self.is_aged_brie(item) or self.is_backstage_passes(item):
                item_quality_difference = 1

            if self.is_backstage_passes(item):
                if item.sell_in < 11:
                    item_quality_difference += 1
                if item.sell_in < 6:
                    item_quality_difference += 1

            item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if self.is_backstage_passes(item):
                    item.quality = 0
                    continue
                if self.is_aged_brie(item):
                    item_quality_difference += 1
                else:
                    item_quality_difference -= 1

            if self.is_conjured(item):
                item_quality_difference *= 2

            item.quality = item.quality + item_quality_difference

            if item.quality < 0:
                item.quality = 0
            elif item.quality > 50:
                item.quality = 50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
