from htmlnode import HTMLNode, LeafNode, ParentNode
from block_markdown import markdown_to_block, block_to_blocktype
from block_markdown import   (
    block_type_paragraph
    block_type_heading 
    block_type_code 
    block_type_quote 
    block_type_unordered_list
    block_type_ordered_list
)

def block_type_paragraph_to_html_node(block, block_type):
    return HTMLNode("p",block,[],{})

def block_type_heading_to_html_node(block, block_type):
    if block.startswith("#"):
        stripped= block.lstrip("#")
        return HTMLNode("h1",stripped, [],{})
    if block.startswith("##"):
        stripped= block.lstrip("#")
        return HTMLNode("h2",stripped, [],{})
    if block.startswith("###"):
        stripped= block.lstrip("#")
        return HTMLNode("h3",stripped, [],{})
    if block.startswith("####"):
        stripped= block.lstrip("#")
        return HTMLNode("h4",stripped, [],{})
    if block.startswith("#####"):
        stripped= block.lstrip("#")
        return HTMLNode("h5",stripped, [],{})
    if block.startswith("######"):
        stripped= block.lstrip("#")
        return HTMLNode("h6",stripped, [],{})

def block_type_code_to_html_node(block, block_type):
    stripped = block.strip("```")
    code_child = HTMLNode("code",stripped,[],{})
    return HTMLNode("pre",None,[code_child],{})

    
