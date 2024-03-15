block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_block(markdown):
    markdown_split = markdown.split("\n\n")
    result_list = []
    for i in range(len(markdown_split)):
        markdown_split[i]= markdown_split[i].strip(" ")
        if markdown_split[i] != "":
            result_list.append(markdown_split[i])
   
    return result_list

def block_to_blocktype(block):
    block_split = block.split("\n")
    
    if (block.startswith("#")
        or block.startswith("##")
        or block.startswith("###")
        or block.startswith("####")
        or block.startswith("#####")
        or block.startswith("######")
    ):
        return block_type_heading

    if len(block_split) > 1 and block_split[0].startswith("```") and block_split[-1].endswith("```"):
        return block_type_code

    if block.startswith(">"):
        for line in block_split:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote

            
    if block.startswith("* "):
        for line in block_split:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list

    if block.startswith("- "):
        for line in block_split:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    
    if block.startswith("1. "):
        i=1
        for line in block_split:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i+=1
        return block_type_ordered_list  
    return block_type_paragraph



    
block_to_blocktype('1. This is **bolded** paragraph\n2. This is another paragraph with *italic* text and `code` here\n3. This is the same paragraph on a new line')