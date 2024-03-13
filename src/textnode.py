from htmlnode import HTMLNode, LeafNode
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return ((self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url))

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(text_node.text,None)

    elif text_node.text_type == text_type_bold:
        return LeafNode(text_node.text,"b")
    
    elif text_node.text_type == text_type_italic:
        return LeafNode(text_node.text,"i")

    elif text_node.text_type == text_type_code:
        return LeafNode(text_node.text, "code")
    
    elif text_node.text_type == text_type_link:
        return LeafNode(text_node.text, "a", {"href":f"{text_node.url}"})
    
    elif text_node.text_type == text_type_image:
        return LeafNode("","img",{"src":f"{text_node.url}","alt":f"{text_node.text}"})
    else:
        raise Exception("Invalid text-type")

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes = []
    for textnode in old_nodes:
        if textnode.text_type != text_type_text:
            new_nodes.append(textnode)
            continue
        if textnode.text.count(delimiter) % 2 != 0:
            raise Exception("Matching closing delimiter does not appear in this node! Wrong Markdown syntax")
        else:
            split_text_list = textnode.text.split(delimiter)
            #index 0 has to be the text before the modified word
            #index 1 is the modified word
            #index 2 is the text afte the modified word
            for i in range(len(split_text_list)):
                if textnode.text.startswith(delimiter) and textnode.text.endswith(delimiter):
                    if i == 0 or i == len(split_text_list)-1:
                        continue
                    elif i % 2 != 0:
                        new_nodes.append(TextNode(split_text_list[i],text_type ))
                    else:
                        new_nodes.append(TextNode(split_text_list[i], text_type_text))

                elif textnode.text.startswith(delimiter):
                    if i == 0:
                        continue
                    if i == 1:
                        new_nodes.append(TextNode(split_text_list[i], text_type))
                    elif i % 2 == 0:
                        new_nodes.append(TextNode(split_text_list[i], text_type_text))
                    else:
                        new_nodes.append(TextNode(split_text_list[i], text_type))

                elif textnode.text.endswith(delimiter):
                    if i == len(split_text_list)-1:
                        continue
                    if i == len(split_text_list)-2:
                        new_nodes.append(TextNode(split_text_list[i], text_type))
                    elif i % 2 == 0:
                        new_nodes.append(TextNode(split_text_list[i], text_type_text))
                    else:
                        new_nodes.append(TextNode(split_text_list[i], text_type)) 
                else:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(split_text_list[i], text_type_text))
                    else:
                        new_nodes.append(TextNode(split_text_list[i], text_type)) 


    return new_nodes 