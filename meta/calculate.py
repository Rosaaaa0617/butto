# energy density* element area
import meta
from meta import elements, constants, models, results, windows, utils, plot2d


def main():
    type = 'plain'
    name_type = 'strain energy density'
    x_formula = 'c1.x'
    y_formula = ''
    for i in range(1, 7):
        y_formula += f'c{i}.y * c{i+6}.y'
        if i != 6:
            y_formula += ' + '
    y_formula = f'0.5*{y_formula}'        
    complex_formula = ''
    window = 'Window1'
    ret = plot2d.CurveFunctionUserDefined(type, name_type, x_formula, y_formula, complex_formula, window)
    print(ret)

def r():
    type = 'plain'
    name_type = 'relation'
    x_formula = 'c1.x'
    y_formula = 'c14.y/c13.y'  
    complex_formula = ''
    window = 'Window1'
    ret = plot2d.CurveFunctionUserDefined(type, name_type, x_formula, y_formula, complex_formula, window)
    print(ret)
    
r()
