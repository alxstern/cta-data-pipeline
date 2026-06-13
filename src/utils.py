import logging
import os

from dotenv import load_dotenv

load_dotenv()


def setup_logging() -> None:
    """Configure logging format and level for the pipeline."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s — %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )


def get_cta_tt_api_key() -> str:
    """Retrieve the CTA Train Tracker API key from environment variables."""
    api_key = os.getenv("CTA_TRAIN_TRACKER_API_KEY")

    if not api_key:
        raise ValueError("CTA_TRAIN_TRACKER_API_KEY not found in environment variables.")

    return api_key