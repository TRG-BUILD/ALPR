

from video_loader import video_loader

def test_video_loader_can_mock_functions_that_use_external_dependencies(mocker):
    mockGetVideos = mocker.patch("video_loader.get_list_of_files_from_dir", return_value=[])
    mockVideoConverter = mocker.patch("video_loader._video_converter", side_effect=["/some/path",5])
    
    video_loader("/some/path")
    
    assert True