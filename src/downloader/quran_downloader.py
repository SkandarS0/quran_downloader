import asyncio
import pathlib

import aiohttp
from colorama import Fore, Style

from src.config.logging_config import logger
from src.custom_types import SurahReference
from src.utils.chunk_utils import chunks

SURAH_AUDIO_URL = "https://cdn.islamic.network/quran/audio-surah/128/ar.aliabdurrahmanalhuthaifyqaloon/{number}.mp3"

async def download_surah(session: aiohttp.ClientSession, surah: SurahReference) -> None:
    audio_url = SURAH_AUDIO_URL.format(number=surah["number"])
    try:
        async with session.get(audio_url) as response:
            file_path = f"data/quran/{surah['englishName']}.mp3"
            if response.status == 200:
                with open(file_path, "wb") as file:
                    file.write(await response.read())
                logger.info(f"Downloaded {file_path}")
            else:
                logger.error(f"Failed to download {file_path} - HTTP {response.status}")
    except Exception as e:
        logger.error(f"An error occurred for {surah['englishName']}: {e}")


async def start_downloading(selected_surahs: list[SurahReference]) -> None:
    pathlib.Path('data/quran').mkdir(exist_ok=True, parents=True)
    async with aiohttp.ClientSession() as session:
        for chunk in chunks(selected_surahs, 5):
            download_tasks = [
                download_surah(session, surah)
                for surah in chunk
                if not pathlib.Path(f"data/quran/{surah['englishName']}.mp3").exists()
            ]
            if download_tasks:
                logger.info("Starting a new batch of downloads")
                await asyncio.gather(*download_tasks)

    print(f"{Fore.GREEN}All files have been downloaded successfully.{Style.RESET_ALL}")
    logger.info("All files have been downloaded successfully.")