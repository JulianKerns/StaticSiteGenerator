from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
import os

def main():
    public_path = "/home/julian_k/workspace/github.com/JulianKerns/StaticSiteGenerator/public"
    static_path = "/home/julian_k/workspace/github.com/JulianKerns/StaticSiteGenerator/static"
    def deleting_public_dir_contents():
        if os.path.exists(public_path):
            public_contents = os.listdir(public_path)

            for element in public_contents:
                if os.path.isfile(os.path.join(public_path, element)):
                    #os.remove(element)
                    print("element")
                else:
                    #shutil.rmtree(os.path.join(public_path,element))
                    print(element)

    def copying_static_dir(public_path, static_path):
        if os.path.exists(static_path):
            static_contents = os.listdir(static_path)
           
            for element in static_contents:
              
                element_path_public = os.path.join(public_path,element)
                element_path_static = os.path.join(public_static,element)

                if os.path.exists(element_path_static):
                    if os.path.isfile(element_path_static):
                        shutil.copy(element_path_static,public_path)
                    else:
                        os.mkdir(element_path_public)
                        copying_static_dir(element_path_public, element_path_static)



  
main()