# PYTHON script
# use python code and ses code load scalar and polt strains/stresses-time curves
import meta
from meta import elements, constants, models, results, windows, utils, plot2d


def main():
        m = models.Model(0)
        filename = m.name
        deck = 'DYNA'
        states = 'all'
        data_scalar = ['Strains,Strain Energy,Outer Surface',
                       'Strains,Strain Energy Density,Outer Surface'
                       ]
        for scalar in data_scalar:
                new_resultsets = results.LoadAppendScalar(m.id, filename, deck, states, scalar)

        elem_id = 97124
        
        window_name = 'Window2'
        w = windows.Create2DPlotWindow(window_name)
        if w:
               print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)

        utils.MetaCommand(f'window active "{window_name}"')    

        all_labels = models.ScalarLabelsOfModel(m.id)
        for strain_label in all_labels:
                utils.MetaCommand(f'xyplot frommodel elements "{window_name}" 0 {elem_id} Centroid Time all all slabel "{strain_label}"')

def area():
	model = models.Model(0)
	elem = elements.Element(id=100, type=constants.SOLID, second_id=-1, model_id=model.id)
	res = model.get_current_resultset()
	val = elem.get_volume(res)
	print(val)
      
def calculate():
    type = 'plain'
    name_type = 'energy / energy density'
    x_formula = 'c13.x'
    y_formula = 'c14.y/c13.y'       
    complex_formula = ''
    window = 'Window2'
    ret = plot2d.CurveFunctionUserDefined(type, name_type, x_formula, y_formula, complex_formula, window)
    print(ret)


    
main()
calculate()