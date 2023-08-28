# Sea of Stars TAS

This Tool Assisted Speedrun uses memory reading and branching logic to automate speedrunning Sea of Stars.
We are not necessarily aiming to be faster than the best human players but are trying to dynamically handle any situation the game has to offer.  
This project has been inspired by the [FFX TAS](https://github.com/coderwilson/FFX_TAS_Python) and [Evoland TAS](https://github.com/orkaboy/Evoland_TAS) that work in a similar fashion.  
Please join [our Discord](https://discord.gg/KrQcSUMuh) if you are interested in the project.  
(If any links are dead, contact @shenef on Discord)

## Progress log

- **2023/08/29:** It's the day of the release and we made good progress. Aside from more internal preparations and adding the first parts of a battle system, the route has been expanded to include the full first room of the Wizard's Lab. Current progress video: <https://youtu.be/yHHF6upZRB4>  
This might mark the end of the work on the demo TAS, with the full game releasing today, there is a lot of new work ahead of us.
- 2023/08/24: The tooling is now capable of reading various data from the game in realtime and we have a short demo TAS that starts at the title screen and ends after the Tavern scene in Brisk.
- 2023/08/11: Initial commit. The game has not yet been released so we are looking into the Demo to figure out the needed tools and memory locations. There currently is no functioning TAS or tooling.

## Setup

Install Python, clone the repo and run `pip install -r requirements.txt`, start the game and then run `py main.py`.

## Contribute

If you want to contribute code, please run `pip install -r dev-requirements.txt`, `pre-commit install` and join our discord.
