# Zoom Background Changer

This is a python script that will use OpenAI's GPT-3 API to generate a new background image for your Zoom meetings.
It can be run as a cron task, manually, or as part of a workflow when you open Zoom!

The script will generate a new background image based on the current date and weather, and overwrite you existing Zoom background.

## Requirements

- Only works on macOS (for now!)
- Python 3.9+
- OpenAI API Key
  - You can get a free API key from OpenAI [here](https://platform.openai.com/).
  - You will need to create an account and generate an API key.
  - You will need to add your API key to the `OPENAI_API_KEY` environment variable.

## Installation

```bash
pip install zoom-background-changer
```

## Usage

```bash
zoom-background-changer
```

## Prompt Template

Can be adjusted by creating a file called `.zoom-background-changer` in your `$HOME` directory.

This file should contain the following:

```json
{
  "prompt": "Today is {date} and the weather is {weather} in {city}.",
  "city": "Boston"
}
```

### Available Variables

- `{date}`: The current date
- `{weather}`: The current weather, from `https://wttr.in/`
- `{city}`: The current city, set from the `city` key in the `.zoom-background-changer` file. Defaults to `Boston, MA`.
- `{time}`: The current time

If you would like to request other variables to be available, please open an issue!
