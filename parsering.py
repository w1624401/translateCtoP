from rply import ParserGenerator
from ast import String, Print


class Pars():

    def __init__(self):
        self.pg = ParserGenerator(
            ['STRING', 'STR', 'PRINT', 'OPEN_PARENS', 'CLOSE_PARENS', 'SEMI_COLON']
             )

    def parse(self):

        @self.pg.production('expression : STR')
        def strings(p):
            return String(p[0].value[1:-1])

        @self.pg.production('expression : STRING')
        def string(p):
            return String(p[0].value)

        @self.pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
        def expression_parens(p):
            return p[1]

        @self.pg.production('expression : OPEN_PARENS expression CLOSE_PARENS SEMI_COLON')
        def expression_semicolon(p):
            return p[1]

        @self.pg.production('expression : PRINT OPEN_PARENS expression CLOSE_PARENS SEMI_COLON')
        def expression(p):
            return Print(p[2])

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
