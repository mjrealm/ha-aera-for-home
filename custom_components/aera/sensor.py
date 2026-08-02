from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.const import PERCENTAGE

from .const import DOMAIN
from .entity import AeraEntity

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    entities = []
    for device_key in coordinator.data:
        entities.append(AeraFragranceNameSensor(coordinator, device_key))
        entities.append(AeraFragranceRemainingSensor(coordinator, device_key))
        
    async_add_entities(entities)

class AeraFragranceNameSensor(AeraEntity, SensorEntity):
    """Representation of an Aera fragrance name sensor."""

    def __init__(self, coordinator, device_key):
        """Initialize."""
        super().__init__(coordinator, device_key)
        self._attr_unique_id = f"{device_key}_fragrance_name"
        self._attr_name = "Current Fragrance"
        self._attr_has_entity_name = True

    @property
    def native_value(self) -> str | None:
        """Return the native value of the sensor."""
        return self.device.fragrance_name

class AeraFragranceRemainingSensor(AeraEntity, SensorEntity):
    """Representation of an Aera fragrance remaining sensor."""

    def __init__(self, coordinator, device_key):
        """Initialize."""
        super().__init__(coordinator, device_key)
        self._attr_unique_id = f"{device_key}_fragrance_remaining"
        self._attr_name = "Fragrance Remaining"
        self._attr_has_entity_name = True
        self._attr_native_unit_of_measurement = PERCENTAGE
        self._attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def native_value(self) -> int | None:
        """Return the native value of the sensor."""
        return self.device.fragrance_remaining
