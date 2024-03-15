from htmlnode import HTMLNode, ParentNode, LeafNode
from block_markdown import markdown_to_block, block_to_blocktype
from block_markdown import (
    block_type_paragraph,
    block_type_heading, 
    block_type_code, 
    block_type_quote, 
    block_type_unordered_list,
    block_type_ordered_list
)
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node) 
        children.append(html_node)
    return children

def block_type_paragraph_to_html_node(block):
    lines = block.split("\n")
    text = " ".join(lines)
    children = text_to_children(text)
    return ParentNode(children,"p")

def block_type_heading_to_html_node(block):
    if block.startswith("######"):
        text= block[7:]
        children = text_to_children(text)
        return ParentNode(children,"h6")

    elif block.startswith("#####"):
        text= block[6:]
        children = text_to_children(text)
        return ParentNode(children,"h5")

    elif block.startswith("####"):
        text= block[5:]
        children = text_to_children(text)
        return ParentNode(children,"h4")

    elif block.startswith("###"):
        text= block[4:]
        children = text_to_children(text)
        return ParentNode(children,"h3")

    elif block.startswith("##"):
        text= block[3:]
        children = text_to_children(text)
        return ParentNode(children,"h2")

    elif block.startswith("#"):
        text= block[2:]
        children = text_to_children(text)
        return ParentNode(children,"h1")
    

def block_type_code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Not valid markdown code syntax")
    text = block.strip("```")
    children = text_to_children(text)
    code = ParentNode(children,"code")
    return ParentNode([code],"pre")

def block_type_quote_to_html_node(block):
    block_split = block.split("\n")
    value = []

    for line in block_split:
        if not line.startswith(">"):
            raise ValueError("Not valid quote markdown syntax")
        strip = line.lstrip(">")  
        value.append(strip)
    
    value_string = " ".join(value)
    children = text_to_children(value_string)
    return ParentNode(children,"blockquote")

def block_type_unordered_list_to_html_node(block):
    block_split = block.split("\n")
    main_children = []
    
    for line in block_split:
        if line.startswith("* "):  
            strip = line.lstrip("* ")
            children = text_to_children(strip)
        elif line.startswith("- "):
            strip = line.lstrip("- ")
            children = text_to_children(strip)

        elif line.startswith("+ "):   
            strip = line.lstrip("+ ")
            children = text_to_children(strip)
            
        main_children.append(ParentNode(children,"li"))

    return ParentNode(main_children, "ul")

def block_type_ordered_list_to_html_node(block):
    block_split = block.split("\n")
    main_children = []
    i = 1
    for line in block_split:
        text = line.lstrip(f"{i}. ")
        children = text_to_children(text)  
        main_children.append(ParentNode(children,"li"))
        i += 1

    return ParentNode(main_children, "ol")
    
def markdown_to_html_node(markdown):
    block_list = markdown_to_block(markdown)
    children = []
    for block in block_list:
        block_type = block_to_blocktype(block)
        if block_type == block_type_paragraph:
            children.append(block_type_paragraph_to_html_node(block))

        elif block_type == block_type_code:
            children.append(block_type_code_to_html_node(block))

        elif block_type == block_type_quote:
            children.append(block_type_quote_to_html_node(block))

        elif block_type == block_type_heading:
            children.append(block_type_heading_to_html_node(block))

        elif block_type == block_type_unordered_list:
            children.append(block_type_unordered_list_to_html_node(block))

        elif block_type == block_type_ordered_list:
            children.append(block_type_ordered_list_to_html_node(block))

    return ParentNode(children,"div")