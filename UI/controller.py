import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def riempi_ddAnno(self):
        anni = self._model.getAnni()
        self._view._ddAnno.options.append(ft.dropdown.Option(text = "Nessun filtro"))
        for anno in anni:
            self._view._ddAnno.options.append(ft.dropdown.Option(anno[0]))
        self._view.update()

    def riempi_ddBrand(self):
        pass

    def riempi_ddRetailer(self):
        pass
