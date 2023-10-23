# SV_mouse_events
Tool to track mouse events and give SpeakerView (Godot engine) *click through* capabilities on MacOS.

## Building
### Install dependencies
Install python 3.12 from python [website](https://www.python.org/).
Install macmouse module:
```
pip3 install macmouse
```
Install pyinstaller module:
```
pip3 install pyinstaller
```


### Clone SV_mouse_events sources
```
git clone git@github.com:GRIS-UdeM/SV_mouse_events.git
```

### Compiling
```
cd SV_mouse_events
pyinstaller --target-arch universal2 SV_mouse_events.py
```

## Running
For SpeakerView to automatically start SV_mouse_events process, the content of `dist/SV_mouse_events/` created by pyinstaller must be placed in a directory named `SVME` in the same directory as SpeakerView.
On first launch, MacOS will ask to give SpeakerView accessibility access (SpeakerView Apple menu > System Settings > Privacy & Security > Accessibility).
