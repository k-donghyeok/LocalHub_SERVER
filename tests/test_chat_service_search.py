from app.services.chat_service import filter_places_by_keywords


class DummyPlace:
    def __init__(self, title, addr1):
        self.title = title
        self.addr1 = addr1


def test_filter_places_by_keywords_matches_space_split_terms():
    places = [
        DummyPlace("해운대 해변", "부산 해운대구"),
        DummyPlace("광안리 해변", "부산 수영구"),
        DummyPlace("마린시티", "부산 해운대구"),
    ]

    result = filter_places_by_keywords(places, "해운대 부산")

    assert [place.title for place in result] == ["해운대 해변", "마린시티"]
