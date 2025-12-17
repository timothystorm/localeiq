import re
from typing import Optional

_LOCALE_SPLIT_RE = re.compile(r"[-_]")


def normalize_locale_tag(tag: Optional[str]) -> Optional[str]:
    """
    Normalizes locale tags.

    fr-ca -> fr-CA
    FR_ca -> fr-CA
    zh_hant_tw -> zh-Hant-TW
    es-419 -> es-419

    :param tag to normalize
    :return: normalized locale tag or None if tag is empty
    """
    if not tag:
        return None

    parts = _LOCALE_SPLIT_RE.split(tag.strip())
    if not parts:
        return None

    normalized: list[str] = []

    for i, part in enumerate(parts):
        if not part:
            continue

        # language (lowercase)
        if i == 0:
            normalized.append(part.lower())

        # script (4 letters, TitleCase)
        elif len(part) == 4 and part.isalpha():
            normalized.append(part.title())

        # region (2 letters or 3 digits, uppercase)
        elif (len(part) == 2 and part.isalpha()) or (len(part) == 3 and part.isdigit()):
            normalized.append(part.upper())

        # variants/extensions (leave as-is for now)
        else:
            normalized.append(part)

    return "-".join(normalized)
