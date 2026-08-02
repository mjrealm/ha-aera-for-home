from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.device_registry import DeviceInfo
from .const import DOMAIN

class AeraEntity(CoordinatorEntity):
    """Base class for Aera entities."""

    def __init__(self, coordinator, device_key):
        """Initialize."""
        super().__init__(coordinator)
        self.device_key = device_key

    @property
    def device(self):
        """Return the device."""
        return self.coordinator.data[self.device_key]

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.device.device_key)},
            name=self.device.device_name,
            manufacturer="Aera for Home",
            model=self.device.device_type,
            sw_version=self.device.firmware_version,
        )
