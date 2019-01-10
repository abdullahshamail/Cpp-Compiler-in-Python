import ply.lex as lex
import ply.yacc as yacc
import sys
start = 'cpp'

tokens = (
    'ANDAND',       # &&
    'CHAR',
    'COLON',
    'COMMA',        # ,
    'DIVIDE',       # /
    'ELSE',         # else
    'EQUAL',        # =
    'EQUALEQUAL',   # ==
    'FALSE',        # false
    'GE',           # >=
    'GT',           # >
    'IDENTIFIER',   # factorial
    'IF',           # if
    'LBRACE',       # {
    'LE',           # <=
    'LPAREN',       # (
    'LT',           # <
    'MINUS',        # -
    'NOT',          # !
    'NUMBER',       # 1234 5.678
    'OROR',         # ||
    'PLUS',         # +
    'RBRACE',       # }
    'RETURN',       # return
    'RPAREN',       # )
    'SEMICOLON',    # ;
    'STRING',       # "this is a \"tricky\" string"
    'TIMES',        # *
    'TRUE',         # TRUE
    'VAR',          # var
    'ENDL',
    'WORD',
    'INT',
    'DOUBLE',
    'BOOL',
    'CHARACTER',
    'DOT',
    'BOOLVALUE',
    'MOD',
    'PLUSPLUS',
    'MINUSMINUS',
    'LSQUARE',
    'RSQUARE',
    'CLASSES',
    'FOR',
    'COUT',
    'ELSEIF',
    'NEWLINE',
    'VOID',
    'PUBLIC',
    'PRIVATE'
)


reserved = (
	'endl',
	'char',
	'int',
	'double',
	'string',
	'bool',
	'cout',
	'if',
	'else if',
	'else',
	'class',
	'for',
	'return',
	'true',
	'false',
	'void',
	'private',
	'public'
	)

t_ignore = ' \t\v\r' # whitespace
t_ANDAND =  r'&&'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_MINUS = r'\-'
t_MINUSMINUS = r'\-\-'
t_PLUSPLUS = r'\+\+'
t_COLON = r':'
t_COMMA =  r','
t_DIVIDE =  r'/'
t_EQUALEQUAL = r'=='
t_EQUAL = r'='
t_GE =  r'>='
t_GT =   r'>'
t_LBRACE = r'\{'
t_LE =  r'<='
t_LPAREN =   r'\('
t_LT = r'<'
t_NOT = r'!'
t_OROR = r'\|\|'
t_PLUS = r'\+'
t_RBRACE =  r'\}'
t_RPAREN =  r'\)'
t_SEMICOLON =   r';'
t_TIMES = r'\*'
t_DOT = r'\.'
t_MOD = r'\%'
t_ENDL = r'endl'
t_VOID = r'void'
t_IF = r'if'
t_ELSEIF = r'else if'
t_ELSE = r'else'
t_FOR = r'for'
t_CHAR = r'char'
t_STRING = r'string'
t_BOOL = r'bool'
t_INT = r'int'
t_DOUBLE = r'double'
t_COUT = r'cout'
t_RETURN = r'return'
t_FALSE = r'false'
t_TRUE = r'true'
t_PRIVATE = r'private'
t_PUBLIC = r'public' 


def t_CLASSES(t):
	r'class'
	return t

def t_BOOLVALUE(t):
	r'true | false'
	return t

def t_CHARACTER(t):
	r'\'[^\']\''
	t.value = t.value[1:-1]
	return t

def t_IDENTIFIER(t):
	r'[A-Za-z][A-Za-z0-9_]*'
	if t.value in reserved:
		t.type = t.value.upper()
	return t

def t_NUMBER(t):
	r'-?[0-9]*\.?[0-9]+'
	if '.' in t.value:
		t.value = float(t.value)
	else:
		t.value = int(t.value)
	return t

def t_WORD(t):
	r'\"[^"]*\"'
	t.value = t.value[1:-1]
	return t

def t_NEWLINE(t):
	r'\n'
	t.lexer.lineno += 1

def t_error(t):
	print "Invalid syntax '%s' at line number : '%d'" % (t.value[0], t.lexer.lineno)
	t.lexer.skip(1)



def p_cpp(p):#
	'cpp : element cpp'
	p[0] = [p[1]] + p[2]

def p_cpp2(p):
	'cpp : classy cpp'
	p[0] = [p[1]] + p[2]
	

def p_cpp1(p):#
	'cpp : '
	p[0] = [ ]

# def p_element(p):
# 	'element : classy'
# 	p[0] = p[1]

def p_element(p):#
	'element : statement'
	p[0] =  p[1]

def p_element1(p):#
	'element : ifstat'
	p[0] =  p[1]

def p_element2(p):#
	'element : forstat'
	p[0] =  p[1]

def p_element3(p):#
	'element : func'
	p[0] =  p[1]



# def p_return(p):
# 	'statement : RETURN statement'
# 	p[0] = ('return_statement', p[1], p[2])



def p_statement0(p):#
	'''statement : INT IDENTIFIER SEMICOLON
				 | STRING IDENTIFIER SEMICOLON
				 | CHAR IDENTIFIER SEMICOLON
				 | BOOL IDENTIFIER SEMICOLON
				 | DOUBLE IDENTIFIER SEMICOLON	'''
	p[0] = ('var_declare', p[1],p[2])

def p_statement1(p):#
	'''statement : INT IDENTIFIER EQUAL expression SEMICOLON
				 | STRING IDENTIFIER EQUAL expression SEMICOLON
				 | CHAR IDENTIFIER EQUAL expression SEMICOLON
				 | BOOL IDENTIFIER EQUAL expression SEMICOLON
				 | DOUBLE IDENTIFIER EQUAL expression SEMICOLON	'''
	p[0] = ('var_declare_assign', p[1],p[2],p[4])

def p_statement2(p):#
	'statement : IDENTIFIER PLUSPLUS SEMICOLON'
	p[0] = ('inc_op_after', p[1])

def p_statement3(p):#
	'statement : IDENTIFIER MINUSMINUS SEMICOLON'
	p[0] = ('dec_op_after', p[1])

def p_statementy(p):#
	'statement : PLUSPLUS IDENTIFIER SEMICOLON'
	p[0] = ('inc_op_before', p[1])

def p_statementz(p):#
	'statement : MINUSMINUS IDENTIFIER SEMICOLON'
	p[0] = ('dec_op_before', p[1])

def p_statement4(p):#
	'statement : IDENTIFIER EQUAL expression SEMICOLON'
	p[0] = ('var_assign', p[1],p[3])

def p_statement8(p):#
	'statement : IDENTIFIER LSQUARE NUMBER RSQUARE EQUAL IDENTIFIER LSQUARE NUMBER RSQUARE SEMICOLON'
	p[0] = ('array_value_replace', p[1],p[3],p[6], p[8])

def p_statement22(p):#
	'statement : IDENTIFIER LSQUARE NUMBER RSQUARE EQUAL expression SEMICOLON'
	p[0] = ('array_index_equal', p[1], p[3], p[6])

