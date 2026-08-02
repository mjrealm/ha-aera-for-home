from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from aera import AeraApi
from .const import DOMAIN, LOGGER
from .coordinator import AeraDataUpdateCoordinator

PLATFORMS: list[Platform] = [Platform.SWITCH, Platform.NUMBER, Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Aera for Home from a config entry."""
    email = entry.data[CONF_EMAIL]
    password = entry.data[CONF_PASSWORD]

    api = AeraApi(email, password)
    
    try:
        await api.login()
    except Exception as ex:
        LOGGER.error(f"Failed to login to Aera API: {ex}")
        raise ConfigEntryNotReady from ex

    coordinator = AeraDataUpdateCoordinator(hass, api)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        coordinator = hass.data[DOMAIN].pop(entry.entry_id)
        await coordinator.api.close()

    return unload_ok
