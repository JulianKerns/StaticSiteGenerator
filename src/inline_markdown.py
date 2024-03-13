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

def split_nodes_links(old_nodes):
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
      
        
      
        