def p_statement5(p):#
	'''statement : INT IDENTIFIER LSQUARE NUMBER RSQUARE SEMICOLON
				 | STRING IDENTIFIER LSQUARE NUMBER RSQUARE SEMICOLON
				 | CHAR IDENTIFIER LSQUARE NUMBER RSQUARE SEMICOLON
				 | BOOL IDENTIFIER LSQUARE NUMBER RSQUARE SEMICOLON
				 | DOUBLE IDENTIFIER LSQUARE NUMBER RSQUARE SEMICOLON'''
	p[0] = ('array_declare', p[1], p[2], p[4])

def p_statement6(p):#
	'''statement : INT IDENTIFIER LSQUARE RSQUARE EQUAL LBRACE data RBRACE SEMICOLON
				 | STRING IDENTIFIER LSQUARE RSQUARE EQUAL LBRACE data RBRACE SEMICOLON
				 | CHAR IDENTIFIER LSQUARE RSQUARE EQUAL LBRACE data RBRACE SEMICOLON
				 | BOOL IDENTIFIER LSQUARE RSQUARE EQUAL LBRACE data RBRACE SEMICOLON
				 | DOUBLE IDENTIFIER LSQUARE RSQUARE EQUAL LBRACE data RBRACE SEMICOLON'''
	p[0] = ('array_declare_assign', p[1], p[2], ('array_data',p[7]))

def p_statement7(p):#
	'''statement : INT IDENTIFIER LSQUARE NUMBER RSQUARE EQUAL LBRACE data RBRACE SEMICOLON
				 | STRING IDENTIFIER LSQUARE NUMBER RSQUARE EQUAL LBRACE data RBRACE SEMICOLON
				 | CHAR IDENTIFIER LSQUARE NUMBER RSQUARE EQUAL LBRACE data RBRACE SEMICOLON
				 | BOOL IDENTIFIER LSQUARE NUMBER RSQUARE EQUAL LBRACE data RBRACE SEMICOLON
				 | DOUBLE IDENTIFIER LSQUARE NUMBER RSQUARE EQUAL LBRACE data RBRACE SEMICOLON'''
	p[0] = ('array_declare_size_assign', p[1], p[2], p[4], ('array_data',p[8]))


def p_statementx(p):#
	'statement : IDENTIFIER LPAREN argues RPAREN SEMICOLON'
	p[0] = ('function_call', p[1], ('arguments_fc', p[3]))

def p_argues(p):#
	'argues : '
	p[0] = []

def p_argues1(p):#
	'argues : BOOLVALUE morargues'
	p[0] = ('boolvalue',p[1],p[2])

def p_argues2(p):#
	'argues : IDENTIFIER morargues'
	p[0] = ('identifier', p[1],p[2])

def p_argues3(p):#
	'argues : NUMBER morargues'
	p[0] = ('number', p[1],p[2])

def p_argues4(p):#
	'argues : WORD morargues'
	p[0] = ('word', p[1],p[2])

def p_argues5(p):#
	'argues : CHARACTER morargues'
	p[0] = ('character', p[1],p[2])

def p_argues6(p):#
	'argues : MINUSMINUS IDENTIFIER morargues'
	p[0] = ('--identifier',p[2],p[3])

def p_argues7(p):#
	'argues : PLUSPLUS IDENTIFIER morargues'
	p[0] = ('++identifier',p[2],p[3])

def p_argues8(p):#
	'argues : IDENTIFIER PLUSPLUS morargues'
	p[0] = ('identifier++', p[1],p[3])

def p_argues9(p):#
	'argues : IDENTIFIER MINUSMINUS morargues'
	p[0] = ('identifier--', p[1],p[3])


def p_morargues1(p):#
	'morargues : '
	p[0] = [ ]

def p_morargues2(p):#
	'morargues : COMMA argues'
	p[0] = p[2]


def p_expression0(p):#
	'expression : IDENTIFIER'
	p[0] = ('identifiername', p[1])

def p_expression1(p):#
	'expression : NUMBER'
	p[0] = ('numbervalue', p[1])

def p_expression2(p):#
	'expression : WORD'
	p[0] = ('stringvalue', p[1])
	
def p_expression3(p):#
	'expression : CHARACTER'
	p[0] = ('charactervalue', p[1])

def p_expression4(p):#
	'expression : BOOLVALUE'
	p[0] = ('boolvalue', p[1])

def p_expression5(p):#
	'expression : IDENTIFIER LSQUARE NUMBER RSQUARE'
	p[0] = ('array_index', p[1], p[3])

def p_expression6(p):#
	'expression : IDENTIFIER LPAREN argues RPAREN'
	p[0] = ('function_call', p[1], ('arguments_fc',p[3]))

def p_expressionii(p):#
	'expression : IDENTIFIER PLUSPLUS'
	p[0] = ('inc_op_after', p[1])

def p_expressionjj(p):#
	'expression : IDENTIFIER MINUSMINUS'
	p[0] = ('dec_op_after', p[1])

def p_expressiony(p):#
	'expression : PLUSPLUS IDENTIFIER'
	p[0] = ('inc_op_before', p[2])

def p_expressionz(p):#
	'statement : MINUSMINUS IDENTIFIER'
	p[0] = ('dec_op_before', p[2])

def p_expression10(p):#
	'''expression : expression PLUS expression
				  | expression MINUS expression
				  | expression DIVIDE expression
				  | expression TIMES expression
				  | expression MOD expression'''
	p[0] = 'binop', p[1],p[2],p[3]

def p_expression121212(p):
	'expression : IDENTIFIER DOT IDENTIFIER'
	p[0] = ('object_var', p[1],p[2],p[3])

# def p_data0(p):
# 	'data : '
# 	p[0] = []

def p_data1(p):#
	'data : data COMMA data'
	p[0] = p[1], p[3]

def p_data2(p):#
	'data : WORD'
	p[0] = ('worddata', p[1])

def p_data3(p):#
	'data : CHARACTER'
	p[0] = ('characterdata', p[1])

def p_data4(p):#
	'data : BOOLVALUE'
	p[0] = ('booldata', p[1])

def p_data5(p):#
	'data : NUMBER'
	p[0] = ('numberdata', p[1])

def p_for0(p):#
	'forstat : FOR LPAREN INT IDENTIFIER EQUAL foreq SEMICOLON IDENTIFIER operator foreq SEMICOLON IDENTIFIER forop RPAREN LBRACE cpp RBRACE'
	p[0] = ('for_statement_int', ('forinitialize',p[4],p[6]), ('forcompare', p[8],p[9],p[10]),('forchanger',p[12],p[13]),('insidefor',p[16]))

def p_for1(p):#
	'forstat : FOR LPAREN IDENTIFIER EQUAL foreq SEMICOLON IDENTIFIER operator foreq SEMICOLON IDENTIFIER forop RPAREN LBRACE cpp RBRACE'
	p[0] = ('for_statement_noint', ('forinit2',p[3],p[5]), ('forcompare',p[7],p[8],p[9]),('forchanger',p[11],p[12]),('insidefor',p[15]))

def p_forop(p):#
	'forop : PLUSPLUS'
	p[0] = ('inc_op', p[1])

def p_forop1(p):#
	'forop : MINUSMINUS'
	p[0] = ('dec_op', p[1])

