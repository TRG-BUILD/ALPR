

from controller import controller

def test_controller_can_mock_functions_that_use_external_dependencies(mocker):
    video_list = []
    mockVideoLoader = mocker.patch("controller.video_loader", return_value=video_list)
    mockUserInput = mocker.patch("controller.user_input", return_value=True)
    mockRecognizer = mocker.patch("controller.recognizer", return_value=True)
    mockFileFormatter = mocker.patch("controller.file_formater", return_value=True)
    
    controller()
    
    assert True
    