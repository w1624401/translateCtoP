from rply import ParserGenerator
from ast import Number, Sum, Sub, Print


class Pars():

    def __init__(self):
        self.pg = ParserGenerator(
            ['NUMBER', 'PRINT', 'OPEN_PARENS', 'CLOSE_PARENS', 'SEMI_COLON', 'SUM', 'SUB'],
            precedence=[('left', ['SUM', 'SUB']), ]
             )

    def parse(self):

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(int(p[0].value))

        @self.pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
        def expression_parens(p):
            return p[1]

        @self.pg.production('expression : OPEN_PARENS expression CLOSE_PARENS SEMI_COLON')
        def expression_semicolon(p):
            return p[1]

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        @self.pg.production('program : PRINT OPEN_PARENS expression CLOSE_PARENS SEMI_COLON')
        def program(p):
            return Print(p)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