def p_foreq1(p):#
	'foreq : NUMBER'
	p[0] = ('number', p[1])

def p_foreq2(p):#
	'foreq : IDENTIFIER'
	p[0] = ('identifier', p[1])

def p_if1(p):#
	'ifstat : IF LPAREN variable operator variable RPAREN LBRACE saleem RBRACE'
	p[0] = ('if_statement', ('ifcomparison',p[3], p[4], p[5]), ('insideif',p[8]))

def p_ifret(p):#
	'ifstat : IF LPAREN variable operator variable RPAREN LBRACE saleem jameel RBRACE'
	p[0] = ('if_statement_return', ('ifcomparison',p[3], p[4], p[5]), p[8], p[9])

def p_if2(p):#
	'ifstat : IF LPAREN variable operator variable RPAREN LBRACE saleem RBRACE ELSE LBRACE saleem RBRACE'
	p[0] = ('if_else_statement', ('ifcomparison',p[3], p[4], p[5]), ('insideif',p[8]), ('elsestatement', ('insideelse',p[12])))

def p_if2ret(p):#
	'ifstat : IF LPAREN variable operator variable RPAREN LBRACE saleem jameel RBRACE ELSE LBRACE saleem jameel RBRACE'
	p[0] = ('if_else_statement_return', ('ifcomparison',p[3], p[4], p[5]), p[8], p[9],p[13],p[14])

def p_if3(p):#
	'ifstat : IF LPAREN variable operator variable RPAREN LBRACE saleem RBRACE ELSE ifstat'
	p[0] = ('if_elseif_statement', ('ifcomparison',p[3], p[4], p[5]), ('insideif',p[8]), ('elseifseries',p[11]))

def p_if3ret(p):#
	'ifstat : IF LPAREN variable operator variable RPAREN LBRACE saleem jameel RBRACE ELSE ifstat'
	p[0] = ('if_elseif_statement_return', ('ifcomparison',p[3], p[4], p[5]), p[8], p[9], p[12])

def p_jameel1(p):#
	'jameel : '
	p[0] = []

def p_jameel2(p):#
	'jameel : RETURN expression SEMICOLON'
	p[0] = ('return', p[2])


def p_if4(p):#
	'andor : OROR'
	p[0] = ('or' , p[1])

def p_if5(p):#
	'andor : ANDAND'
	p[0] = ('and' , p[1])

def p_ifx(p):#
	'andor : '
	p[0] = [ ]

def p_if6(p):#
	'ifstat : IF LPAREN ifstat1 andor ifstat1 RPAREN LBRACE saleem RBRACE'
	p[0] = ('if_statement_mul', ('ifcomparisonsss',p[3], p[4], p[5]), ('insideif',p[8]))

def p_if6ret(p):#
	'ifstat : IF LPAREN ifstat1 andor ifstat1 RPAREN LBRACE saleem jameel RBRACE'
	p[0] = ('if_statement_return_mul', ('ifcomparisonsss',p[3], p[4], p[5]), ('insideif',p[8],p[9]))

def p_if7(p):#
	'ifstat1 : variable operator variable'
	p[0] = ('ifcomparison', p[1],p[2],p[3])

def p_if10(p):#
	'ifstat1 : ifstat1 andor ifstat1'
	p[0] = ('arguments_if', p[1], p[2], p[3])

def p_ify(p):#
	'ifstat1 : '
	p[0] = []

def p_if8(p):#
	'ifstat : IF LPAREN ifstat1 andor ifstat1 RPAREN LBRACE saleem RBRACE ELSE LBRACE saleem RBRACE'
	p[0] = ('if_else_statement_mul', ('ifcomparisonsss',p[3], p[4], p[5]), ('insideif',p[8]), ('elsestatement',('insideelse', p[12])))

def p_if8return(p):#
	'ifstat : IF LPAREN ifstat1 andor ifstat1 RPAREN LBRACE saleem jameel RBRACE ELSE LBRACE saleem jameel RBRACE'
	p[0] = ('if_else_statement_return_mul', ('ifcomparisonsss',p[3], p[4], p[5]), ('insideif',p[8], p[9]), p[13],p[14])


def p_saleem1(p):#
	'saleem : '
	p[0] = []

def p_saleem2(p):#
	'saleem : element saleem'
	p[0] = p[1],p[2]

# def p_saleem3(p):
# 	'saleem : RETURN NUMBER SEMICOLON'
# 	p[0] = ('return', p[2])

def p_if9(p):#
	'ifstat : IF LPAREN ifstat1 andor ifstat1 RPAREN LBRACE saleem RBRACE ELSE ifstat'
	p[0] = ('if_elseif_statement_mul', ('ifcomparisonsss',p[3], p[4], p[5]), ('insideif',p[8]), p[11])

def p_if9return(p):#
	'ifstat : IF LPAREN ifstat1 andor ifstat1 RPAREN LBRACE saleem jameel RBRACE ELSE ifstat'
	p[0] = ('if_elseif_statement_return_mul', ('ifcomparisonsss',p[3], p[4], p[5]),('insideif', p[8], p[9]), ('elseifseries', p[12]))

def p_ope1(p):#
	'operator : EQUALEQUAL'
	p[0] = ('comparison_operator',p[1])
def p_ope2(p):#
	'operator : GE'
	p[0] = ('comparison_operator',p[1])
def p_ope3(p):#
	'operator : LE'
	p[0] = ('comparison_operator',p[1])
def p_ope4(p):#
	'operator : NOT EQUAL'
	p[0] = ('comparison_operator',p[1]+p[2])
def p_ope5(p):#
	'operator : GT'
	p[0] = ('comparison_operator',p[1])
def p_ope6(p):#
	'operator : LT'
	p[0] = ('comparison_operator',p[1])

def p_var1(p):#
	'variable : IDENTIFIER'
	p[0] = ('compare_identifier',p[1])
def p_var2(p):#
	'variable : NUMBER'
	p[0] = ('compare_number',p[1])
def p_var3(p):#
	'variable : BOOLVALUE'
	p[0] = ('compare_bool',p[1])
def p_var4(p):#
	'variable : CHARACTER'
	p[0] = ('compare_char',p[1])
def p_var5(p):#
	'variable : WORD'
	p[0] = ('compare_word',p[1])
def p_var6(p):#
	'variable : IDENTIFIER LSQUARE NUMBER RSQUARE'
	p[0] = ('compare_array_element',p[1],p[3])

def p_output(p):#
	'statement : COUT to_output SEMICOLON'
	p[0] = 'cout_statement', p[2]

def p_output1(p):#
	'to_output : LT LT expression more'
	p[0] = p[3], p[4]

def p_output2(p):#
	'to_output : LT LT ENDL more'
	p[0] = p[3], p[4]

# def p_output2(p):
# 	'to_output : LT LT NUMBER more'
# 	p[0] = ('output_number', p[3], p[4])

# def p_output3(p):
# 	'to_output : LT LT WORD more'
# 	p[0] = ('output_word', p[3], p[4])

# def p_output4(p):
# 	'to_output : LT LT CHARACTER more'
# 	p[0] = ('output_identifier', p[3], p[4])

