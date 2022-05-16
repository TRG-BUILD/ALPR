

from user_input import user_input

def test_user_input_can_be_setup_for_unit_tests_using_mocks(mocker):
    mockGetMIModel = mocker.patch("user_input.get_mi_model", return_value="alpr")
    mockGetCode = mocker.patch("user_input.get_code", return_value="someCode")
    mockGetMinConfidence = mocker.patch("user_input.get_min_confidence", return_value=101)
    mockGetFileFormat = mocker.patch("user_input.get_file_format", return_value="someFormat")
    mockGetSeperator = mocker.patch("user_input.get_seperator", return_value="someSeperator")
    mockGetSortBy = mocker.patch("user_input.get_sorting", return_value="somethingToSortBy")
    
    user_input()
    
    assert True