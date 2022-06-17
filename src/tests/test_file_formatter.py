

from file_formater import file_formater

def test_file_formater_can_mock_functions_that_use_external_dependencies(mocker):
    mockWriteToCSV = mocker.patch("file_formater.write_to_csv", return_value=True)
    results_list = []
    sort_by = "tid"
    minimum_confidence = 99
    
    result = file_formater("/some/file/path", ".some_format", "some;seperator", minimum_confidence, sort_by, results_list)
    
    assert result == True