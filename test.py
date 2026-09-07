import unittest
from translate_history import save_translate_history
class TestHistory(unittest.TestCase):

    def test_save_history(self):
        save_translate_history(
            "中文",
            "英语",
            "你好",
            "Hello"
        )
        with open("translation_history.txt", "r", encoding="utf-8") as f:
            content = f.read()

        # 检查文件中是否包含正确内容
        self.assertIn("源语言：中文", content)
        self.assertIn("目标语言：英语", content)
        self.assertIn("原文：你好", content)
        self.assertIn("译文：Hello", content)


if __name__ == "__main__":
    unittest.main()