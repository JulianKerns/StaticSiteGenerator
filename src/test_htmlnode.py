
import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_props(self):
        node = HTMLNode("a", "this is a link", ["snap"],{"href": "https://www.google.com", "target": "_blank"})
        actual = node.props_to_HTML()
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(actual, expected)
    
    def test_eq_repr(self):
        node = HTMLNode("a", "this is a link", ["snap"],{"href": "https://www.google.com", "target": "_blank"})
        actual = repr(node)
        expected = "HTMLNode(a, this is a link, ['snap'], {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(actual, expected)

class TestLeafNode(unittest.TestCase):
    def test_eq_with_props(self):
        leafnode = LeafNode( "this is a link","a",{"href": "https://www.google.com", "target": "_blank"})
        actual = leafnode.to_HTML()
        expected = '<a href="https://www.google.com" target="_blank">this is a link</a>'
        self.assertEqual(actual, expected)


    def test_eq_without_props(self):
        leafnode = LeafNode( "this is a link","a")
        actual = leafnode.to_HTML()
        expected = '<a>this is a link</a>'
        self.assertEqual(actual, expected)

    def test_eq_with_empty_props(self):
        leafnode = LeafNode( "this is a paragraph","p",{})
        actual = leafnode.to_HTML()
        expected = '<p>this is a paragraph</p>'
        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()