#!/usr/bin/python3

import sys
import unittest

def debug(str):
    print("Debug: {}".format(str))
    pass


class TestTelegram(unittest.TestCase):
    def test_001(self):
        (buffer, consumed) = Telegram().buffered_truncate("", 9, ["this", "is", "an", "test"])

        self.assertEqual(buffer, "this is")
        self.assertEqual(consumed, 2)
    
    def test_002(self):
        (buffer, consumed) = Telegram().buffered_truncate("", 1, [])

        self.assertEqual(buffer, "")
        self.assertEqual(consumed, 0)

class Telegram:
    def __init__(self):
        pass

    def buffered_truncate(self, buffer, buffer_len, words):
        consumed = 0

        for w in words:
            if (len(buffer) == 0) and (len(words[consumed]) <= buffer_len):
                buffer = words[consumed]
                consumed = consumed + 1
            elif len(buffer) + len(words[consumed]) + 1 <= buffer_len:
                buffer = buffer + " " + words[consumed]
                consumed = consumed + 1
            else:
                break

        return (buffer, consumed)

def main():
    lines = [x.strip() for x in sys.stdin]
    buffer = ""

    tg = Telegram()

    for l in lines:
        line = l.split(' ')

        while line:
            (buffer, consumed) = tg.buffered_truncate(buffer, 14, line)

            if consumed < len(line):
                print(buffer)
                line = line[consumed:]
                buffer = ""
            else:
                line = []
            
            debug("consumed -> {}, buffer -> {}, L -> {}".format(consumed, buffer, line))
        
    if buffer:
        print(buffer)


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
