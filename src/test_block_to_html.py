import unittest
from block_to_html import *
from pprint import pprint
from htmlnode import HTMLNode


class TestParentNode(unittest.TestCase):
    def test_eq_paragraph_ulist(self):
        markdown = """  This is **bolded** paragraph

  This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line



* This is a list
* with items""" 
        
    
        actual = markdown_to_html_node(markdown)
        expected = ParentNode([
            ParentNode([
                LeafNode("This is ", None),
                LeafNode("bolded", "b"),
                LeafNode(" paragraph",None)
                ],"p"),
            ParentNode([
                LeafNode("This is another paragraph with ",None),
                LeafNode("italic", "i"),
                LeafNode(" text and ",None),
                LeafNode("code","code"),
                LeafNode( " here This is the same paragraph on a new line",None)
                ],"p"),
            ParentNode([
                ParentNode([
                    LeafNode("This is a list",None)
                ],"li"),
                ParentNode([
                    LeafNode("with items",None)
                ],"li")
            ],"ul")
        ],"div",None)
        
        print(actual)
        print()
        print(expected)
        self.assertEqual(actual,expected)


   



if __name__ == "__main__":
    unittest.main()