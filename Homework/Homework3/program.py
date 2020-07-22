from sympy import *

#parse the following int or return 1 if there's nothing
def parse_int(s): 
    i = 0
    while i < len(s) and s[i].isdigit(): i += 1
    return 1 if i == 0 else int(s[:i])

def balance_equation(inp):
    l_r = inp.partition(' = ')
    l_terms = l_r[0].count('+') + 1
    terms = l_r[0].split(' + ') + l_r[2].split(' + ')

    #rows are equations for each element, columns come from terms and represent unknowns
    columns = []
    elements = []
    for term_number, term in enumerate(terms):
        column = [0] * len(elements)
        #terms on the right side are subtracted to get a homogeneous system of equations
        factor = 1 if term_number < l_terms else -1
        for i, c in enumerate(term):
            if c == '.':
                #assume that no term has more than one dot
                factor *= parse_int(term[i + 1:])
            elif c in '([':
                #get the int after the matching paren
                j = i + 1
                parens = 1
                while parens != 0:
                    if term[j] in '([': parens += 1
                    elif term[j] in ')]': parens -= 1
                    j += 1
                factor *= parse_int(term[j:])
            elif c in ')]':
                factor = int(factor / parse_int(term[i + 1:]))
            elif c.isupper():
                #add the quantity of the element to this term's column
                j = i + 1
                while j < len(term) and term[j].islower(): j += 1
                if term[i:j] not in elements:
                    elements.append(term[i:j])
                    column.append(0)
                column[elements.index(term[i:j])] += parse_int(term[j:]) * factor
        columns.append(column)

    for col in columns:
        col += [0] * (len(elements) - len(col))

    print(columns)
    mat = Matrix(columns).T
    #let the library do all the math
    #print(mat)
    nspace = mat.nullspace()
    #print(nspace)
    
    
    if len(nspace) == 0:
        return 'Nope!\n'
    else:
        #somehow get a usable list out of this, simplify using gcd, and convert to string
        divisor = 1
        for x in nspace[0].T.tolist()[0]: divisor = gcd(divisor, x)
        coefs = list(map(lambda x: str(x / divisor), nspace[0].T.tolist()[0]))
        
        #don't include '1's
        coefs = list(map(lambda x: '' if x == '1' else x, coefs))
        
        #format the output
        out = ' + '.join(map(lambda t: ''.join(t), zip(coefs, terms)))
        #put the '->' sign back in in kind of a silly way
        return out.replace('+', '->', l_terms).replace('->', '+', l_terms - 1)

infile = open('homework3SampeInput.txt', 'r')
outfile = open('balanced.txt', 'w')
inp = infile.readline()
while inp != '':
    outfile.write(balance_equation(inp))
    inp = infile.readline()

infile.close()
outfile.close()