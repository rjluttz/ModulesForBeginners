from ..student import register as rg
from ..teacher import employ as em
from .application import apply_details
import logging
logger = logging.getLogger(__name__)


def update_registry(details, code):
    if code == "STUDENT":
        apply_details(rg, details, code)
    else:
        apply_details(em, details, code)
    logger.debug(f"Successfully updated registry")
