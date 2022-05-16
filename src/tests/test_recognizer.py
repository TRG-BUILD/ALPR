

from recognizer import recognizer

def test_recognizer_can_mock_functions_that_use_external_dependencies(mocker):
    mockFindPlates = mocker.patch("recognizer.find_plates", return_value=[])
    
    recognizer("eu","alpr","/some/path",1)
    
    assert True