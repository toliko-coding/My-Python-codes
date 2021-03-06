# --------------------------------------
# Exp class
# --------------------------------------
class Exp(object):
    """A call expression in Calculator."""
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands
    def __repr__(self):
        return 'Exp({0},{1})'.format(repr(self.operator), 						         repr(self.operands))
    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)
# --------------------------------------
'''
>>> Exp('add', [1, 2])
Exp('add',[1, 2])
>>> str(Exp('add', [1, 2]))
'add(1, 2)'
>>>
'''

# --------------------------------------
# join and map
# --------------------------------------
'''
>>> s = ["a", "b", "c"]
>>> ', '.join(map(str, s))
'a, b, c'
>>> 
'''

# --------------------------------------
# Hierarchical structure
# --------------------------------------
'''
>>> Exp('add', [1, Exp('mul', [2, 3, 4])])
Exp('add',[1, Exp('mul',[2, 3, 4])])
>>> str(Exp('add', [1, Exp('mul', [2, 3, 4])]))
'add(1, mul(2, 3, 4))'
>>> 
'''

# --------------------------------------
# calc_eval
# --------------------------------------
def calc_eval(exp):
    """Evaluate a Calculator expression."""
    if type(exp) in (int, float):
        return exp
    elif type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
    return calc_apply(exp.operator, arguments)


# --------------------------------------
# Applying operator to arguments
# --------------------------------------
from functools import reduce
from operator import mul
def calc_apply(operator, args):
    """Apply the named operator to a list of args."""
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer/denom

# --------------------------------------
'''
>>> args = [1,2,3,4]
>>> args[:1] + [-arg for arg in args[1:]]
[1, -2, -3, -4]
>>> sum(args[:1] + [-arg for arg in args[1:]])
-8
>>> calc_apply('+', [1, 2, 3])
6
>>> calc_apply('-', [10, 1, 2, 3])
4
>>> calc_apply('*', [])
1
>>> calc_apply('/', [40, 5])
8.0
'''

# --------------------------------------
# calc_eval and calc_apply
# --------------------------------------
'''
>>> e = Exp('add', [2, Exp('mul', [4, 6])])
>>> str(e)
'add(2, mul(4, 6))'
>>> calc_eval(e)
26
>>> 
'''

# --------------------------------------
# read_eval_print_loop
# --------------------------------------
'''
def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        expression_tree = calc_parse(input('calc> '))
        print(calc_eval(expression_tree))
'''
# --------------------------------------
# input
# --------------------------------------
'''
while True:
    inp = input('abc> ')
    print('line: ',inp)
'''
'''
abc> hujkh
line:  hujkh
abc> 3+2
line:  3+2
abc> 
Traceback (most recent call last):
  File "D:\BACKUP-DISK-D-19_8_2016\My\SCE\Principles of Programming Languages\2020-summer\Lec\Lec6\lesson-12.py", line 121, in <module>
    inp = input('abc> ')
KeyboardInterrupt
>>>
'''
def func():
    while True:
        try:
            inp = input('abc> ')
            print('line: ',inp)
        except(KeyboardInterrupt, EOFError):
            print('Calculation completed.')
            return
'''
>>> func()
abc> kk
line:  kk
abc> 
Calculation completed.
'''
# --------------------------------------
# read_eval_print_loop
# --------------------------------------
def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError): # <Control>-D, etc.
            print('Calculation completed.')
            return

# --------------------------------------
# calc_parse
# --------------------------------------
def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree

# --------------------------------------
# tokenize
# --------------------------------------
def tokenize(line):
    """Convert a string into a list of tokens."""
    spaced = line.replace('(',' ( ').replace(')',' ) ').replace(',', ' , ')
    return spaced.split()

# --------------------------------------
'''
>>> tokenize('add(2, mul(4, 6))')
['add', '(', '2', ',', 'mul', '(', '4', ',', '6', ')', ')']
'''

# --------------------------------------
# analyze
# --------------------------------------
'''
def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens."""
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    else:
        tokens.pop(0) # Remove (
    return Exp(token, analyze_operands(tokens))
'''
# --------------------------------------
# analyze_operands
# --------------------------------------
'''
def analyze_operands(tokens):
    """Read a list of comma-separated operands."""
    operands = []
    while tokens[0] != ')':
        if operands:
            tokens.pop(0) # Remove ,
        operands.append(analyze(tokens))
    tokens.pop(0) # Remove )
    return operands
'''
# --------------------------------------
# analyze_token
# --------------------------------------
def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token."""
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token

# --------------------------------------
'''
>>> expression = 'add(2, mul(4, 6))'
>>> analyze(tokenize(expression))
Exp('add',[2, Exp('mul',[4, 6])])
>>> str(analyze(tokenize(expression)))
'add(2, mul(4, 6))'
'''

known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/']

# --------------------------------------
# analyze
# --------------------------------------
def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens."""
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected ' + token)

# --------------------------------------
# analyze_operands
# --------------------------------------
def analyze_operands(tokens):
    """Analyze a sequence of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0) # Remove )
    return operands

# --------------------------------------
# assert_non_empty
# --------------------------------------
def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')


'''
calc> add(2,3)
5
calc> add(1, 2, 3, 4)
10
calc> mul()
1
calc> sub(10, 1, 2, 3)
4
calc> sub(3)
-3
calc> div(15, 12)
1.25
calc> sub(100, mul(7, add(8, div(-12, -3))))
16.0
calc> -(100, *(7, +(8, /(-12, -3))))
16.0
calc> add(2, 3)
5
calc> (+ 2 a)
SyntaxError: unexpected (
calc> mul(1, 2, 3)
6
calc> add()
0
calc> add(2, div(4, 8))
2.5
calc> add
SyntaxError: expected ( after add
calc> div(5)
TypeError: div requires exactly 2 arguments
calc> div(1, 0)
ZeroDivisionError: division by zero
calc> 
'''
