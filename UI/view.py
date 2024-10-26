import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._ddAnno = None
        self._ddBrand = None
        self._ddRetailer = None
        self._btnTop = None
        self._btnAnalisi = None
        self._lvResult = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        #ROW 1
        self._ddAnno = ft.Dropdown(
            label="anno",
            width= 300,
            hint_text = "selezionare filtro anno"
        )

        self._ddBrand = ft.Dropdown(
            label = "brand",
            width= 300,
            hint_text = "selezionare filtro brand"
        )

        self._ddRetailer = ft.Dropdown(
            label = "retailer",
            width = 500,
            hint_text = "selezionare filtro retailer"
        )

        row1 = ft.Row([self._ddAnno, self._ddBrand, self._ddRetailer], alignment= ft.MainAxisAlignment.CENTER)

        self._controller.riempi_ddAnno()
        self._controller.riempi_ddBrand()
        self._controller.riempi_ddRetailer()
        #ROW 2
        self._btnTop = ft.ElevatedButton(text="Top vendite")

        self._btnAnalisi = ft.ElevatedButton(text = "Analizza vendite")

        row2 = ft.Row([self._btnTop, self._btnAnalisi], alignment= ft.MainAxisAlignment.CENTER)

        #RESULT
        self._lvResult = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self._page.add(row1, row2, self._lvResult)

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update(self):
        self._page.update()
