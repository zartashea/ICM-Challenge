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
        self.assertEqual(ChatbotCoversationAdapter.convert_MarkDown_to_HTML(open("index.html", "r").read()), open("index.html", "r").read())

    def test_HTMLtoMarkdown(self):
         self.assertEqual(ChatbotCoversationAdapter.convert_HTML_to_MarkDown(""), 'FOO')

if __name__ == '__main__':
    unittest.main()