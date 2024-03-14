import re
from textnode import   (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)

def split_nodes_delimiter(old_nodes, delimiter ,text_type):
    new_nodes = []
    for textnode in old_nodes:
        if textnode.text_type != text_type_text:
            new_nodes.append(textnode)
            continue
        if delimiter not in textnode.text:
            new_nodes.append(textnode)
            continue
        else:
            split_text_list = textnode.text.split(delimiter)
            if len(split_text_list) % 2 == 0:
                raise ValueError("Matching closing delimiter does not appear in this node! Wrong Markdown syntax")
            #index 0 has to be the text before the modified word
            #index 1 is the modified word
            #index 2 is the text afte the modified word
            for i in range(len(split_text_list)):
                
                if textnode.text.startswith(delimiter) and textnode.text.endswith(delimiter):
                    if i == 0 or i == len(split_text_list)-1:
                        continue
                    if i % 2 != 0:
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
                    # in the case where the whole text is ecased in delimiters additional whitespace textnodes are generated
                    #i am leaving them in for formatting reasons for now
                    
                    if i % 2 == 0:
                        new_nodes.append(TextNode(split_text_list[i], text_type_text))
                    else:
                        new_nodes.append(TextNode(split_text_list[i], text_type)) 


    return new_nodes 

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == None or node.text == "":
            continue
        extracted_images = extract_markdown_images(node.text)
        if extracted_images == []:
            new_nodes.append(node)
            continue
       
        split_text = []
        text_part = node.text
        for i in range(len(extracted_images)):
            section = text_part.split(f"[{extracted_images[i][0]}]({extracted_images[i][1]})", 1) 
            if len(section) != 2:
                raise Exception("Image markdown syntax was not properly closed")
            head = text_part.split(f"![{extracted_images[i][0]}]({extracted_images[i][1]})", 1)[0]
            tail = text_part.split(f"![{extracted_images[i][0]}]({extracted_images[i][1]})", 1)[1]
            if head != "":
                split_text.append(head)
            split_text.append([extracted_images[i][0],extracted_images[i][1]])
            text_part = tail
          
        if text_part:
            split_text.append(text_part)
        
        for n in range(len(split_text)):
            if type(split_text[0]) == list:
                if n % 2 == 0:
                    new_nodes.append(TextNode(split_text[n][0],text_type_image,split_text[n][1]))
                else:
                    new_nodes.append(TextNode(split_text[n],text_type_text))

            else:
                if n % 2 == 0:
                    new_nodes.append(TextNode(split_text[n],text_type_text))
                else:
                    new_nodes.append(TextNode(split_text[n][0],text_type_image,split_text[n][1]))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text == None or node.text == "":
            continue
        extracted_links = extract_markdown_links(node.text)
        if extracted_links == []:
            new_nodes.append(node)
            continue
       
        split_text = []
        text_part = node.text
        for i in range(len(extracted_links)):
            section = text_part.split(f"[{extracted_links[i][0]}]({extracted_links[i][1]})", 1) 
            if len(section) != 2:
                raise Exception("Link markdown syntax was not properly closed")
            head = text_part.split(f"[{extracted_links[i][0]}]({extracted_links[i][1]})", 1)[0]
            tail = text_part.split(f"[{extracted_links[i][0]}]({extracted_links[i][1]})", 1)[1]
            if head != "":
                split_text.append(head)
            split_text.append([extracted_links[i][0],extracted_links[i][1]])
            text_part = tail
          
        if text_part:
            split_text.append(text_part)
        
        for n in range(len(split_text)):
            if type(split_text[0]) == list:
                if n % 2 == 0:
                    new_nodes.append(TextNode(split_text[n][0],text_type_link,split_text[n][1]))
                else:
                    new_nodes.append(TextNode(split_text[n],text_type_text))

            else:
                if n % 2 == 0:
                    new_nodes.append(TextNode(split_text[n],text_type_text))
                else:
                    new_nodes.append(TextNode(split_text[n][0],text_type_link,split_text[n][1]))

    return new_nodes
      

def text_to_textnodes(text):
    #start by creating a textnode with the whole text as text
    starting_textnode= TextNode(text,text_type_text)
    #splitting the whole text into textnodes that can then be processed into HTMLNodes
    split_by_bold = split_nodes_delimiter([starting_textnode], "**",text_type_bold)
    split_by_italic = split_nodes_delimiter(split_by_bold, "*", text_type_italic)
    split_by_code = split_nodes_delimiter(split_by_italic, "`", text_type_code)
    split_by_image = split_nodes_image(split_by_code)
    split_by_link = split_nodes_link(split_by_image)
    return split_by_link
        
      
text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)")
