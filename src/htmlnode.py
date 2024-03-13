class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_HTML(self):
        raise NotImplementedError("this method needs to be implemented")
    
    def props_to_HTML(self):
        if not self.props:
            return ""
        props_dict = self.props
        props_list = []
        for key,value in props_dict.items():
            props_list.append(f' {key}="{value}"')
        joined_props_list = "".join(props_list)
        return joined_props_list 
       
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)
    
    def __eq__(self, other):
        return ((self.value == other.value) and (self.tag == other.tag) and (self.props == other.props))

    def __repr__(self):
        return f"LeafNode({self.value}, {self.tag}, {self.props})"

    def to_HTML(self):
        if not self.value and self.value != "": 
            raise ValueError("LeafNode needs a value to be valid")
        elif not self.tag:
            return f"{self.value}"
        else:
            return f'<{self.tag}{self.props_to_HTML()}>{self.value}</{self.tag}>'
        
class ParentNode(HTMLNode):

    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)

    def to_HTML(self):
        if not self.tag:
            raise ValueError("ParentNode needs a tag to be valid")
        if not self.children:
            raise ValueError("ParentNode needs children to be valid")
        
        html_string =""
        for node in self.children:
            html_string += node.to_HTML()
        if self.props:
            return f'<{self.tag}{self.props_to_HTML()}>{html_string}</{self.tag}>'

        return f'<{self.tag}>{html_string}</{self.tag}>'
        

         
        
