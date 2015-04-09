import ply.lex as lex


tokens = (
        'LANGLE',       # <
        'LANGLESLASH',  # </
        'RANGLE',       # >
        'SLASHRANGLE',  # />
        'EQUAL',        # =
        'STRING',       # "144"
        'WORD',         # 'Welcome' in "Welcome to my webpage."
)

t_ignore                = ' \t\v\r' # shortcut for whitespace

states = ( ('htmlcomment', 'exclusive'),)

def t_htmlcomment(t):
    r'<!--'
    t.lexer.begin('htmlcomment')

def t_htmlcomment_end(t):
    r'-->'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.begin('INITIAL')
    pass

def t_htmlcomment_error(t):
    t.lexer.skip(1)

def t_LANGLESLASH(t):
        r'</'
        return t

def t_LANGLE(t):
        r'<'
        return t

def t_SLASHRANGLE(t):
        r'/>'
        return t

def t_RANGLE(t):
        r'>'
        return t

def t_EQUAL(t):
        r'='
        return t

def t_STRING(t):
        r'"[^"]*"'
        t.value = t.value[1:-1] # drop "surrounding quotes"
        return t

def t_WORD(t):
        r'[^ <>\n]+'
        return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

webpage1 = '"This" is <b>my</b>webpage!'
webpage2 = """Tricky \n"string" <i>output<i/>!"""
webpage3 = """Line1
    Line2
    """
webpage4 = "hello <!-- comment -->all"
htmllexer1 = lex.lex()
htmllexer1.input(webpage1)
htmllexer2 = lex.lex()
htmllexer2.input(webpage2)
htmllexer3 = lex.lex()
htmllexer3.input(webpage3)
htmllexer4 = lex.lex()
htmllexer4.input(webpage4)

def printToken(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)
    print("------------------------------")

printToken(htmllexer1)
printToken(htmllexer2)
printToken(htmllexer3)
printToken(htmllexer4)

# output of htmllexer1

'''
LexToken(STRING,'This',1,0)
LexToken(WORD,'is',1,7)
LexToken(LANGLE,'<',1,10)
LexToken(WORD,'b',1,11)
LexToken(RANGLE,'>',1,12)
LexToken(WORD,'my',1,13)
LexToken(LANGLESLASH,'</',1,15)
LexToken(WORD,'b',1,17)
LexToken(RANGLE,'>',1,18)
LexToken(WORD,'webpage!',1,19)'''

# output of htmllexer2

'''
LexToken(WORD,'Tricky',1,0)
LexToken(STRING,'string',2,8)
LexToken(LANGLE,'<',2,17)
LexToken(WORD,'i',2,18)
LexToken(RANGLE,'>',2,19)
LexToken(WORD,'output',2,20)
LexToken(LANGLE,'<',2,26)
LexToken(WORD,'i/',2,27)
LexToken(RANGLE,'>',2,29)
LexToken(WORD,'!',2,30)
'''

# output of htmllexer3

'''
LexToken(WORD,'Line1',1,0)
LexToken(WORD,'Line2',2,10)
'''

# output of htmllexer4

'''
LexToken(WORD,'hello',1,0)
LexToken(WORD,'all',1,22)
'''