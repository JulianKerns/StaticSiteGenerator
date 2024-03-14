import unittest

from block_markdown import markdown_to_block, block_to_blocktype

class TestTextNode(unittest.TestCase):
    def test_eq_markdown_to_block_whitespaces_and_empty_blocks(self):
        text = """  This is **bolded** paragraph

  This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line



* This is a list
* with items"""
        actual = markdown_to_block(text)
        expected =[
        'This is **bolded** paragraph',
         'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
         '* This is a list\n* with items'
         ]
        self.assertEqual(actual,expected)
    

   
    def test_eq_markdown_to_block_and_empty_blocks(self):
        text = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

    Hello hello hello



* This is a list
* with items"""
        actual = markdown_to_block(text)
        expected =[
        'This is **bolded** paragraph',
        
         'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
         'Hello hello hello',
         '* This is a list\n* with items'
         ]
        self.assertEqual(actual,expected)

    def test_eq_markdown_to_block(self):
        text = """This is **bolded** paragraph
This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

    Hello hello hello



* This is a list
* with items"""
        actual = markdown_to_block(text)
        expected =[
        'This is **bolded** paragraph\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
         'Hello hello hello',
         '* This is a list\n* with items'
         ]
        self.assertEqual(actual,expected)

    def test_eq_block_to_blocktype_olist(self):
        block = '1. This is **bolded** paragraph\n2. This is another paragraph with *italic* text and `code` here\n3. This is the same paragraph on a new line'
        actual = block_to_blocktype(block)
        expected = "ordered_list"
        self.assertEqual(actual,expected)

    def test_eq_block_to_blocktype_ulist1(self):
        block = '* This is **bolded** paragraph\n* This is another paragraph with *italic* text and `code` here\n* This is the same paragraph on a new line'
        actual = block_to_blocktype(block)
        expected = "unordered_list"
        self.assertEqual(actual,expected)
    
    def test_eq_block_to_blocktype_ulist2(self):
        block = '- This is **bolded** paragraph\n- This is another paragraph with *italic* text and `code` here\n- This is the same paragraph on a new line'
        actual = block_to_blocktype(block)
        expected = "unordered_list"
        self.assertEqual(actual,expected)

    def test_eq_block_to_blocktype_code(self):
        block = '```This is **bolded** paragraph\n```This is another paragraph with *italic* text and `code` here\n```This is the same paragraph on a new line'
        actual = block_to_blocktype(block)
        expected = "code"
        self.assertEqual(actual,expected)

    def test_eq_block_to_blocktype_quote(self):
        block = '>This is **bolded** paragraph\n>This is another paragraph with *italic* text and `code` here\n>This is the same paragraph on a new line'
        actual = block_to_blocktype(block)
        expected = "quote"
        self.assertEqual(actual,expected)
    
    def test_eq_block_to_blocktype_heading(self):
        block = '###This is **bolded** paragraph\n##This is another paragraph with *italic* text and `code` here\n##This is the same paragraph on a new line'
        actual = block_to_blocktype(block)
        expected = "heading"
        self.assertEqual(actual,expected)
    def test_eq_block_to_blocktype_empty(self):
        block = ''
        actual = block_to_blocktype(block)
        expected = "paragraph"
        self.assertEqual(actual,expected)










if __name__ == "__main__":
    unittest.main()