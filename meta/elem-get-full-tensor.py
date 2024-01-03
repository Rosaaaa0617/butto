# choose one element and get 6 Stresses and Strains results of all states
import meta
from meta import elements, constants, models, results, windows

# load scalar - strains
def process_data(m, filename, deck, states, data_scalar, elem_id):
    if data_scalar not in ['Strains,Full Tensor(UCS),Outer Surface', 'Stresses,Full Tensor(UCS),Outer Surface']:
        new_resultsets = results.LoadAppendScalar(m.id, filename, deck, states, data_scalar)
        elem = elements.Element(id=elem_id, type=constants.SHELL, second_id=-1, model_id=m.id)
        
        for res in new_resultsets:
            elem_res = elem.get_centroid_scalar(res)
            if elem_res:
                print(elem_res.element_id, res.state, res.time, data_scalar, elem_res.value)

def main(elem_id):
    m = models.Model(0)
    filename = m.name
    deck = 'DYNA'
    states = 'ALL'

    all_scalars = ['Strains,Full Tensor(UCS),Outer Surface',
                   'Stresses,Full Tensor(UCS),Outer Surface'
                  ]
    for scalar in all_scalars:
        process_data(m, filename, deck, states, scalar, elem_id)

    all_labels = models.ScalarLabelsOfModel(m.id)
    for data_scalar in all_labels:
        process_data(m, filename, deck, states, data_scalar, elem_id)

if __name__ == '__main__':
    # Example: pass ID as an argument to main function
    element_id = 97124
    main(element_id)
