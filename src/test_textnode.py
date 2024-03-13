import unittest

from textnode import TextNode, text_node_to_html_node 
from htmlnode import HTMLNode, LeafNode
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_delimiter 


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

    def test_eq_old_node_to_new_node_not_text(self):
        textnode = LeafNode("this is bold","b")
        actual = (split_nodes_delimiter([textnode],"*","text"))
        expected =[LeafNode("this is bold","b")]
        self.assertEqual(actual,expected)

    def test_eq_old_node_to_new_node_middle(self):
        textnode = TextNode("this text is **bold** text","text")
        actual = (split_nodes_delimiter([textnode],"**","bold"))
        expected =[TextNode("this text is ","text"),
                    TextNode("bold","bold"),
                    TextNode(" text","text")
                    ]
        self.assertEqual(actual,expected)

    def test_eq_old_node_to_new_node_(self):
        textnode = TextNode("this text is **bold** text","text")
        leafnode = LeafNode("this is bold","b")
        actual = (split_nodes_delimiter([textnode,leafnode],"**","bold"))
        expected =[TextNode("this text is ","text"),
                    TextNode("bold","bold"),
                    TextNode(" text","text"),
                    LeafNode("this is bold","b")
                    ]
        self.assertEqual(actual,expected)


    def test_eq_old_node_to_new_node_(self):
        textnode = TextNode("*this* text is *italic* text","text")
        leafnode = LeafNode("this is italic","i")
        actual = (split_nodes_delimiter([textnode,leafnode],"*","italic"))
        expected =[TextNode("this","italic"),
                    TextNode(" text is ","text"),
                    TextNode("italic","italic"),
                    TextNode(" text","text"),
                    LeafNode("this is italic","i")
                    ]
        self.assertEqual(actual,expected)


    def test_eq_old_node_to_new_node_(self):
        textnode = TextNode("this `text` is a `code block`","text")
        leafnode = LeafNode("this is italic","i")
        actual = (split_nodes_delimiter([textnode,leafnode],"`","code"))
        expected =[TextNode("this ","text"),
                    TextNode("text","code"),
                    TextNode(" is a ","text"),
                    TextNode("code block","code"),
                    LeafNode("this is italic","i")
                    ]
        self.assertEqual(actual,expected)
        
    def test_eq_old_node_to_new_node(self):
        textnode = TextNode("**this** text is **bold text**","text")
        leafnode = LeafNode("this is bold","b")
        actual = (split_nodes_delimiter([textnode,leafnode],"**","bold"))
        expected =[TextNode("this","bold"),
                    TextNode(" text is ","text"),
                    TextNode("bold text","bold"),
                    LeafNode("this is bold","b")
                    ]
        self.assertEqual(actual,expected)

    def test_eq_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)" 
        actual = extract_markdown_images(text)
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]
        self.assertEqual(actual,expected)

    def test_eq_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)" 
        actual = extract_markdown_links(text)
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertEqual(actual,expected)

    


if __name__ == "__main__":
    unittest.main()
