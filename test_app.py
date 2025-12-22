import unittest
import app
class TestApp(unittest.TestCase):
    def test_say_hello(self):
        result = app.say_hello()
        self.assertEqual(result, "Hello from Jenkins CI/CD pipeline")
if __name__ == "__main__":
    unittest.main()
