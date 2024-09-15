import os
import google.generativeai as genai
from google.generativeai.types import content_types
from collections.abc import Iterable

genai.configure(api_key=os.environ["API_KEY"])

def set_light_values(brightness: int, color_temp: str) -> dict:
    """Set the brightness and color temperature of a room light. (mock API).

    Args:
        brightness: Light level from 0 to 100. Zero is off and 100 is full brightness
        color_temp: Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.

    Returns:
        A dictionary containing the set brightness and color temperature.
    """
    print(f"LIGHTBOT: Lights set to brightness({brightness}) and colorTemperature({color_temp}).")
    return {
        "brightness": brightness,
        "colorTemperature": color_temp
    }

model = genai.GenerativeModel(model_name='gemini-1.5-flash', tools=[set_light_values])

chat = model.start_chat()

def tool_config_from_mode(mode: str, fns: Iterable[str] = ()):
    """Create a tool config with the specified function calling mode."""
    return content_types.to_tool_config(
        {"function_calling_config": {"mode": mode, "allowed_function_names": fns}}
    )

def send_message_in_none_mode():
    # Text-only mode: NONE
    tool_config = tool_config_from_mode("NONE")
    response = chat.send_message('Dim the lights so the room feels cozy and warm.', tool_config=tool_config)
    print(response.text)

    """
    [출력]

    As a language model, I can't physically interact with the real world, so I can't dim the lights for you. 

    However, I can help you achieve that cozy and warm feeling!  

    **Here are some tips:**

    * **Use a dimmer switch:** This is the easiest way to adjust the lighting.
    * **Use warm-toned light bulbs:** Warm white or soft white bulbs create a more inviting ambiance than cool white bulbs.
    * **Use candles:** Candles add a warm glow and a relaxing scent to the room.
    * **Add soft lighting:**  Lamps with soft shades or string lights can add a cozy touch.
    * **Draw the curtains:**  Dimming the lights will make the room feel more intimate.
    * **Add throws and blankets:**  Cozy up with soft blankets and throws.

    I hope these tips help you create a cozy and warm atmosphere in your room!
    """

def send_message_in_auto_mode():
    # Automatic mode: AUTO
    tool_config = tool_config_from_mode("AUTO")
    response = chat.send_message('Dim the lights so the room feels cozy and warm.', tool_config=tool_config)
    print(response.parts)  # response.text 없음

    """
    [출력]

    [function_call {
    name: "set_light_values"
    args {
        fields {
        key: "color_temp"
        value {
            string_value: "warm"
        }
        }
        fields {
        key: "brightness"
        value {
            number_value: 50
        }
        }
    }
    }]
    """

def send_message_in_any_mode():
    # Function-calling mode: ANY
    tool_config = tool_config_from_mode("ANY", ["set_light_values"])
    response = chat.send_message('Dim the lights so the room feels cozy and warm.', tool_config=tool_config)
    print(response.parts)  # response.text 없음

    """
    [출력]

    [function_call {
    name: "set_light_values"
    args {
        fields {
        key: "color_temp"
        value {
            string_value: "warm"
        }
        }
        fields {
        key: "brightness"
        value {
            number_value: 50
        }
        }
    }
    }]
    """

def send_message_in_automatic_second_call_mode():
    # Automatic function calling
    auto_chat = model.start_chat(enable_automatic_function_calling=True)
    tool_config = tool_config_from_mode("AUTO")
    response = auto_chat.send_message('Dim the lights so the room feels cozy and warm.', tool_config=tool_config)
    print(response.text)

    """
    [출력]
    
    LIGHTBOT: Lights set to brightness(50.0) and colorTemperature(warm).
    OK. I've dimmed the lights to 50% and set the color temperature to warm.  Let me know if you'd like to adjust them further.
    """

send_message_in_automatic_second_call_mode()