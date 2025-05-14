# Description
An interactive fiction where natural language processing is performed by modern AI so that the player can attempt anything they can think of.
The AI generates an image representation for each area explored by the player, edit it whenever the player attempts to do anything in that area.
NPCs also use an LLM and each one has its own context.

# Example
First area
<br>
**Prompt**: `A room with 3 doors, a table, 3 chairs and a window, the room has some furnitures. The house is in a city and it is morning.`
<br>
![Area 1](examples/area_1.avif)

First area edit (1)
<br>
**Prompt**: `I throw one of the chairs onto the floor.`
<br>
![Area 1 Edit 1](examples/area_1_edit_1.avif)

First area edit (2)
<br>
**Prompt**: `I use the time machine to travel into the future, 50 years from now.`
<br>
![Area 1 Edit 2](examples/area_1_edit_2.avif)

Second area
<br>
**Prompt**: `I exit through the window and walk outside.`
<br>
![Area 2](examples/area_2.avif)


# Instructions
Just run `test_1.py` with Python in a virtual environment. The images will be saved to `output\`.