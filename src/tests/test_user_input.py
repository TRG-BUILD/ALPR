

from user_input import user_input

def test_user_input_can_be_setup_for_unit_tests(mocker):
    mockGetCode = mocker.patch("src.user_input.get_code", return_value="eu")
    
    user_input()
    
    assert True