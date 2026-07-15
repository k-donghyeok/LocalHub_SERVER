from sqlalchemy import case, or_
from sqlalchemy.orm import Session

from app.models.place import Place


def search_places(db: Session, keyword: str, limit: int = 20) -> list[dict]:
    normalized_keyword = (keyword or "").strip()
    if not normalized_keyword:
        return []

    tokens = [token for token in normalized_keyword.split() if token]
    if not tokens:
        return []

    query = db.query(Place)
    for token in tokens:
        token_filter = f"%{token}%"
        query = query.filter(
            or_(
                Place.title.ilike(token_filter),
                Place.addr1.ilike(token_filter),
            )
        )

    places = query.order_by(
        case(
            (Place.title == normalized_keyword, 0),
            else_=1,
        ),
        Place.title.asc(),
    ).limit(limit).all()
    return [
        {
            "id": place.id,
            "content_id": place.content_id,
            "title": place.title,
            "address": " ".join(part for part in (place.addr1, place.addr2) if part),
        }
        for place in places
    ]
