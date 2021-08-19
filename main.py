import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD #the tileset to use
    )

    event_handler = EventHandler()

    with tcod.context.new_terminal(
            screen_width,
            screen_height,      #passing all these as arguments
            tileset=tileset,
            title="Roguelike Demo",
            vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F") #creates console
        while True: #Main game loop
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console) #updates screen

            root_console.clear()

            for event in tcod.event.wait(): #Listens for user's input
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()

if __name__ == "__main__":
    main()