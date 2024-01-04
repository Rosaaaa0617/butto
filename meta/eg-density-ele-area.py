# energy density* element area
import meta
from meta import elements, constants, models, results, windows, utils, plot2d

# get elements volume & area
def main():
    model = models.Model(0)
    elem = elements.Element(id=97124, type=constants.SHELL, second_id=-1, model_id=model.id)
    res = model.get_current_resultset()
    vol = elem.get_volume(res)
    area = elem.get_area(res)
    print(vol)
    print(area)
    calculate(area)


def calculate(val):
    type = 'plain'
    name_type = 'energy density ratio'
    x_formula = 'c13.x'
    y_formula = f'c14.y * {val}'  # f-string 格式化
    complex_formula = ''
    window = 'Window2'
    ret = plot2d.CurveFunctionUserDefined(type, name_type, x_formula, y_formula, complex_formula, window)
    print(ret)

main()
