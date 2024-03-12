from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode

def main():
    textnode1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #print(repr(textnode1))
   

    #htmlnode1 = HTMLNode("a", "this is a link", ["snap"],{"href": "https://www.google.com", "target": "_blank"})
   # print(repr(htmlnode1))
   
    leafnode1 = LeafNode( "this is a link","a",{"href": "https://www.google.com", "target": "_blank"})
    leafnode2 = LeafNode( "this is a link","a")
    print(leafnode1.to_HTML())
    print(leafnode2.to_HTML())
  

  
main()