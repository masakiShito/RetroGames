# tests/test_tetris.py
import unittest
from retrogames import play_tetris

class TestTetris(unittest.TestCase):
    def test_play_tetris(self):
        play_tetris()  # This will just print the placeholder message

if __name__ == "__main__":
    unittest.main()
