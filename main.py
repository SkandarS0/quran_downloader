import asyncio

from colorama import Fore, Style, init

from src.config.logging_config import setup_logging, logger
from src.custom_types import SurahReference
from src.downloader.quran_downloader import start_downloading
from src.utils.metadata_utils import load_metadata

METADATA_URL = "https://api.alquran.cloud/v1/meta"

# Initialize colorama
init(autoreset=True)

# Configure logging to a file
setup_logging()

surahs_references: list[SurahReference] = []

async def input_menu() -> None:
    selected_surahs = []
    while True:
        print(f"\n{Fore.CYAN}Welcome to the Quran Downloader{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please select an option:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1. Choose the surah/surahs you want to download:{Style.RESET_ALL}")
        if len(selected_surahs) != 0:
            print(f"{Fore.GREEN}2. Start downloading.{Style.RESET_ALL}")
        print(f"{Fore.RED}0. Exit{Style.RESET_ALL}")

        choice = input(f"{Fore.BLUE}Enter your choice: {Style.RESET_ALL}")

        if choice == "1":
            logger.info("Option 1 selected (choose surahs)")
            display_surahs()
            selected_surahs = select_surahs()

        elif choice == "2" and len(selected_surahs) != 0:
            logger.info("Option 2 selected (start downloading)")
            await start_downloading(selected_surahs)

        elif choice == "0":
            logger.info("Exiting menu")
            print(f"{Fore.MAGENTA}Thank you for using the menu. Goodbye!{Style.RESET_ALL}")
            break
        else:
            logger.warning("Invalid option selected")
            print(f"{Fore.RED}Invalid option, please try again.{Style.RESET_ALL}")


def display_surahs() -> None:
    for surah_reference in surahs_references:
        print(
            f"{Fore.GREEN}{surah_reference["number"]}. {surah_reference['englishName']} ({surah_reference['name']}){Style.RESET_ALL}")


def select_surahs() -> list[SurahReference]:
    selection = input("Enter the Surah numbers you want to download (e.g., '1', '1-5', '1 6-20'): ")
    selected_surahs = []

    # Split the input by spaces and commas
    tokens = selection.replace(',', ' ').split()

    for token in tokens:
        if '-' in token:
            # Handle range input
            start, end = map(int, token.split('-'))
            if 1 <= start <= 114 and 1 <= end <= 114:
                selected_surahs.extend(surahs_references[start - 1:end])
            else:
                print(f"Range {start}-{end} is out of bounds. Please enter a valid range (1-114).")
        else:
            # Handle single number input
            try:
                index = int(token.strip()) - 1
                if 0 <= index < 114:
                    selected_surahs.append(surahs_references[index])
                else:
                    print(f"Number {index + 1} is out of bounds. Please enter a valid number (1-114).")
            except ValueError:
                print(f"Invalid input {token}. Please enter numbers or ranges like '1-10'.")

    logger.info(f"Selected Surahs: {[surah['englishName'] for surah in selected_surahs]}")
    return selected_surahs


async def main() -> None:
    global surahs_references

    surahs_references = await load_metadata()

    await input_menu()

    logger.info("Program completed")


# Run the main async function
if __name__ == "__main__":
    asyncio.run(main())
