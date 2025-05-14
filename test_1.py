from adventure import AdventureManager



ai = AdventureManager(
    # jpeg seems to be the lighter format as of now.
    img_fmt='jpeg',
    # Compression level doesn't seem to work (2025-05-02).
    #img_compression=100
)

print('Generating the first area initial visual representation...')
area_1 = ai.gen_img('A room with 3 doors, a table, 3 chairs and a window, the room has some furnitures. The house is in a city and it is morning.')
ai.save_img('area_1', area_1)

print('Editing it...')
area_1_edit_1 = ai.edit_img(area_1, 'I throw one of the chairs onto the floor.')
area_1_edit_1_path = ai.save_img('area_1_edit_1', area_1_edit_1)

print('Loading the edit...')
area_1_edit_1 = ai.load_img(area_1_edit_1_path)
print('Editing it again...')
area_1_edit_2 = ai.edit_img(area_1_edit_1, 'I use the time machine to travel into the future, 50 years from now.')
ai.save_img('area_1_edit_2', area_1_edit_2)

print('Editing/Genereting the second area...')
area_2 = ai.edit_img(area_1_edit_2, 'I exit through the window and walk outside.')
ai.save_img('area_2', area_2)