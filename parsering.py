from rply import ParserGenerator
from ast import Number, Sum, Sub, Print, String


class Pars():

    def __init__(self):
        self.pg = ParserGenerator(
            ['INCLUDE', 'LIBstdio.h', 'MAIN', 'NUMBER', 'STR', 'PRINT', 'START', 'FINISH', 'OPEN_PARENS', 'CLOSE_PARENS', 'SEMI_COLON', 'SUM', 'SUB'],
            precedence=[('left', ['SUM', 'SUB']), ]
             )

    def parse(self):

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(int(p[0].value))

        @self.pg.production('expression : STR')
        def strings(p):
            return String(p[0].value[1:-1])

        @self.pg.production('expression : INCLUDE expression')
        def include(p):
            return p[1]

        @self.pg.production('expression : LIBstdio.h expression')
        def include(p):
            return p[1]

        @self.pg.production('expression : MAIN expression')
        def cmainc(p):
            return p[1]

        @self.pg.production('expression : START expression FINISH')
        def expression_start_finish(p):
            return p[1]

        @self.pg.production('expression : START OPEN_PARENS expression FINISH')
        def expression_open_parens(p):
            return p[1]

        @self.pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
        def expression_close_parens(p):
            return p[1]

        @self.pg.production('expression : START expression SEMI_COLON FINISH')
        def expression_semicolon(p):
            return p[1]

        @self.pg.production('expression : START expression SUM expression FINISH')
        @self.pg.production('expression : START expression SUB expression FINISH')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        @self.pg.production('expression : PRINT OPEN_PARENS expression CLOSE_PARENS SEMI_COLON')
        def expression(p):
            return Print(p[2])

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
            return self.pg.build()
