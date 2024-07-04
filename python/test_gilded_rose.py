# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


    def test_aged_brie(self):
        items = [
            Item("Aged Brie", 3, 49),
            Item("Aged Brie", 0, 0)
        ]
        glided_rose = GildedRose(items)
        for i in range(2):
            glided_rose.update_quality()

        self.assertEqual(50, items[0].quality)
        self.assertEqual(4, items[1].quality)

        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(-2, items[1].sell_in)

    def test_conjured_aged_brie(self):
        items = [
            Item("Conjured Aged Brie", 3, 0),
            Item("Conjured Aged Brie", 0, 0)
        ]

        gilded_rose = GildedRose(items)
        for i in range(2):
            gilded_rose.update_quality()

        self.assertEqual(4, items[0].quality)
        self.assertEqual(8, items[1].quality)

    def test_sulfuras(self):
        items = [
            Item("Sulfuras", 0, 3),
            Item("Sulfuras Mega", 1, 30)
        ]

        glided_rose = GildedRose(items)
        glided_rose.update_quality()

        self.assertEqual(3, items[0].quality)
        self.assertEqual(30, items[1].quality)

        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(1, items[1].sell_in)

    def test_backstage_passes(self):
        items = [
            Item("Backstage passes to a TAFKA", 12, 5),
            Item("Backstage passes Coldplay", 10, 5),
            Item("Backstage passes Guns n Roses", 5, 5),
            Item("Backstage passes Metallica", 0, 5)
        ]
        glided_rose = GildedRose(items)
        glided_rose.update_quality()

        self.assertEqual(6, items[0].quality)
        self.assertEqual(7, items[1].quality)
        self.assertEqual(8, items[2].quality)
        self.assertEqual(0, items[3].quality)

        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(9, items[1].sell_in)
        self.assertEqual(4, items[2].sell_in)
        self.assertEqual(-1, items[3].sell_in)

    def test_elixirs(self):
        items = [
            Item("Elixir of the Mongoose", 3, 1)
        ]

        gilded_rose = GildedRose(items)

        for i in range(2):
            gilded_rose.update_quality()

        self.assertEqual(0, items[0].quality)



if __name__ == '__main__':
    unittest.main()
