# Aera Home Assistant Integration

![Aera for Home Logo](images/aera_logo.png)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=mjrealm&repository=ha-aera-for-home&category=integration) [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=aera)

Custom integration for Home Assistant to control and monitor Aera for Home smart diffusers.

## Features
- Turn diffusers on and off.
- Monitor remaining fragrance percentage.
- View current fragrance name.
- Control scent intensity.

## Installation

### HACS (Recommended)
1. Open **HACS** in your Home Assistant instance.
2. Click the three dots in the top right corner and select **Custom repositories**.
3. Add the URL of this repository (`https://github.com/mjrealm/ha-aera-for-home`) and select **Integration** as the category.
4. Click **Add**, then search for "Aera for Home" in HACS and click **Download**.
5. **Restart** Home Assistant.
6. Go to **Settings > Devices & Services > Add Integration** and search for "Aera for Home".

### Manual
1. Download the latest release from this repository.
2. Copy the `custom_components/aera` directory into your Home Assistant's `config/custom_components/` directory.
3. **Restart** Home Assistant.
4. Go to **Settings > Devices & Services > Add Integration** and search for "Aera for Home".

## Entities

### Switch

| Name | Description | Entity Name |
| :--- | :--- | :--- |
| **Power** | Main power control for the diffuser. | `switch.<device_name>_power` |

### Number

| Name | Description | Entity Name |
| :--- | :--- | :--- |
| **Intensity** | Fragrance intensity control (1 to device max). | `number.<device_name>_intensity` |

### Sensor

| Name | Description | Entity Name |
| :--- | :--- | :--- |
| **Current Fragrance** | Displays the name of the currently inserted fragrance cartridge (e.g. "White Tea"). | `sensor.<device_name>_fragrance_name` |
| **Fragrance Remaining** | The remaining percentage of the fragrance cartridge. | `sensor.<device_name>_fragrance_remaining` |

## Credits

This integration is powered by the unofficial [aeraforhome](https://pypi.org/project/aeraforhome/) Python library.
