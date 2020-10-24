import toga
from toga.style.pack import COLUMN, Pack


class SuccessBox:
    def __init__(self, email):
        self.box = toga.Box()
        self.label = toga.Label(f'Hello {email}', style=Pack(font_size=25))
        self.box.add(self.label)


class LoginBox:
    def __init__(self, window=None):
        self.window = window
        self.box = toga.Box()

        self.username_label = toga.Label(
            'Username', style=Pack(padding=10, padding_top=50, font_size=20)
        )
        self.username_input = toga.TextInput(
            placeholder='your_username',
            style=Pack(padding_left=10, padding_right=10),
        )
        self.password_label = toga.Label(
            'Password', style=Pack(padding=10, padding_top=50, font_size=20)
        )

        self.password_input = toga.PasswordInput(
            placeholder='your_password',
            style=Pack(padding_left=10, padding_right=10),
        )
        self.password_input.style.update(padding=10)
        self.error_output = toga.TextInput(readonly=True)

        self.login_input = toga.Button('Login', on_press=self.login_handler)
        self.login_input.style.update(padding=35)
        self.box.style.update(direction=COLUMN)
        self.box.add(
            self.username_label,
            self.username_input,
            self.password_label,
            self.password_input,
            self.login_input,
            self.error_output,
        )

    def login_handler(self, widget):
        val1 = self.username_input.value == 'test'
        val2 = self.password_input.value == '1234'

        if all([val1, val2]):
            self.window.content = SuccessBox(self.username_input.value).box

        self.error_output.value = 'Login error'
        self.username_input.clear()
        self.password_input.clear()


class LivedePython(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = LoginBox(self.main_window).box
        self.main_window.show()


def main():
    return LivedePython()
