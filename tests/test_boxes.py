from livedepython.app import SuccessBox, LoginBox
from pytest import mark


def test_success_box_should_return_hello_username():
    box = SuccessBox('Eduardo')
    assert box.label.text == 'Hello Eduardo'


def test_success_box_should_have_label_inside_box():
    box = SuccessBox('Eduardo')
    assert box.box.children[0].text == 'Hello Eduardo'


@mark.parametrize(
    'element',
    [
        'username_label',
        'username_input',
        'password_label',
        'password_input',
        'error_output',
        'login_input',
    ],
)
def test_login_box_should_have_elements(element):
    box = LoginBox()
    assert hasattr(box, element)


def test_login_action_should_return_login_error():
    box = LoginBox()
    box.login_input.on_press('')
    assert box.error_output.value == 'Login error'
