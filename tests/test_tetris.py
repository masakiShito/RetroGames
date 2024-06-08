# tests/test_tetris.py
import unittest
from retrogames.tetris import play_tetris

class TestTetris(unittest.TestCase):
    def test_play_tetris(self):
        # モックの標準スクリーンを作成するためにcursesを使用します
        import curses
        curses.wrapper(play_tetris)  # テストとしてcurses.wrapperを呼び出します

if __name__ == "__main__":
    unittest.main()
