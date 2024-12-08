import aiohttp

from src.config.logging_config import logger
from src.custom_types import MetadataResponse, SurahReference

METADATA_URL = "https://api.alquran.cloud/v1/meta"

async def load_metadata() -> list[SurahReference]:
    async with aiohttp.ClientSession() as session:
        async with session.get(METADATA_URL) as response:
            metadata: MetadataResponse = await response.json()
            logger.info("Metadata loaded.")
            return metadata["data"]["surahs"]["references"]  # Adjust key path based on actual API response
