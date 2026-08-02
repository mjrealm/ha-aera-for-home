from datetime import timedelta
import logging

DOMAIN = "aera"
LOGGER = logging.getLogger(__package__)

DEFAULT_POLL_INTERVAL = timedelta(seconds=60)
