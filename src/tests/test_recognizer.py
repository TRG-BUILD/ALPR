

from recognizer import recognizer

def test_recognizer_can_be_setup_for_unit_tests(mocker):
    mockFindPlates = mocker.patch("src.recognizer.find_plates", return_value=[])
    
    recognizer("eu","alpr","/some/path",1)
    
    assert True