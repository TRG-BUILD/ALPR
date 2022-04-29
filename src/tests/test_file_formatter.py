

from file_formater import file_formater

def test_file_formater_can_be_setup_for_unit_tests(mocker):
    mockOpen = mocker.patch("src.file_formater.open", return_value=True)
    results_list = []
    
    file_formater("/some/file/path", ".some_format", "some;seperator", results_list)
    
    assert True