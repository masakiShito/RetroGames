# tests/test_snake.py
import unittest
from retrogames.snake import play_snake

class TestSnake(unittest.TestCase):
    def test_play_snake(self):
        # モックの標準スクリーンを作成するためにcursesを使用します
        import curses
        curses.wrapper(play_snake)  # テストとしてcurses.wrapperを呼び出します

if __name__ == "__main__":
    unittest.main()