# def p_output5(p):
# 	'to_output : LT LT BOOLVALUE more'
# 	p[0] = ('output_boolvalue', p[3], p[4])

# def p_output6(p):
# 	'to_output : LT LT ENDL more'
# 	p[0] = ('output_endl', p[3], p[4])

def p_more1(p):#
	'more : '
	p[0] = [ ]

def p_more2(p):#
	'more : to_output'
	p[0] = p[1]


def p_function1(p):#
	'''func : INT IDENTIFIER LPAREN args RPAREN LBRACE saleem RETURN expression SEMICOLON RBRACE
			| DOUBLE IDENTIFIER LPAREN args RPAREN LBRACE saleem RETURN expression SEMICOLON RBRACE
			| BOOL IDENTIFIER LPAREN args RPAREN LBRACE saleem RETURN expression SEMICOLON RBRACE
			| CHAR IDENTIFIER LPAREN args RPAREN LBRACE saleem RETURN expression SEMICOLON RBRACE
			| STRING IDENTIFIER LPAREN args RPAREN LBRACE saleem RETURN expression SEMICOLON RBRACE'''
	p[0] = ('function_initialize', p[1], p[2], ('arguments_func',p[4]), p[7],p[8],p[9])


def p_function12(p):#
	'''func : INT IDENTIFIER LPAREN args RPAREN LBRACE saleem RBRACE
			| DOUBLE IDENTIFIER LPAREN args RPAREN LBRACE saleem RBRACE
			| BOOL IDENTIFIER LPAREN args RPAREN LBRACE saleem RBRACE
			| CHAR IDENTIFIER LPAREN args RPAREN LBRACE saleem RBRACE
			| STRING IDENTIFIER LPAREN args RPAREN LBRACE saleem RBRACE'''
	p[0] = ('function_initialize', p[1], p[2], ('arguments_func',p[4]), p[7])


def p_function2(p):#
	'func : VOID IDENTIFIER LPAREN args RPAREN LBRACE element RBRACE'
	p[0] = ('function_initialize_void', p[1], p[2], p[4], p[7])

# def p_type1(p):
# 	'''type : VOID
# 			| BOOL
# 			| CHAR
# 			| STRING
# 			| INT
# 			| DOUBLE'''
# 	p[0] = p[1]


def p_args(p):#
	'''args : INT IDENTIFIER moreargs
			| DOUBLE IDENTIFIER moreargs
			| CHAR IDENTIFIER moreargs
			| STRING IDENTIFIER moreargs
			| BOOL IDENTIFIER moreargs '''
	p[0] =  p[1],p[2],p[3]


def p_args_arrays(p):#
	'''args : INT IDENTIFIER LSQUARE RSQUARE moreargs
			| DOUBLE IDENTIFIER LSQUARE RSQUARE moreargs
			| CHAR IDENTIFIER LSQUARE RSQUARE moreargs
			| STRING IDENTIFIER LSQUARE RSQUARE moreargs
			| BOOL IDENTIFIER LSQUARE RSQUARE moreargs '''
	p[0] =  p[1],p[2]+p[3]+p[4]

def p_moreargs(p):#
	'moreargs : '
	p[0] = [ ]

def p_moreargs1(p):#
	'moreargs : COMMA args'
	p[0] = p[2]


# def p_clasas1(p):
# 	'classy : CLASSES'
# 	p[0] = p[1]

def p_class0(p):
	'classy : CLASSES IDENTIFIER LBRACE PUBLIC COLON stufffff RBRACE SEMICOLON'
	p[0] = ('class_declaration', p[2], ('classvariables',p[6]))

def p_class1(p):
	'stufffff : stuffbud stufffff'
	p[0] = p[1], p[2]

def p_class2(p):
	'stufffff : '
	p[0] = []

def p_classobject(p):
	'statement : IDENTIFIER IDENTIFIER SEMICOLON'
	p[0] = ('classobject_created', p[1], p[2])

def p_accessandedit(p):
	'statement : IDENTIFIER DOT IDENTIFIER EQUAL variable SEMICOLON'
	p[0] = ('object_var_update', p[1],p[2],p[3], p[5])


def p_stuffff1212(p):#
	'''stuffbud : INT IDENTIFIER SEMICOLON
				 | STRING IDENTIFIER SEMICOLON
				 | CHAR IDENTIFIER SEMICOLON
				 | BOOL IDENTIFIER SEMICOLON
				 | DOUBLE IDENTIFIER SEMICOLON	'''
	p[0] = ('var_declare_class', p[1],p[2])

# print arrays

# if statemenet ko check kareen zara
# phir uskay baad for loops check kareen
# aur phir tunay functions kay saath recursion try karni hai
# aur tunay boolean 0,1 nahi kiya aur na hi nested paranetheses





