
import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

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


class TestParentNode(unittest.TestCase):
    def test_eq_children(self):
        parentnode = ParentNode([
            LeafNode("this is bold","b"),
            LeafNode("this is italic","i"),
            LeafNode("this is just plain text",None)
        ],"p",{"href" : "https://www.google.com"})
        actual = parentnode.to_HTML()
        expected = '<p href="https://www.google.com"><b>this is bold</b><i>this is italic</i>this is just plain text</p>'
        self.assertEqual(actual,expected)
    
    def test_eq_no_tag(self):
        parentnode = ParentNode([
            LeafNode("this is bold","b"),
            LeafNode("this is italic","i"),
            LeafNode("this is just plain text",None)
        ],None,{"href" : "https://www.google.com"})
        actual = parentnode.to_HTML()
        expected = ValueError("ParentNode needs a tag to be valid")
        self.assertEqual(actual,expected)

    def test_eq_no_children(self):
        parentnode = ParentNode(None,"p",{"href" : "https://www.google.com"})
        actual = parentnode.to_HTML()
        expected = ValueError("ParentNode needs children to be valid")
        self.assertEqual(actual,expected)


    def test_eq_no_value_leaf(self):
        parentnode = ParentNode([
            LeafNode(None,"b"),
            LeafNode("this is italic","i"),
            LeafNode("this is just plain text",None)
        ],"p",{"href" : "https://www.google.com"})
        actual = parentnode.to_HTML()
        expected = ValueError("LeafNode needs a value to be valid")
        self.assertEqual(actual,expected)

    
    def test_eq_no_parent_in_parent(self):
        parentnode = ParentNode([
            LeafNode("this is bold","b"),
            ParentNode([
                LeafNode("this is a link", "a", {"href": "https://boot.dev"}),
                LeafNode("this is text", None)
            ],"p"),
            LeafNode("this is just plain text", None)
            ],"p")
        actual = parentnode.to_HTML()
        expected = '<p><b>this is bold</b><p><a href="https://boot.dev">this is a link</a>this is text</p>this is just plain text</p>'
        self.assertEqual(actual,expected)

    def test_eq_no_parent_in_parent(self):
        parentnode = ParentNode([
            LeafNode("this is bold","b"),
            ParentNode([
                LeafNode("this is a link", "a", {"href": "https://boot.dev"}),
                LeafNode("this is text", None)
            ],"p"),
            LeafNode("this is just plain text", None)
            ],"p")
        actual = parentnode.to_HTML()
        expected = '<p><b>this is bold</b><p><a href="https://boot.dev">this is a link</a>this is text</p>this is just plain text</p>'
        self.assertEqual(actual,expected)








if __name__ == "__main__":
    unittest.main()