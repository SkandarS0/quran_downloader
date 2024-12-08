import logging


def setup_logging(log_file: str = "application.log") -> None:
    """Set up logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, mode="w"),
        ]
    )


logger = logging.getLogger(__name__)
