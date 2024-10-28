import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailer_code = None
        self._brand = None
        self._anno = None

    def riempi_ddAnno(self):
        anni = self._model.getAnni()
        self._view._ddAnno.options.append(ft.dropdown.Option(key = "None", text = "Nessun filtro"))
        for anno in anni:
            self._view._ddAnno.options.append(ft.dropdown.Option(anno[0]))
        self._view.update()

    def riempi_ddBrand(self):
        brands = self._model.getBrands()
        self._view._ddBrand.options.append(ft.dropdown.Option(key = "None", text="Nessun filtro"))
        for brand in brands:
            self._view._ddBrand.options.append(ft.dropdown.Option(brand[0]))
        self._view.update()

    def riempi_ddRetailer(self):
        self._view._ddRetailer.options.append(ft.dropdown.Option(key = "None", text="Nessun filtro", data =None, on_click= self.read_retailer))
        retailers = self._model.getRetailers()
        for retailer in retailers:
            self._view._ddRetailer.options.append(ft.dropdown.Option(key= retailer.retailer_code, text = retailer.retailer_name,
                                                                     data = retailer, on_click = self.read_retailer))
        self._view.update()

    def read_retailer(self, e):
        if e.control.data is None:
            self._retailer = None
        else:
            self._retailer_code = e.control.data.retailer_code

    def leggiddAnno(self, e):
        if self._view._ddAnno.value == "None":
            self._anno = None
        else:
            self._anno = self._view._ddAnno.value

    def leggiddBrand(self,e):
        if self._view._ddBrand.value == "None":
            self._brand = None
        else:
            self._brand = self._view._ddBrand.value

    def getTopVend(self, e):
        self._view._lvResult.controls.clear()
        listVend = self._model.getTopVendite(self._anno, self._brand, self._retailer_code)
        if len(listVend) == 0:
            self._view._lvResult.controls.append(ft.Text("Non ci sono vendite con questi filtri"))
        else:
            for vend in listVend:
                self._view._lvResult.controls.append(ft.Text(vend))
        self._view.update()


    def getAnalisi(self):
        pass
