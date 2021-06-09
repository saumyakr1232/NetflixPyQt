from pages.LoginPageUi import  Ui_LoginPage
from pages.PageWindow import  PageWindow

class LoginPage(PageWindow):
    def __init__(self):
        super().__init__()
        ui = Ui_LoginPage()
        ui.setupUi(self)
        self.setWindowTitle("Login Netflix")
        self.ui = ui
        self.UiComponents()


    def UiComponents(self):

        self.ui.BackButtton.clicked.connect(
            self.make_handleButton("backButton")
        )
        self.ui.SettingButton.clicked.connect(
            self.make_handleButton("searchButton")
        )

        self.ui.LoginButton.clicked.connect(
            self.make_handleButton("searchButton")
        )

    def make_handleButton(self, button):
        def handleButton():
            if button == "searchButton":
                self.goto("search")
            if button == "backButton":
                self.goto("main")
        return handleButton