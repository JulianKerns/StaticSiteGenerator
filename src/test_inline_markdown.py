import unittest

from textnode import TextNode, text_node_to_html_node 
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_links



class TestTextNode(unittest.TestCase):
    def test_eq_images_first(self):
        textnode = [TextNode("Hello friends ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and others","text")]
        actual = split_nodes_image(textnode)
        expected =[TextNode("Hello friends ","text"),
                    TextNode("image","image","https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ","text"),
                    TextNode("second image","image","https://i.imgur.com/3elNhQu.png"),
                    TextNode(" and others","text")
                    ]
        self.assertEqual(actual,expected)

    def test_eq_text_first(self):
        textnode = [TextNode("![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and others","text")]
        actual = split_nodes_image(textnode)
        expected =[TextNode("image","image","https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ","text"),
                    TextNode("second image","image","https://i.imgur.com/3elNhQu.png"),
                    TextNode(" and others","text")
                    ]
        self.assertEqual(actual,expected)

    def test_eq_images_first_and_last(self):
        textnode = [TextNode("![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)","text")]
        actual = split_nodes_image(textnode)
        expected =[TextNode("image","image","https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ","text"),
                    TextNode("second image","image","https://i.imgur.com/3elNhQu.png"),
                    ]
        self.assertEqual(actual,expected)
    
    def test_eq_images_last(self):
        textnode = [TextNode("Hello friends ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)","text")]
        actual = split_nodes_image(textnode)
        expected =[TextNode("Hello friends ","text"),
                    TextNode("image","image","https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ","text"),
                    TextNode("second image","image","https://i.imgur.com/3elNhQu.png"),
                    ]
        self.assertEqual(actual,expected)

    def test_eq_no_value(self):
        textnode = TextNode("Hello friends ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)","text")
        textnode_empty= TextNode(None,"text")
        actual = split_nodes_image([textnode, textnode_empty])
        expected =[TextNode("Hello friends ","text"),
                    TextNode("image","image","https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ","text"),
                    TextNode("second image","image","https://i.imgur.com/3elNhQu.png"),
                    ]
        self.assertEqual(actual,expected)

    def test_eq_no_value_image(self):
        textnode = TextNode("Hello friends ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)","text")
        textnode_empty= TextNode("hello this has no imagesyntax","text")
        actual = split_nodes_image([textnode, textnode_empty])
        expected =[TextNode("Hello friends ","text"),
                    TextNode("image","image","https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ","text"),
                    TextNode("second image","image","https://i.imgur.com/3elNhQu.png"),
                    TextNode("hello this has no imagesyntax","text")
                    ]
        self.assertEqual(actual,expected)

    def test_eq_text_first_link(self):
        textnode = TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)","text")
        actual = split_nodes_links([textnode])
        expected =[TextNode("This is text with a ","text"),
                    TextNode("link","link","https://www.example.com"),
                    TextNode(" and ","text"),
                    TextNode("another","link","https://www.example.com/another"),
                    
                    ]
        self.assertEqual(actual,expected)
    
    def test_eq_text_first_and_last_link(self):
        textnode = TextNode("[link](https://www.example.com) and [another](https://www.example.com/another)","text")
        actual = split_nodes_links([textnode])
        expected =[
                    TextNode("link","link","https://www.example.com"),
                    TextNode(" and ","text"),
                    TextNode("another","link","https://www.example.com/another"),
                    
                    ]
        self.assertEqual(actual,expected)

    def test_eq_link_first_and_last_text(self):
        textnode = TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another) and other words","text")
        actual = split_nodes_links([textnode])
        expected =[TextNode("This is text with a ","text"),
                    TextNode("link","link","https://www.example.com"),
                    TextNode(" and ","text"),
                    TextNode("another","link","https://www.example.com/another"),
                    TextNode(" and other words","text")
                    ]
        self.assertEqual(actual,expected)



if __name__ == "__main__":
    unittest.main()

       # split_nodes_image([TextNode("Hello friends ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and others","text")])