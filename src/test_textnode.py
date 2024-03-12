import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(node1, node2)

    def test_eq2(self):
        node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertEqual(node1, node2)
    
    def test_eq3(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertEqual(node1, node2)
    
    def test_eq4(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