def eval_exp(objects,tree, all_classes, variables, arrays):  
    nodetype = tree[0]
    # print tree
    # if nodetype == 'a':
    # print nodetype
    if nodetype == "numbervalue" or nodetype == "numberdata" or nodetype == "compare_number" or nodetype is "number":
        return tree[1]
    elif nodetype is "endl":
        print "endl"
    elif nodetype == "stringvalue" or nodetype == "worddata" or nodetype == "compare_word":
        return tree[1]
    elif nodetype == "identifiername" or nodetype is "compare_identifier" or nodetype is "identifier":
        if(tree[1] in variables):
            return variables[tree[1]]
        else:
            print "Variable not declared."
            exit()
    elif nodetype == "charactervalue" or nodetype == "characterdata" or nodetype == "compare_char":
        # print "supsasas"
        return tree[1]
    elif nodetype == "boolvalue" or nodetype == "booldata" or nodetype == "compare_bool":
        return tree[1]
    elif nodetype == "comparison_operator":
        return tree[1]
    elif nodetype is "array_index" or nodetype == "compare_array_element":
        # print "sup111"
        # print arrays
        if(tree[1] in arrays):
            list_of_array = (arrays[tree[1]])[2]
            return list_of_array
        else:
			# print arrays
			print "Array not declared 1"
			exit()
    elif nodetype is "forinitialize":
        # print tree[2]
        initialval = eval_exp(objects,tree[2], all_classes,variables,arrays)
        variables[tree[1]] = ('int', initialval)
        return tree[1]
        # variables[tree[1]]
    elif nodetype == "inc_op_after":
        if tree[1] in variables:
            getval = (variables[tree[1]])[1]
            newtuple = ((variables[tree[1]])[0], getval + 1)
            variables[tree[1]] = newtuple
            return getval
        elif tree[1] in arrays:
            print "in arrays"
        else:
            print "Variable not declared"
    elif nodetype == "dec_op_after":
        if tree[1] in variables:
            getval = (variables[tree[1]])[1]
            newtuple = ((variables[tree[1]])[0], getval - 1)
            variables[tree[1]] = newtuple
            return getval
        elif tree[1] in arrays:
            print "in arrays"
        else:
            print "Variable not declared"
    elif nodetype == "inc_op_before":
        if tree[1] in variables:
            getval = (variables[tree[1]])[1]
            newtuple = ((variables[tree[1]])[0], getval + 1)
            variables[tree[1]] = newtuple
            return getval + 1
        elif tree[1] in arrays:
            print "in arrays"
        else:
            print "Variable not declared"
    elif nodetype == "dec_op_before":
        if tree[1] in variables:
            getval = (variables[tree[1]])[1]
            newtuple = ((variables[tree[1]])[0], getval - 1)
            variables[tree[1]] = newtuple
            return getval - 1
        elif tree[1] in arrays:
            print "in arrays"
        else:
            print "Variable not declared"
    elif nodetype == "array_data":
        arraydata = []
        treeinstance = tree[1]
        while (type(treeinstance) is not int or type(treeinstance) is not str or type(treeinstance) is not bool or type(treeinstance) is not float):
            if(type(treeinstance[1]) is int or type(treeinstance[1]) is str or type(treeinstance[1]) is bool or type(treeinstance[1]) is float):
                arraydata.append(eval_exp(objects,treeinstance, all_classes, variables, arrays))
                break
            else:
                arraydata.append(eval_exp(objects,treeinstance[0], all_classes, variables, arrays))
                treeinstance = treeinstance[1] 
        return arraydata
    elif nodetype == "binop":
        left_child = tree[1]
        operator = tree[2]
        right_child = tree[3]
        left_val = 0
        xyz = eval_exp(objects,left_child, all_classes, variables, arrays)
        if (type(xyz) is list):
            left_val = xyz[left_child[2]]
        else:
            left_val = xyz
        right_val = eval_exp(objects,right_child, all_classes, variables, arrays)
        if operator == "+":
            return left_val + right_val
        elif operator == "-":
            return left_val - right_val
        elif operator == "*":
            return left_val * right_val
        elif operator == "/":
            return left_val / right_val
        elif operator == "%":
            return left_val % right_val
    elif nodetype is "array_value_replace":
        if tree[3] in arrays and tree[1] in arrays:
            array_of_left = (arrays[tree[1]])[2]
            array_of_right = (arrays[tree[3]])[2]
            # print array_of_left
            # print array_of_right
            if(tree[2] > len(array_of_left) or tree[4] > len(array_of_right)):
                print "Index out of bounds"
                exit()
            else:
                array_of_left[tree[2]] = array_of_right[tree[4]]
                arrays[tree[1]] = ((arrays[tree[1]])[0],array_of_left)
        else:
            print "Array not declared"
            exit()
    elif nodetype is "array_index_equal":
        if(tree[1] in arrays):
            # print tree[2], "\n"
            # print tree[3], "\n"
            to_equate =  eval_exp(objects,tree[3], all_classes, variables, arrays)
            type_of_array = (arrays[tree[1]])[0] 
            type_to_equate = tree[3][0]
            if (type_of_array is 'int' and (type_to_equate is "numbervalue" or type_to_equate is "inc_op_after" or type_to_equate is "inc_op_before" or type_to_equate is "dec_op_before" or type_to_equate is "dec_op_after")) or (type_of_array is 'string' and type_to_equate is "stringvalue") or (type_of_array is 'char' and type_to_equate is "charactervalue") or (type_of_array is 'bool' and type_to_equate is "boolvalue") or (type_of_array is 'double' and type_to_equate is "numbervalue"):
                array_to_change = arrays[tree[1]][2]
                if(tree[2] > len(array_to_change)):
                    print "Index out of bounds"
                    exit()
                else:
                    array_to_change[tree[2]] = to_equate
                    arrays[tree[1]] = (type_of_array, (arrays[tree[1]])[1]  ,array_to_change)
            else:
                print "Types dont match meri jaan"
                exit()
        else:
            "Array not declared"
            exit()
    elif nodetype == "cout_statement":
        # print "in cout statement ||||||||||||"
        child = tree[1]
        # print child[0]
        while child is not []:
            # print child[0]
            # print child
            if(child[0] == "endl"):
                print "\n"
                # print "sexadsdafasdwqddasdasdasdas"
                child = child[1]
                if(child == []):
                    break
                # break
                # print "adsadasdasdasd"
            else:
                value = eval_exp(objects,child[0],all_classes, variables, arrays)
                if(value != None):
                    if(type(value) is tuple):
                        print value[1]
                    elif(type(value) is list):
                        if((child[0])[2] < len(value)):
                            print value[(child[0])[2]]
                        else:
                            print "Index value out of range"
                    else:
        	        	print value
                child = child[1]
                if(child == []):
                    break


    elif nodetype == "var_declare":
        if(tree[2] in variables):
            print "Variable name \"",tree[2],"\" already declared"
        else:
            variables[tree[2]] = (tree[1], None)
    elif nodetype == "var_assign":
        # print "var_assign", tree
        # print tree[2]
        value = eval_exp(objects,tree[2], all_classes, variables, arrays)
        # print value
        type_of_val = type(value)
        # print type_of_val
        if(tree[1] in variables):
            art = variables[tree[1]]
            # print art[0]
            if (type_of_val is int and art[0] == 'int') or (type_of_val is float and art[0] == 'double') or (type_of_val is str and art[0] == 'string') or (type_of_val is str and art[0] == 'char') or (type_of_val is bool and art[0] == 'bool'):
                toput = (art[0], value)
                variables[tree[1]] = toput
            elif type_of_val is tuple and art[0] in 'int':
                toput = value[1] + value[3]
                # print toput
                variables[tree[1]] = (art[0],toput)
            else:
                print "Types dont match 0"
                exit()
        else:
            print "Variable not declared"
            exit()
    elif nodetype == "var_declare_assign":
        if(tree[2] in variables):
            print "Variable name \"",tree[2],"\" already declared"
        else:
            type_of_input = tree[1]
            to_match = (tree[3])[0]
            if type_of_input=='int' and to_match=="numbervalue":
                num = eval_exp(objects,tree[3], all_classes, variables, arrays)
                variables[tree[2]] = (tree[1], num)
            elif type_of_input=='string' and to_match=="stringvalue":
                num = eval_exp(objects,tree[3], all_classes, variables, arrays)
                variables[tree[2]] = (tree[1], num)
            elif type_of_input=='char' and to_match=="charactervalue":
                num = eval_exp(objects,tree[3], all_classes, variables, arrays)
                variables[tree[2]] = (tree[1], num)
            elif type_of_input=='bool' and to_match=="boolvalue":
                num = eval_exp(objects,tree[3], all_classes, variables, arrays)
                variables[tree[2]] = (tree[1], num)
            elif type_of_input=='double' and to_match=="numbervalue":
                num = eval_exp(objects,tree[3], all_classes, variables, arrays)
                variables[tree[2]] = (tree[1], num)
            elif type_of_input=='int' and to_match=="identifiername":
                num = eval_exp(objects,tree[3], all_classes, variables, arrays)
                if(num is not None and num[0] == type_of_input):
                    variables[tree[2]] = (tree[1], num[1])
                elif num is None:
                    exit()
                else:    
                    print "Types don't match"
            elif type_of_input=='string' and to_match=="identifiername":
                num = eval_exp(objects,tree[3], all_classes, variables, arrays)
                if(num is not None and num[0] == type_of_input):
                    variables[tree[2]] = (tree[1], num[1])
                else:
                    print "Types don't match"
            elif type_of_input=='char' and to_match=="identifiername":
                num = eval_exp(objects,tree[3], all_classes, variables, arrays)
                if(num is not None and num[0] == type_of_input):
                    variables[tree[2]] = (tree[1], num[1])
                elif num is None:
                    exit()
                else:    
                    print "Types don't match"
            elif type_of_input=='bool' and to_match=="identifiername":
                num = eval_exp(objects,tree[3], all_classes, variables, arrays)
                if(num is not None and num[0] == type_of_input):
                    variables[tree[2]] = (tree[1], num[1])
                elif num is None:
                    exit()
                else:    
                    print "Types don't match"
            elif type_of_input=='double' and to_match=="identifiername":
                num = eval_exp(objects,tree[3], all_classes, variables, arrays)
                if(num is not None and num[0] == type_of_input):
                    variables[tree[2]] = (tree[1], num[1])
                elif num is None:
                    exit()
                else:    
                    print "Types don't match"
            elif (type_of_input is 'int' or type_of_input is 'double') and to_match is 'binop':
                num = eval_exp(objects,tree[3], all_classes, variables, arrays)
                variables[tree[2]] = (tree[1],num)
            elif type_of_input == 'int' and to_match is "inc_op_after":
                ret = eval_exp(objects,tree[3], all_classes, variables, arrays)
                if type(ret) == int:
                    variables[tree[2]] = (tree[1], ret)
                else:
                    print "Types dont match 4"
                    exit()
            elif type_of_input == 'int' and to_match is "dec_op_after":
                ret = eval_exp(objects,tree[3], all_classes, variables, arrays)
                if type(ret) == int:
                    variables[tree[2]] = (tree[1], ret)
                else:
                    print "Types dont match 3"
                    exit()
            elif type_of_input == 'int' and to_match is "inc_op_before":
                ret = eval_exp(objects,tree[3], all_classes, variables, arrays)
                if type(ret) == int:
                    variables[tree[2]] = (tree[1], ret)
                else:
                    print "Types dont match 2"
                    exit()
            elif type_of_input == 'int' and to_match is "dec_op_before":
                ret = eval_exp(objects,tree[3], all_classes, variables, arrays)
                if type(ret) == int:
                    variables[tree[2]] = (tree[1], ret)
                else:
                    print "Types dont match 1"
                    exit()
            elif type_of_input == 'int' and to_match is "dec_op_after":
                ret = eval_exp(objects,tree[3], all_classes, variables, arrays)
            elif type_of_input == 'int' and to_match is "inc_op_before":
                ret = eval_exp(objects,tree[3], all_classes, variables, arrays)
            elif type_of_input == 'int' and to_match is "dec_op_before":
                ret = eval_exp(objects,tree[3], all_classes, variables, arrays)
            elif to_match in "array_index" and type_of_input == 'int':
                if((tree[3])[1] in arrays):
                    if type_of_input == (arrays[(tree[3])[1]])[0]:
                        ret = eval_exp(objects,tree[3], all_classes, variables, arrays)
                        value_to_access = (tree[3])[2]
                        if(value_to_access > len(ret)):
                            print "List index out of range"
                            exit()
                        else:
                            variables[tree[2]] = (tree[1], ret[value_to_access])
                    else:
                        print "Types don't match"
            else:
                print "Syntax error in input. Types don't match"
    elif nodetype == "array_declare":
    	if(tree[2] in arrays):
    		print "Array name already declared"
    	else:
	    	arrays[tree[2]] = (tree[1], tree[3], None)
    elif nodetype is "array_declare_size_assign":
        getlist = eval_exp(objects,tree[4],all_classes,variables,arrays)
        length = len(getlist)
        # print getlist
        # print tree[1]
        if (length is tree[3]):
			for x in range(length):
				if tree[1] in 'int':
					if not isinstance(getlist[x], int):
						print "Type of array and data does not match1"
						exit()
					else:
						# print "declared"
						arrays[tree[2]] = (tree[1],tree[3],getlist)
				elif tree[1] in 'double':
					if not isinstance(getlist[x], float):
						print "Type of array and data does not match2"
						exit()
					else:
						arrays[tree[2]] = (tree[1],tree[3],getlist)
				elif tree[1] in 'bool':
					if not isinstance(getlist[x], bool):
						print "Type of array and data does not match3"
						exit()
					else:
						arrays[tree[2]] = (tree[1],tree[3],getlist)
				elif tree[1] in 'string':
					if not isinstance(getlist[x], str):
						print "Type of array and data does not match4"
						exit()
					else:
						arrays[tree[2]] = (tree[1],tree[3],getlist)
				elif tree[1] in 'char':
					if isinstance(getlist[x], str) and len(getlist[x]) is not 1:
						print "Type of array and data does not match5"
						exit()
				elif not isinstance(getlist[x], str):
					print "Type of array and data does not match6"
					exit()
				else:
					arrays[tree[2]] = (tree[1],tree[3],getlist)
	else:
			print "no match"
    elif nodetype is "array_declare_assign":
        getlist = eval_exp(objects,tree[3], all_classes, variables, arrays)
        # print getlist
        length = len(getlist)
        for x in range(length):
            if tree[1] in 'int':
                if not isinstance(getlist[x], int):
                    print "Type of array and data does not match"
                    exit()
                else:
                    arrays[tree[2]] = (tree[1], None ,getlist)
            elif tree[1] in 'double':
                if not isinstance(getlist[x], float):
                    print "Type of array and data does not match"
                    exit()
                else:
                    arrays[tree[2]] = (tree[1], None ,getlist)
            elif tree[1] in 'bool':
                if not (getlist[x] in 'false' or getlist[x] in 'true'):
                    # print getlist[x]
                    print "Type of array and data does not match"
                    exit()
                else:
                    arrays[tree[2]] = (tree[1], None ,getlist)
            elif tree[1] in 'string':
                if not isinstance(getlist[x], str):
                    # print getlist[x]
                    print "Type of array and data does not match"
                    exit()
                else:
                    arrays[tree[2]] = (tree[1], None ,getlist)
            elif tree[1] in 'char':
                if isinstance(getlist[x], str) and len(getlist[x]) is not 1:
                    # print getlist[x]
                    print "Type of array and data does not mat"
                    exit()
                elif not isinstance(getlist[x], str):
                    print "Type of array and data does not match"
                    exit()                   
                else:
                    arrays[tree[2]] = (tree[1], None ,getlist)
    elif nodetype is "ifcomparison":
        # print "tree[3]", tree[3]
        # print tree
        val_left = eval_exp(objects,tree[1], all_classes, variables, arrays)
        # print "val_left", val_left
        val_lefty = val_left
        # print val_left
        val_op = eval_exp(objects,tree[2], all_classes, variables, arrays)
        # print "val_op", val_op
        val_right = eval_exp(objects,tree[3], all_classes, variables, arrays)
        # print "val_right",val_right
        # print val_left is list 
        # print "here"
        if type(val_left) is list or type(val_right) is list:
            # print "tree[1", tree[1]
            array_type = arrays[tree[1][1]][0]
            # print array_type
            if (tree[1][2] > len(val_left)):
                print "list index out of range"
            else:
                val_lefty = val_left[tree[1][2]]
                val_left[0] = array_type
                # print val_lefty, val_left[0]
                # print "sup"
            # print "is list"
            # exit() 
        # print type(val_left)
        # print type(val_right) 
        if (type(val_left) is tuple) or (type(val_right) is tuple):
            # print "in"
            # print val_left[0] in "int" and type(val_right) is int
            if (val_left[0] in "int" and type(val_right) is int) or (val_left[0] in "string" and type(val_right) is str) or (val_left[0] in "double" and type(val_right) is float) or (val_left[0] in "bool" and type(val_right) is bool) or (val_left[0] in "char" and type(val_right) is str):
                # print "sup"
                if val_op == "<":
                    return val_left[1] < val_right
                elif val_op == ">":
                    return val_left[1] > val_right
                elif val_op == "<=":
                    return val_left[1] <= val_right
                elif val_op == ">=":
                    return val_left[1] >= val_right
                elif val_op == "!=":
                    return val_left[1] != val_right
                elif val_op == "==":
                    return val_left[1] == val_right
                else:
                    return False
            elif (val_left[0] is "int" and val_right[0] is "int") or (val_left[0] is "string" and val_right[0] is "string") or (val_left[0] is "double" and val_right[0] is "double") or (val_left[0] is "bool" and val_right[0] is "bool") or (val_left[0] is "char" and val_right[0] is "bool"):
                if val_op == "<":
                    return val_left[1] < val_right
                elif val_op == ">":
                    return val_left[1] > val_right
                elif val_op == "<=":
                    return val_left[1] <= val_right
                elif val_op == ">=":
                    return val_left[1] >= val_right
                elif val_op == "!=":
                    return val_left[1] != val_right
                elif val_op == "==":
                    return val_left[1] == val_right
                else:
                    return False
        elif (type(val_left) is int and type(val_right) is int) or (type(val_left) is str and type(val_right) is str) or (type(val_left) is float and type(val_right) is float) or (type(val_left) is bool and type(val_right) is bool) or (type(val_left) is str and type(val_right) is str):
            if val_op == "<":
                return val_left < val_right
            elif val_op == ">":
                return val_left > val_right
            elif val_op == "<=":
                return val_left <= val_right
            elif val_op == ">=":
                return val_left >= val_right
            elif val_op == "!=":
                return val_left != val_right
            elif val_op == "==":
                return val_left == val_right
            else:
                return False
        else:
            print "Types don't match"
            exit()
    elif nodetype is "insideif" or nodetype is "insideelse":
        # print "insideif"
        child = tree[1]

        while 1:
            # print child
            # print child == []
            if(child == []):
                break
            else:
                eval_exp(objects,child[0], all_classes, variables, arrays)
                child = child[1]

        length = len(tree[1])
        # eval_exp(objects,tree[1][0], all_classes, variables, arrays)
    elif nodetype is "if_statement":
        # print "tree[0]", tree[0]
        truth = eval_exp(objects,tree[1], all_classes, variables, arrays)
        if truth == True:
            eval_exp(objects,tree[2], all_classes, variables, arrays)
            #this will only do it for one statement inside if
        else:
            print "Condition not met"
        # print "tree[1]", tree[1]
    elif nodetype is "elsestatement":
        # print tree
        # print tree[1], "\n"
        eval_exp(objects,tree[1], all_classes, variables, arrays)
        # print "elsestatementasdsadsad"
    elif nodetype is "if_else_statement":
        truth = eval_exp(objects,tree[1], all_classes, variables, arrays)
        # print truth
        if truth == True:
            eval_exp(objects,tree[2], all_classes, variables, arrays)
        else:
            eval_exp(objects,tree[3], all_classes, variables, arrays)

    elif nodetype is "elseifseries":
        # print tree[0]
        # print tree[1]
        eval_exp(objects,tree[1], all_classes, variables, arrays)
        # print "sexbomb"
    elif nodetype is "if_elseif_statement":

        truth = eval_exp(objects,tree[1], all_classes, variables, arrays)
        # print truth
        # truth = True
        if truth == True:
            eval_exp(objects,tree[2], all_classes, variables, arrays)
        else:
            eval_exp(objects,tree[3], all_classes, variables, arrays)
    elif nodetype is "ifcomparisonsss":

        left_truth = eval_exp(objects,tree[1], all_classes, variables, arrays)
        op = tree[2][1]
        right_truth = eval_exp(objects,tree[3], all_classes, variables, arrays)
        # print left_truth, right_truth
        # right_truth = False
        if (op == "&&"):
            return left_truth and right_truth
        elif(op == "||"):
            return left_truth or right_truth
        else:
            # print "sup"
            return False 
    elif nodetype is "if_statement_mul":
        # print tree
        # print tree[0]
        truth1 = eval_exp(objects,tree[1], all_classes, variables, arrays)
        # print truth1
        if truth1 == True:
            eval_exp(objects,tree[2], all_classes, variables, arrays)
        else:
            print "Conditions of if not met."
    elif nodetype is "if_else_statement_mul":
        # print tree[0]
        # print tree
        # print tree[1]
        # print tree[2]
        # print tree[3]
        truth2 = eval_exp(objects,tree[1], all_classes, variables, arrays)
        # print truth2
        # truth2 = False
        if truth2 == True:
            eval_exp(objects,tree[2], all_classes, variables, arrays)
        else:
            eval_exp(objects,tree[3], all_classes, variables, arrays)
    elif nodetype is "if_elseif_statement_mul":
        # print "multiple"
        # print tree[1]
        # print tree[2]
        # print tree[3]
        truth3 = eval_exp(objects,tree[1], all_classes, variables, arrays)
        # print truth3
        if truth3 == True:
            eval_exp(objects,tree[2], all_classes, variables, arrays)
        else:
            eval_exp(objects,tree[3], all_classes, variables, arrays)
        # exit()
    elif nodetype is "forcompare":
        # print tree
        var = tree[1]
        op = eval_exp(objects,tree[2],all_classes,variables,arrays)
        val = eval_exp(objects,tree[3],all_classes,variables,arrays)
        return (var,op,val)
    elif nodetype is "inc_op":
        return tree[1]
    elif nodetype is "dec_op":
        return tree[1]
    elif nodetype is "forchanger":
        var = tree[1]
        change = eval_exp(objects,tree[2],all_classes,variables,arrays)
        return (var, change)
    elif nodetype is "insidefor":
        length = len(tree[1])
        for x in range(length):
            eval_exp(objects,tree[1][x], all_classes, variables, arrays)
    elif nodetype is "for_statement_int":
        var_initialized = eval_exp(objects,tree[1],all_classes,variables,arrays)
        (var1, check, limit) = eval_exp(objects,tree[2],all_classes,variables,arrays)
        (var2, oper) = eval_exp(objects,tree[3],all_classes,variables,arrays)
        val_of_var = (variables[var1])[1]
        if(check is '<'):
            # print val_of_var
            while val_of_var < limit:
                # print "sup1212"
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    # print "val_of_var", val_of_var
                    variables[var1] = (variables[var1][0], val_of_var)
                elif(oper == '--'):
                    val_of_var-=1
                    variables[var1] = (variables[var1][0], val_of_var)
        elif(check is '>'):
            while val_of_var > limit:
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    variables[var1] = (variables[var1][0], val_of_var)
                elif(oper == '--'):
                    val_of_var-=1
                    variables[var1] = (variables[var1][0], val_of_var)
        elif(check is '>='):
            while val_of_var >= limit:
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    variables[var1] = (variables[var1][0], val_of_var)
                elif(oper == '--'):
                    val_of_var-=1
                    variables[var1] = (variables[var1][0], val_of_var)            
        elif(check is '<='):
            while val_of_var <= limit:
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    variables[var1] = (variables[var1][0], val_of_var)
                elif(oper == '--'):
                    val_of_var-=1
                    variables[var1] = (variables[var1][0], val_of_var)
        elif(check is '=='):
            while val_of_var == limit:
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    variables[var1] = (variables[var1][0], val_of_var)
                elif(oper == '--'):
                    val_of_var-=1
                    variables[var1] = (variables[var1][0], val_of_var)            
        elif(check is '!='):
            while val_of_var != limit:
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    variables[var1] = (variables[var1][0], val_of_var)
                elif(oper == '--'):
                    val_of_var-=1 
                    variables[var1] = (variables[var1][0], val_of_var)           
        else:
            exit()
    elif nodetype is "forinit2":
        # print tree[2]
        toeq = eval_exp(objects,tree[2], all_classes,variables,arrays)
        # print toeq
        type_toeq = type(toeq)
        if tree[1] in variables:
            stuff = variables[tree[1]]
            if stuff[0] == 'int' and type_toeq is int:
                newtup = (stuff[0], toeq)
                variables[tree[1]] = newtup
                return tree[1]
            else:
                print "Types dont match bro"
                exit()
        else:
            print "Variable not declared"
            exit()
    elif nodetype is "for_statement_noint":
        # print tree[1]
        var = eval_exp(objects,tree[1], all_classes, variables, arrays)
        (var1, check, limit) = eval_exp(objects,tree[2],all_classes,variables,arrays)
        (var2, oper) = eval_exp(objects,tree[3],all_classes,variables,arrays)
        val_of_var = (variables[var1])[1]
        if(check is '<'):
            # print val_of_var
            while val_of_var < limit:
                # print tree[4], "\n"
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    variables[var1] = (variables[var1][0], val_of_var)
                elif(oper == '--'):
                    val_of_var-=1
                    variables[var1] = (variables[var1][0], val_of_var)
        elif(check is '>'):
            while val_of_var > limit:
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    variables[var1] = (variables[var1][0], val_of_var)

                elif(oper == '--'):
                    val_of_var-=1
                    variables[var1] = (variables[var1][0], val_of_var)

        elif(check is '>='):
            while val_of_var >= limit:
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    variables[var1] = (variables[var1][0], val_of_var)

                elif(oper == '--'):
                    val_of_var-=1
                    variables[var1] = (variables[var1][0], val_of_var)

        elif(check is '<='):
            while val_of_var <= limit:
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    variables[var1] = (variables[var1][0], val_of_var)

                elif(oper == '--'):
                    val_of_var-=1
                    variables[var1] = (variables[var1][0], val_of_var)

        elif(check is '=='):
            while val_of_var == limit:
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    variables[var1] = (variables[var1][0], val_of_var)
                elif(oper == '--'):
                    val_of_var-=1 
                    variables[var1] = (variables[var1][0], val_of_var)           
        elif(check is '!='):
            while val_of_var != limit:
                eval_exp(objects,tree[4], all_classes,variables,arrays)
                if(oper == '++'):
                    val_of_var+=1
                    variables[var1] = (variables[var1][0], val_of_var)
                elif(oper == '--'):
                    val_of_var-=1 
                    variables[var1] = (variables[var1][0], val_of_var)           
        else:
            exit()
    elif nodetype is "var_declare_class":
        return (tree[1],tree[2])
    elif nodetype is "classvariables":
        # print tree[1]
        alltups = ()
        child = tree[1]
        while child is not []:
            if child == []:
                break
            else:
                tup = eval_exp(objects,child[0], all_classes, variables, arrays)
                child = child[1]
                alltups += tup
        # print tree[1][0]
        return alltups
        # print tree[1][1]
        # print tree[1][1][0]
        # print tree[1][1][1][0]
    elif nodetype is "class_declaration":
        # print tree
        # print tree[2]
        ret = eval_exp(objects,tree[2], all_classes, variables, arrays)
        all_classes[tree[1]] = ret
    elif nodetype is "classobject_created":
        # print tree
        if (tree[1] in all_classes):
            abcalpha = []
            variables122 = all_classes[tree[1]]
            x = 0
            while x < len(variables122):
                abcalpha.append((variables122[x+1],None))
                x = x+2
                # objects[tree[2]] = variables122
            objects[tree[2]] = abcalpha
        else:
            print "Class not declared"
    elif nodetype is "object_var_update":
        # print tree
        if(tree[1] in objects):
            if(tree[2] == '.'):
                length = len(objects[tree[1]])
                # print length
                y = 0
                while y < length:
                    boo = tree[3] in (objects[tree[1]])[y]
                    if boo == True:
                        new_val = eval_exp(objects,tree[4],all_classes,variables,arrays)
                        objects[tree[1]][y] = (objects[tree[1]][y][0], new_val) 
                        # print new_val
                        y +=1
                    else:
                        y+=1
            else:
                print "invalid operand"
                exit()
        else:
            print "Object not declared"
            exit()
    elif nodetype is "object_var":
        # print tree
        if tree[1] in objects:
            if tree[2] == '.':
                length = len(objects[tree[1]])
                y = 0
                while y < length:
                    boo = tree[3] in (objects[tree[1]])[y]
                    if boo == True:
                        # new_val = eval_exp(objects,tree[4],all_classes,variables,arrays)
                        # objects[tree[1]][y] = (objects[tree[1]][y][0], new_val) 
                        return objects[tree[1]][y][1]
                        # print new_val
                        y+=1
                    else:
                        y+=1
            else:
                print "invalid operand"
                exit()
        else:
            print "Object not declared"
            exit()
    elif nodetype == None:
        return None
    else:
        print tree
        eval_exp(objects,tree[1],all_classes, variables, arrays)



def recursion(objects, tree, all_classes, variables, arrays):
    length = len(tree)
    # print length
    for x in range(length):
        eval_exp(objects,tree[x], all_classes, variables, arrays)

arrays = {} # {name: (type, size, values)}
all_classes = {}
variables = {}
objects = {}






# to_print = []
# variables = {}
lexer = lex.lex()
parser = yacc.yacc()

with open(sys.argv[1], 'r') as myfile:
    data=myfile.read().replace('\n', '').replace('\"', '\"')

mystr = data



tree1 = parser.parse(mystr , lexer= lexer)
# print tree1

recursion(objects,tree1, all_classes, variables, arrays)
# recursion(tree1, to_print, variables, arrays)
