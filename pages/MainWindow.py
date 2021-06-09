from pages.PageWindow import  PageWindow
from pages.LandingPage import  Ui_LandingPage

class LandingPage(PageWindow):
    def __init__(self):
        super().__init__()
        ui = Ui_LandingPage()
        ui.setupUi(self)
        self.setWindowTitle("Netflix")
        self.ui = ui
        self.UiComponents()


    def UiComponents(self):

        self.ui.SignInButton.clicked.connect(
            self.make_handleButton("searchButton")
        )

    def make_handleButton(self, button):
        def handleButton():
            if button == "searchButton":
                self.goto("search")
        return handleButton