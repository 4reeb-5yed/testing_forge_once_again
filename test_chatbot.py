import unittest
from unittest.mock import patch
from chatbot import ChatBot

class TestChatBot(unittest.TestCase):
    def setUp(self):
        self.chatbot = ChatBot()

    def test_greet_user(self):
        with patch('builtins.print') as mock_print:
            self.chatbot.greet_user("Alice")
            mock_print.assert_called_with("Hello, Alice!")

    def test_handle_simple_query(self):
        with patch('builtins.input', return_value="What is the weather?"):
            with patch('builtins.print') as mock_print:
                self.chatbot.run()
                mock_print.assert_called_with("The weather is sunny today.")

    def test_handle_complex_query(self):
        with patch('builtins.input', return_value="What is the capital of France?"):
            with patch('builtins.print') as mock_print:
                self.chatbot.run()
                mock_print.assert_called_with("The capital of France is Paris.")

    def test_handle_unknown_query(self):
        with patch('builtins.input', return_value="What is the meaning of life?"):
            with patch('builtins.print') as mock_print:
                self.chatbot.run()
                mock_print.assert_called_with("I'm sorry, I don't have an answer for that.")

if __name__ == '__main__':
    unittest.main()
