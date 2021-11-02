import mymodule

import mock
import pytest

@mock.patch('mymodule.os.path')
@mock.patch('mymodule.os')
def test_rm(mock_os, mock_path):
    reference = mymodule.RemovalService()

    mock_path.isfile.return_value = False
    reference.rm('any path')

    assert mock_os.remove.called == 0, 'Failed to not remove the file if not present.'

    mock_path.isfile.return_value = True
    reference.rm('any path')

    mock_os.remove.assert_called_with('any path')

def test_upload_complete():
    mock_removal_service = mock.create_autospec(mymodule.RemovalService)
    reference = mymodule.UploadService(mock_removal_service)
    
    reference.upload_complete("my uploaded file")
   
    mock_removal_service.rm.assert_called_with("my uploaded file")