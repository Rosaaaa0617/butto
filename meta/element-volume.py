import meta
from meta import elements
from meta import constants
from meta import models

def main():
	model = models.Model(0)
	elem = elements.Element(id=100, type=constants.SOLID, second_id=-1, model_id=model.id)
	res = model.get_current_resultset()
	val = elem.get_volume(res)
	print(val)

if __name__ == '__main__':
	main()