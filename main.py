from lexering import Lexer
from parsering import Pars

print("Filename please:")
fname = input()
with open(fname) as f:
    text_input = f.read()


lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Pars()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

