import meta
from meta import elements, constants, models, results, windows


# load scalar - strain energy
def main():
    m = models.Model(0)
    filename = m.name
    deck = 'DYNA'
    states = 'ALL'
    data_scalar = 'Strains,Strain Energy,Outer Surface'
    new_resultsets = results.LoadAppendScalar(m.id, filename, deck, states, data_scalar)
    
    elem = elements.Element(id=97124, type=constants.SHELL, second_id=-1, model_id=m.id)
    
    for res in new_resultsets:
        elem_res = elem.get_centroid_scalar(res)
        if elem_res:
        	print(elem_res.element_id, res.state, res.time, elem_res.value)


if __name__ == '__main__':
    main()