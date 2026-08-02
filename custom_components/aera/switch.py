from typing import Any
from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .entity import AeraEntity

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the switch platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    entities = []
    for device_key in coordinator.data:
        entities.append(AeraSwitch(coordinator, device_key))
        
    async_add_entities(entities)

class AeraSwitch(AeraEntity, SwitchEntity):
    """Representation of an Aera power switch."""

    def __init__(self, coordinator, device_key):
        """Initialize."""
        super().__init__(coordinator, device_key)
        self._attr_unique_id = f"{device_key}_power"
        self._attr_name = "Power"
        self._attr_has_entity_name = True

    @property
    def is_on(self) -> bool:
        """Return true if the device is on."""
        return self.device.is_power_on

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the device on."""
        await self.coordinator.api.set_power(self.device, True)
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the device off."""
        await self.coordinator.api.set_power(self.device, False)
        await self.coordinator.async_request_refresh()
