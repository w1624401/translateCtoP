from rply import LexerGenerator


class Lexer():

    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('PRINT', r'print')
        self.lexer.add('NUMBER', r'\d+')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Signs
        self.lexer.add('OPEN_PARENS', r'\(')
        self.lexer.add('CLOSE_PARENS', r'\)')
        self.lexer.add('SEMI_COLON', r'\;')
        # Ignore spaces
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
