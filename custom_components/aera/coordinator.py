from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from aera import AeraApi
from .const import DOMAIN, DEFAULT_POLL_INTERVAL

_LOGGER = logging.getLogger(__name__)

class AeraDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Aera data."""

    def __init__(self, hass: HomeAssistant, api: AeraApi) -> None:
        """Initialize."""
        self.api = api
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=DEFAULT_POLL_INTERVAL,
        )

    async def _async_update_data(self):
        """Update data via library."""
        try:
            devices = await self.api.get_devices()
            device_data = {}
            for device in devices:
                await self.api.get_device_properties(device)
                device_data[device.device_key] = device
            return device_data
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}") from err
