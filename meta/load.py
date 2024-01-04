# PYTHON script
import meta
from meta import results
from meta import models


def model():
	window_name = 'MetaPost'
	filename = 'Z:/cae_jobs/rcwall/final/glass/d3plot'
	deck = 'DYNA'
	r = models.LoadModel(window_name, filename, deck)
	if r:
		print(r.id, r.name, r.label, r.deck, r.active)
                

def LoadAppendDeformations():
        model_id = 0
        filename = 'Z:/cae_jobs/rcwall/final/glass/d3plot'
        deck = 'DYNA'
        states = 'all'
        data_deform = 'Displacements'
        new_resultsets = results.LoadAppendDeformations(model_id, filename, deck, states, data_deform)
        for res in new_resultsets:
                print(res.cycle, res.model_id)


def LoadAppendScalar():
        model_id = 0
        filename = 'Z:/cae_jobs/rcwall/final/glass/d3plot'
        deck = 'DYNA'
        states = 'all'
        data_scalar = 'Strains,Strain Energy,Outer Surface'
        new_resultsets = results.LoadAppendScalar(model_id, filename, deck, states, data_scalar)
        for res in new_resultsets:
                print(res.cycle, res.model_id)


def LoadAppendVector():
        model_id = 0
        filename = 'Z:/cae_jobs/rcwall/final/glass/d3plot'
        deck = 'DYNA'
        states = 'all'
        data_vector = 'Stress components,Major Principal,Inner Surface'
        new_resultsets = results.LoadAppendVector(model_id, filename, deck, states, data_vector)
        for res in new_resultsets:
                print(res.cycle, res.model_id)

if __name__ == '__main__':
        main()