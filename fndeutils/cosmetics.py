from typing import NamedTuple

import fortnite_api
from redbot.core.i18n import Translator

_t = Translator("FndeUtils", __file__)

__all__ = [
    "Cosmetic",
    "CosmeticData",
    "get_cosmetic_data",
]

Cosmetic = (
    fortnite_api.CosmeticBr
    | fortnite_api.CosmeticCar
    | fortnite_api.CosmeticLegoKit
    | fortnite_api.CosmeticInstrument
    | fortnite_api.CosmeticTrack
)


class CosmeticData(NamedTuple):
    name: str
    image_url: str
    display_type: str


def get_cosmetic_data(cosmetic: Cosmetic) -> CosmeticData:
    if isinstance(cosmetic, fortnite_api.CosmeticTrack):
        name = cosmetic.title
        image_url = cosmetic.album_art.url
        display_type = _t("Jam Track")
    else:
        name = cosmetic.name
        image = cosmetic.images and (
            cosmetic.images.featured
            or cosmetic.images.icon
            or cosmetic.images.small_icon
            or cosmetic.images.large
            or cosmetic.images.small
        )
        image_url = image.url if image else ""
        display_type = cosmetic.type.display_value if cosmetic.type else "???"
    return CosmeticData(name, image_url, display_type)
