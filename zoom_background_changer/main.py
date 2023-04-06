import datetime
import json
import os
import urllib

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

ZOOM_DIR = f"/Users/{os.getlogin()}/Library/Application Support/zoom.us/data/VirtualBkgnd_Custom/"


def read_config_file() -> dict:
    """Read the config file at $HOME/.zoom-background-changer.

    Use config file's contents to build values for `weather` and `temperature`.
    `weather` is built by calling to https://wttr.in/{city}?format=j1
    `temperature` is built by calling to https://wttr.in/{city}?format=j1

    Returns:
        dict: The config file as a dictionary."""
    config_file_path = os.path.expanduser("~/.zoom-background-changer")
    # if the config file doesn't exist, create it
    if not os.path.exists(config_file_path):
        with open(config_file_path, "w") as f:
            f.write(
                json.dumps(
                    {
                        "city": "Boston",
                    }
                )
            )

    config = json.load(open(config_file_path))
    city_wttr = json.load(
        urllib.request.urlopen(f"https://wttr.in/{config['city']}?format=j1")
    )
    config["weather"] = city_wttr["current_condition"][0]["weatherDesc"][0]["value"]
    config["temperature"] = city_wttr["current_condition"][0]["temp_F"]
    return config


def build_prompt(config: dict) -> str:
    """Build the prompt for the OpenAI API.

    Args:
        config (dict): The config file as a dictionary.

    Returns:
        str: The prompt for the OpenAI API."""

    template = """A colorful Zoom background for {date}.
      The weather in {city} is {weather} and {temperature} degrees farenheight today.
      Include the {city} skyline.
      Photo, Skyline, Weather, Real Photo, Real Skyline, Real Weather.
      """

    try:
        template = config["prompt"]
    except KeyError:
        pass

    today = datetime.datetime.now()

    prompt = template.format(
        date=today,
        city=config["city"],
        weather=config["weather"],
        temperature=config["temperature"],
    )

    return prompt


def generate_new_image() -> str:
    """Return URL of new image from openai."""
    return openai.Image.create(
        prompt=build_prompt(read_config_file()),
        n=2,
        size="1024x1024",
    )["data"][0]["url"]


def main():
    """Generate new image and replace the existing zoom background."""
    # Generate a new image URL
    new_image_url = generate_new_image()

    # Get the name of the current file in the directory
    current_file = os.listdir(ZOOM_DIR)[0]

    # Download the new image from the URL and save it as the current file
    urllib.request.urlretrieve(new_image_url, ZOOM_DIR + current_file)


if __name__ == "__main__":
    main()
