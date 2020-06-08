from app import service
from app.service import PHRASES


def test_get_random_phrase():
    phrase = service.get_random_phrase()
    assert isinstance(phrase, str)
    assert phrase in PHRASES
