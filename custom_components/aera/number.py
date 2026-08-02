from homeassistant.components.number import NumberEntity
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
    """Set up the number platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    entities = []
    for device_key in coordinator.data:
        entities.append(AeraIntensity(coordinator, device_key))
        
    async_add_entities(entities)

class AeraIntensity(AeraEntity, NumberEntity):
    """Representation of an Aera intensity control."""

    def __init__(self, coordinator, device_key):
        """Initialize."""
        super().__init__(coordinator, device_key)
        self._attr_unique_id = f"{device_key}_intensity"
        self._attr_name = "Intensity"
        self._attr_has_entity_name = True
        self._attr_native_min_value = 1
        self._attr_native_step = 1

    @property
    def native_max_value(self) -> float:
        """Return the maximum value."""
        return float(self.device.max_intensity)

    @property
    def native_value(self) -> float:
        """Return the current value."""
        return float(self.device.intensity)

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        await self.coordinator.api.set_intensity(self.device, int(value))
        await self.coordinator.async_request_refresh()
