from lexering import Lexer
from parsering import Pars

text_input = "print(4 + 4 - 2);"

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Pars()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

