from hiflow import Bot
import unittest

class BotTest(unittest.TestCase):
    def test_bot(self):
        bot = Bot()
        bot.send("this is a test message")
