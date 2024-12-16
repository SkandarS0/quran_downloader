from typing import TypedDict


class DataAyahsCount(TypedDict):
    count: int


class SurahReference(TypedDict):
    number: int
    name: str
    englishName: str
    englishNameTranslation: str
    numberOfAyahs: int
    revelationType: str


class DataSurahs(TypedDict):
    count: int
    references: list[SurahReference]


class MetadataResponseData(TypedDict):
    ayahs: DataAyahsCount
    surahs: DataSurahs


class MetadataResponse(TypedDict):
    code: int
    status: str
    data: MetadataResponseData
