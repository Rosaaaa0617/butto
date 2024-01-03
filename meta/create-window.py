import meta
from meta import elements, constants, models, results, windows

# create 2dplot window
def createwindow():
	window_name = 'Window1'
	w = windows.Create2DPlotWindow(window_name)
	if w:
		print(w.name, w.page_id, w.active, w.height, w.width, w.plot2d, w.enabled)

if __name__ == '__main__':
	main()