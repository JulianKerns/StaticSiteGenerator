from htmlnode import HTMLNode, ParentNode, LeafNode
from block_to_html import markdown_to_html_node
import os

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
    
        


    
