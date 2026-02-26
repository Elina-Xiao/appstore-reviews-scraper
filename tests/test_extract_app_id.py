from commentsE import extract_app_id

def test_extract_app_id_from_url():
    assert extract_app_id("https://apps.apple.com/us/app/meitu-ai-photo-video-editor/id416048305") == "416048305"

def test_extract_app_id_from_digits():
    assert extract_app_id("389801252") == "389801252"
