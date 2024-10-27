<h1 align="center">
    <br>
    <a href=""><img src="./assets/mello_pfp.jpg" width="200"></a>
    <br>
    Mello
    <br>
</h1>

<h4 align="center">A Simple Discord Bot written in <a href="https://www.python.org" target="_blank">Python</a> for my Discord Server /serenity*</a></h4>
<p align="center">*server is still under development!</p>

<p align="center">
    <a href="https://www.python.org">
        <img src="https://img.shields.io/badge/Python%20Version-3.12%2B-blue?style=flat&logo=python">
    </a>
        <a href="https://github.com/Rapptz/discord.py">
        <img src="https://img.shields.io/pypi/v/discord.py?style=flat&logo=discord&label=discord.py">
    </a>
    <a href="https://github.com/python-poetry/poetry">
        <img src="https://img.shields.io/pypi/v/poetry?style=flat&logo=poetry&label=Poetry">
    </a>
    <a href="https://github.com/itzAyrun/mello">
        <img src="https://img.shields.io/github/commit-activity/w/itzAyrun/mello?style=flat&logo=gitforwindows">
    </a>
</p>

<p align="center">
    <a href="#installation">Installation</a> •
    <a href="#Usage">Usage</a> •
    <a href="#contributing">Contributing</a> •
    <a href="#license">License</a> •
    <a href="#acknowledgements">Acknowledgements</a> •
    <a href="#contact">Contact</a>
</p>

## Current Features

- **Hello Command**: A simple command that responds with a friendly greeting.

## Planned Features

- Moderation tools( kick, ban, mute )
- Fun commands( jokes, trivia, games )
- Music playback( not too sure about this one )
- Polls and voting systems
- Custom commands

## Installation

### Prerequisites

- Python 3.12 or higher
- [discord.py](https://github.com/Rapptz/discord.py) library

### Setup

1. Clone the repository


```bash
git clone https://github.com/itzAyrun/mello.git
cd mello
```

2. Install the required packages:

```bash
pip install requirements.txt
```

3. Create a `.env` file in the root directory and add your bot token:


```env
BOT_TOKEN="your_bot_token_here"
```

4. Run the bot( from the root directory! ):

```bash
# If you have 'make' installed in your system
make run

# OR

# Run it manually
python -m mello.main
```

5. ( Optional ) If you want to change the prefix:

Open the [config.toml](./config.toml) file in the root directory and add your custom prefix. Please keep the prefix short and not more than 2 characters long.

```toml
prefix = ["?"]  # This is the default prefix

# To add your custom one, just append the prefix to the array
prefix = ["?", "!"]

# It is also recommended to not leave this empty, even though mello supports both slash and text commands
```

## Usage

Once the bot is running, you can use the following commands in your Discord server:


```bash
<prefix_set_for_the_bot>hello

# OR
<prefix_set_for_the_bot>hi

# OR
<prefix_set_for_the_bot>hey

# slash commands are also supported
/hello
```

The bot will respond with a random greeting response.

## Contributing

Feel free to modify the source code to fit your needs! Contributions and improvements are welcome.
If you have any ideas for new features, consider opening an issue or submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgements

Thanks to the [discord.py](https://github.com/Rapptz/discord.py) community for their support and documentation.

## Contact

For any inquiries or feedback, feel free to reach out to [ayrun3412@gmail.com].
