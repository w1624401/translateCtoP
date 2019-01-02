from rply import LexerGenerator


class Lexer():

    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('PRINT', r"printf")
        # Operators
        # Signs
        self.lexer.add('OPEN_PARENS', r'\(')
        self.lexer.add('CLOSE_PARENS', r'\)')
        self.lexer.add('SEMI_COLON', r'\;')
        self.lexer.add('STR', r'"(.*?)"')
        self.lexer.add('STRING', r'[a-zA-Z_]*')


    def get_lexer(self):

        self._add_tokens()
        return self.lexer.build()
