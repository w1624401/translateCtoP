from rply import LexerGenerator


class Lexer():

    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        #mains
        self.lexer.add('INCLUDE', r"#include ")
        self.lexer.add('MAIN', r"main\(\)")
        self.lexer.add('PRINT', r"printf")
        self.lexer.add('NUMBER', r'\d+')
        #libraries
        self.lexer.add('LIBstdio.h', r"<stdio.h>")
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Signs
        self.lexer.add('START', '{')
        self.lexer.add('FINISH', '}')
        self.lexer.add('OPEN_PARENS', r'\(')
        self.lexer.add('CLOSE_PARENS', r'\)')
        self.lexer.add('SEMI_COLON', r'\;')
        self.lexer.add('STR', r'"(.*?)"')
        # Ignore spaces
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
