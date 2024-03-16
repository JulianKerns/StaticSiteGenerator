from htmlnode import HTMLNode, ParentNode, LeafNode
from block_to_html import markdown_to_html_node
import os
import pathlib

def extract_title(markdown):
    markdown_split = markdown.split("\n")
    for line in markdown_split:
        if line.startswith("# "):
            return line[2:]

    raise Exception("All pages need a h1 header")    

def generate_page_function():

    from_path ="/home/julian_k/workspace/github.com/JulianKerns/StaticSiteGenerator/content/index.md"
    dest_path ="/home/julian_k/workspace/github.com/JulianKerns/StaticSiteGenerator/public/index.html"
    template_path = "/home/julian_k/workspace/github.com/JulianKerns/StaticSiteGenerator/template.html"
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path,mode = "r") as  markdown_file: 
        markdown_contents = markdown_file.read()
    
    with open(template_path, mode = "r") as template_file: 
        template_contents = template_file.read()
    
    html_content = markdown_to_html_node(markdown_contents).to_HTML()

    title_page = extract_title(markdown_contents)

    html_template_first= template_contents.replace('{{ Title }}', title_page )
    html_template_new = html_template_first.replace('{{ Content }}',html_content)

    output_dir =os.path.dirname(dest_path)
    os.makedirs(output_dir, exist_ok = True)

    with open(dest_path,mode ="w") as output_file:
        output_file.write(html_template_new)


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Generating pages from {dir_path_content} to {dest_dir_path} using {template_path}")
    if os.path.exists(dir_path_content):
        content_list = os.listdir(dir_path_content)

    with open(template_path, mode = "r") as template_file: 
        template_contents = template_file.read()
        
        for element in content_list:

            element_content_path = os.path.join(dir_path_content, element)
           
            if os.path.isfile(element_content_path):
                content_file_object= pathlib.Path(element_content_path)
                if content_file_object.suffix == ".md":
                
                    with open(element_content_path,mode = "r") as  markdown_file: 
                        markdown_contents = markdown_file.read()

                    html_content = markdown_to_html_node(markdown_contents).to_HTML()
                    title_page = extract_title(markdown_contents)

                    html_template_first= template_contents.replace('{{ Title }}', title_page )
                    html_template_new = html_template_first.replace('{{ Content }}',html_content)

                    output_dir = os.path.dirname(dest_dir_path)
                    os.makedirs(output_dir, exist_ok = True)

                    element_dest_path = os.path.join(dest_dir_path, element)

                    dest_file_object= pathlib.Path(element_dest_path)
                    dest_file_stripped = dest_file_object.stem
                    html_element = dest_file_stripped + ".html"
                    html_element_dest_path = os.path.join(dest_dir_path, html_element)

                    with open(html_element_dest_path,mode ="w") as output_file:
                        output_file.write(html_template_new)

            else:
                element_dir_dest_path = os.path.join(dest_dir_path, element)
                os.makedirs(element_dir_dest_path, exist_ok = True)
                generate_page_recursive(element_content_path, template_path, element_dir_dest_path)

    
