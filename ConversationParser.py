#Declarations
import pypandoc

class ChatbotCoversationAdapter():
    #HTML TO MARKDOWN
    def convert_HTML_to_MarkDown(htmlstring):
        output = pypandoc.convert_text(htmlstring, 'md', format='html')
        return output
    
    #MARKDOWN TO HTML
    def convert_MarkDown_to_HTML(mdstring):
        output = pypandoc.convert_text(mdstring, 'html', format='md')
        return output


import unittest

class TestStringMethods(unittest.TestCase):

    def test_MarkdownToHTML(self):
        self.assertEqual(ChatbotCoversationAdapter.convert_MarkDown_to_HTML(open("hyperlink.html", "r").read()), open("hyperlink.md", "r").read())
        self.assertEqual(ChatbotCoversationAdapter.convert_MarkDown_to_HTML(open("images.html", "r").read()), open("images.md", "r").read())
        self.assertEqual(ChatbotCoversationAdapter.convert_MarkDown_to_HTML(open("list.html", "r").read()), open("list.md", "r").read())
        self.assertEqual(ChatbotCoversationAdapter.convert_MarkDown_to_HTML(open("list_multi.html", "r").read()), open("list_multi.md", "r").read())
        self.assertEqual(ChatbotCoversationAdapter.convert_MarkDown_to_HTML(open("Text.html", "r").read()), open("Text.md", "r").read())


if __name__ == '__main__':
    unittest.main()