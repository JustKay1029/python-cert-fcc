test_settings = {
    "brightness": 50,
    "volume":60,
    }

def add_setting(test_settings, pairs):
    key,value = pairs
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        test_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(test_settings,pairs):
    key,value = pairs
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        test_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(test_settings,sett):
    key = sett.lower()
    if key in test_settings:
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(test_settings):
    if len(test_settings) == 0:
        return "No settings available."
    lines = ["Current User Settings:"]
    for key, value in test_settings.items():
        capitalized_key = key.capitalize()
        lines.append(f"{capitalized_key}: {value}")
    
    return "\n".join(lines) + "\n"