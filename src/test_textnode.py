import unittest

from textnode import TextNode, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(node1, node2)

    def test_eq2_fail(self):
        node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertEqual(node1, node2)
    
    def test_eq3_fail(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertEqual(node1, node2)
    
    def test_eq4(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_eq_text_to_node_text(self):
        textnode = TextNode("this is plain text","text")
        actual = text_node_to_html_node(textnode).to_HTML()
        expected = 'this is plain text'
        self.assertEqual(actual,expected)

    def test_eq_text_to_node_img(self):
        textnode = TextNode("this is an image","image","https://image.com")
        actual = (text_node_to_html_node(textnode)).to_HTML()
        expected = '<img src="https://image.com" alt="this is an image"></img>'
        self.assertEqual(actual,expected)

    def test_eq_text_to_node_link(self):
        textnode = TextNode("Google","link","https://google.com")
        actual = (text_node_to_html_node(textnode)).to_HTML()
        expected = '<a href="https://google.com">Google</a>'
        self.assertEqual(actual,expected)

    def test_eq_text_to_node_bold(self):
        textnode = TextNode("this text is bold","bold")
        actual = (text_node_to_html_node(textnode)).to_HTML()
        expected = '<b>this text is bold</b>'
        self.assertEqual(actual,expected)

    def test_eq_text_to_node_wrong_type(self):
        textnode = TextNode("this text is bold","asdfoiuh")
        actual = (text_node_to_html_node(textnode)).to_HTML()
        expected = '<b>this text is bold</b>'
        self.assertEqual(actual,expected)


if __name__ == "__main__":
    unittest.main()
