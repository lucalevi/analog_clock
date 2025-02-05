# Analog Clock in Python (Tkinter)

![The final graphical clock]([http://url/to/img.png](https://github.com/lucalevi/analog_clock/blob/main/clock.png))

A simple **analog clock** built using Python and Tkinter. This project visually represents an analog clock with hour, minute, and second hands, along with numbers and tick marks.

## Features
- Displays a **real-time** analog clock.
- Uses **Tkinter Canvas** for drawing.
- Includes **hour markers and numbers**.
- Fully **responsive and auto-updating** every second.
- Simple and lightweight with no external dependencies.

## Installation
### 1. Ensure Python is Installed
This project requires Python **3.6 or later**. You can check your version with:
```sh
python --version
```
If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).

### 2. Install Tkinter (if not already installed)
Tkinter is included with most Python distributions, but if you run into errors, install it as follows:

#### **Windows**
Tkinter is typically pre-installed. If not, install it using:
```sh
pip install tk
```

#### **MacOS** (if Tkinter is missing)
MacOS users may need to install Tkinter manually:
```sh
brew install tcl-tk
```
Then, ensure Python recognizes Tkinter:
```sh
export LDFLAGS="-L/opt/homebrew/opt/tcl-tk/lib"
export CPPFLAGS="-I/opt/homebrew/opt/tcl-tk/include"
```
If using **pyenv**, also run:
```sh
pyenv install --force 3.x.x  # Replace with your Python version
```

#### **Linux**
For **Debian/Ubuntu**-based distributions:
```sh
sudo apt update && sudo apt install python3-tk
```
For **Arch Linux**:
```sh
sudo pacman -S tk
```
For **Fedora**:
```sh
sudo dnf install python3-tkinter
```

## Running the Analog Clock
Once Tkinter is installed, clone this repository and run the script:
```sh
git clone https://github.com/yourusername/analog-clock.git
cd analog-clock
python analog_clock.py
```
The analog clock should now appear!

## Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

## License
This project is open-source and available under the **MIT License**.

