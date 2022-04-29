

from video_loader import video_loader

def test_video_loader_can_be_setup_for_unit_tests(mocker):
    mockVideoConverter = mocker.patch("src.video_loader._video_converter", side_effect=["/some/path",5])
    
    video_loader("/some/path")
    
    assert True