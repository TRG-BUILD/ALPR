

from user_input import user_input

def test_user_input_can_mock_functions_that_use_external_dependencie(mocker):
    mockGetMIModel = mocker.patch("user_input.get_mi_model", return_value="alpr")
    mockGetCode = mocker.patch("user_input.get_code", return_value="someCode")
    mockGetMinConfidence = mocker.patch("user_input.get_min_confidence", return_value=101)
    mockGetFileFormat = mocker.patch("user_input.get_file_format", return_value="someFormat")
    mockGetSeperator = mocker.patch("user_input.get_seperator", return_value="someSeperator")
    mockGetSortBy = mocker.patch("user_input.get_sorting", return_value="somethingToSortBy")
    
    resultCode, resultMI,resultFormat,resultSep,resultConf,resultSort = user_input()
    
    assert resultMI == "alpr"
    assert resultCode == "someCode"
    assert resultConf == 101
    assert resultFormat == "someFormat"
    assert resultSep == "someSeperator"
    assert resultSort == "somethingToSortBy"