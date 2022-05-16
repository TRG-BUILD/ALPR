

from controller import controller

def test_true():
    assert True

def test_controller_can_be_setup_for_integration_tests(mocker):
    mockVideoLoader = mocker.patch("src.controller.video_loader", return_value=True)
    mockUserInput = mocker.patch("src.controller.user_input", return_value=True)
    mockRecognizer = mocker.patch("src.controller.recognizer", return_value=True)
    mockFileFormatter = mocker.patch("src.controller.file_formatter", return_value=True)
    
    controller()
    
    assert True
    