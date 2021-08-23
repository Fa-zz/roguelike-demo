# Sets up initial variables (screen size, tileset), creates entities, passes them to the engine

import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD #the tileset to use
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width/2), int(screen_height/2), "@", (255,255,255))
    npc = Entity(int(screen_width/2-5), int(screen_height/2), "@", (255,255,0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
            screen_width,
            screen_height,      #passing all these as arguments
            tileset=tileset,
            title="Roguelike Demo",
            vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F") #creates console
        while True: #Main game loop
            engine.render(console=root_console, context=context) # prints to screen

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
