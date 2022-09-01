from typing import List, Optional

from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.profiles import Profile
from app.models.domain.rwmodel import RWModel

from pydantic import validator

class Item(IDModelMixin, DateTimeModelMixin, RWModel):
    slug: str
    title: str
    description: str
    tags: List[str]
    seller: Profile
    favorited: bool
    favorites_count: int
    image: Optional[str]
    body: Optional[str]

    @validator("image")
    def validate_image(cls, image):
        return image or "http://localhost:3001/placeholder.png"
