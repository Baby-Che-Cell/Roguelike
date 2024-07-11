#!/usr/bin/env python3
import tcod

#Inputs and their classes
from actions import EscapeAction, MovementAction
from input_handler import EventHandler


def main() -> None:
    #defining screen dimensions, move into json file later
    screen_width=80
    screen_height=50

    #defining player position
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    #loading tilesheet to be used
    tileset = tcod.tileset.load_tilesheet(
        "gametiles.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    #This creates the terminal to be used
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        #The main game loop that updates constantly
        while True:
            #prints the player
            root_console.print(x=player_x, y=player_y, string="@")

            #this command refreshes the frame
            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue
                    
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                #Escapes the game
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


#Stopper so this doesnt run unless called
if __name__ == "__main__":
    main()