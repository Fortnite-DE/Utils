from typing import NamedTuple

import fortnite_api
from redbot.core.i18n import Translator

_ = Translator("FndeUtils", __file__)

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
    type: fortnite_api.CosmeticType
    display_type: str
    is_shop: bool = False


def get_cosmetic_data(cosmetic: Cosmetic) -> CosmeticData:
    if isinstance(cosmetic, fortnite_api.CosmeticTrack):
        name = cosmetic.title
        image_url = cosmetic.album_art.url
        type_ = fortnite_api.CosmeticType.JAM_TRACK
        display_type = _("Jam Track")
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
        assert cosmetic.type is not None
        type_ = cosmetic.type.value
        display_type = cosmetic.type.display_value if cosmetic.type else "???"
    is_shop = not (
        isinstance(cosmetic, (fortnite_api.CosmeticBr, fortnite_api.CosmeticCar))
        and "Cosmetics.Source.ItemShop" not in cosmetic.gameplay_tags
    )

    return CosmeticData(name, image_url, type_, display_type, is_shop)
