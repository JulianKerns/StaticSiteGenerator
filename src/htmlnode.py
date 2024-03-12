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

    def to_HTML(self):
        if not self.value: 
            raise ValueError("LeafNode needs a value tp be valid")
        elif not self.tag:
            return f"{self.value}"
        else:
            return f'<{self.tag}{self.props_to_HTML()}>{self.value}</{self.tag}>'
        
            