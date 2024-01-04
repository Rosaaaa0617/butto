import meta
from meta import elements, constants, models, results, windows, utils


# load scalar - strain energy
def main():
    m = models.Model(0)
    filename = m.name
    deck = 'DYNA'
    states = 'ALL'
    data_scalar = ['Strains,Full Tensor(UCS),Outer Surface',
                   'Stresses,Full Tensor(UCS),Outer Surface',
                   'Strains,Strain Energy Density,Outer Surface']
    
    for scalar in data_scalar:
         new_resultsets = results.LoadAppendScalar(m.id, filename, deck, states, scalar)
    
    elem_id = 97124
        
    window_name = 'Window1'
    w = windows.Create2DPlotWindow(window_name)
    if w:
            print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)

    utils.MetaCommand(f'window active "{window_name}"')    

    all_labels = models.ScalarLabelsOfModel(m.id)
    for strain_label in all_labels:
            utils.MetaCommand(f'xyplot frommodel elements "{window_name}" 0 {elem_id} Centroid Time all all slabel "{strain_label}"')




if __name__ == '__main__':
    main()