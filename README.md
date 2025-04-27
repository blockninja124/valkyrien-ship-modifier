# Valkyrien Ship Modifier
This is a python application written using Tkinter, which allows you to easily edit Valkyrien Skies ship-data files.

This can be useful when you need to remove a corrupted ship, or change its data externally. 

## Running

### From Source

Simple run the `main.py` python script.
The `NBT` library is required. You can install it via pip:

```console
pip install NBT
```

### From .exe

You can find .exe artifact files, compiled with pyinstaller, from the latest github "build" action.

## Usage

Once you have the program launched, simply hit "open file". It will prompt you to locate a vs ship data file (`vs_ship_data.dat`). These are stored at: `<minecraft>/saves/<your world>/data/`. (`<minecraft>` will vary depending on what launcher you use). 

You can then navigate the data. Once you reach a value you want to change, simply double click it.

- If the value is a number, it will not allow you to type letters. 
- If it has letters, it _will_ let you type numbers, but this could cause issues!
- If it is `null`, it cannot be changed (although it can be deleted)
- If it is `True` or `False`, it can only be chaged to `True` or `False`, any other value will not save

## Oops I broke my world

**Editing the ship data file is _inherently_ dangerous! Do it only at your own risk!**

Its also _highly_ recommended to make a world backup! Or atleast a copy of the `vs_ship_data.dat` file elsewhere.

If you do make a big mistake, don't panic. You have a couple of options to undo it.

### Option 1:

**Don't save.** If you haven't saved your mistake yet, simply hit "close" and confirm that you want to lose your unsaved changed.

### Option 2:

If you have already saved, again don't panic! Whatever you do **don't save again**. When you save, the application creates a backup of your previous data file, simple named `vs_ship_data.dat_old`. Close the app, _don't save_, and delete `vs_ship_data.dat`. Then rename `vs_ship_data.dat_old` to `vs_ship_data.dat`.

### Option 3:

If you have already saved your ship file twice, then `vs_ship_data.dat_old` has already been overwritten with the bad data. You can try to fix the data using the app, or if its beyond its capabilities you can edit the file manually:

- Open it in any nbt viewer (e.g. https://www.brandonfowler.me/nbtreader/)
- Copy the data from `data/vspipeline`. It should be a list of numbers
- The list of numbers is bytes. Simple use the bytes as a text file
- It's serialized json - Ascii encoding
- It’ll then look a lot nicer if you put it into https://jsonformatter.org/
- Repair your data
- Do all the steps to open the file in reverse
(serialize the json, then turn the ascii string into bytes, then put it back in the ships.dat)