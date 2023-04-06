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

First you will need to set a custom background image in Zoom.

You can do this by going to `Preferences > Video > Virtual Background > Choose Virtual Background...` and selecting an image.

Then from the command line, run:
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
- `{city}`: The current city, set from the `city` key in the `.zoom-background-changer` file. Defaults to `Boston, MA`. If set, the following extra variables will be available:
  - `{weather}`: The current weather, from `https://wttr.in/`
  - `{temperature}`: The current temperature, from `https://wttr.in/`

Any other key/value pairs in the `.zoom-background-changer` file will be available as variables in the prompt template, so get creative!

If you would like to request a new functional variable similar to `city`, please open an Issue or Pull Request!
