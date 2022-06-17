from unittest.mock import ANY

from controller import controller

def test_controller_can_mock_functions_that_use_external_dependencies_with_a_valid_video(mocker, first_video_info):
    video_list = [first_video_info]
    mockVideoLoader = mocker.patch("controller.video_loader", return_value=video_list)
    mockUserInput = mocker.patch("controller.user_input", return_value=[
        "SomeCode","SomeMIModel","SomeFormat","SomSeperator",10,"SomethingToSortBy"])
    mockRecognizer = mocker.patch("controller.recognizer", return_value=True)
    mockFileFormatter = mocker.patch("controller.file_formater", return_value=True)

    result = controller()
    
    assert result == True
    
def test_controller_should_terminate_with_error_if_no_videos_are_available(mocker):
    video_list = []
    mockVideoLoader = mocker.patch("controller.video_loader", return_value=video_list)
    mockUserInput = mocker.patch("controller.user_input", return_value=[
        "SomeCode","SomeMIModel","SomeFormat","SomSeperator",10,"SomethingToSortBy"])
    mockRecognizer = mocker.patch("controller.recognizer", return_value=True)
    mockFileFormatter = mocker.patch("controller.file_formater", return_value=True)
    
    result = controller()
    
    mockVideoLoader.assert_called_once_with(ANY)
    mockUserInput.assert_not_called()
    mockRecognizer.assert_not_called()
    mockFileFormatter.assert_not_called()
    assert result == False