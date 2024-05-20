# KMK-Mechanical-Keyboard

# 1. Making the Layout
## Requirements
The layout I would design had certain specifications for my use case. I needed:
1. A function row
2. A numpad
3. Insert and Delete Keys
4. Volume keys
5. Print screen key
6. The total width of the keyboard had to be as long as or shorter then a traditional full-size keyboard.
7. The cost of the keyboard should be ~$100.

In addition, I had other requirements that I simply wanted:
* The numpad will be left-handed. I wanted to find out whether not having to move my hand between the mouse and numpad when typing into spreadsheets would increase productivity.
  * This had a secondary purpose of centering the main keys; The numpad will be on the left whereas the mouse will be on the right. Normally both are on the right side, so main keys are shifted left, messing with ergonomics.
* The keybard will be ergonomic with a split down the center of the home row of the keyboard.
* The keyboard will have hot-swappable switches.
* The keyboard will sound "nice"
These requirements were chosen so that I would make a keyboard layout which does not yet exist on the market. It served as justification for why I had to handwire one and not just go out and build a normal keyboard.

## Problems
With the budget set in mind, the microcontroller was already decided for me; it would be the Raspberry Pi Pico. At only $4, there was no other micro controller that could come even close to its price while providing as many GPIO pins that it has. Even though it came with whopping 26 GPIO pins, it was still one pin short of making a traditional full-size keyboard layout, which needed 27. This meant that I had to find a way to reduce the number of columns my keyboard had by one in order to meet the pin requirement.
The budget also meant that my keyboard layout should use as many standard keys as possible. Any exotic keyshapes meant a more expensive keycap set to accomodate them. Since I wanted a split keyboard, my layout could not be a standard Alice layout, since its split space bar and two 'B' keys was hard to find among the cheapest keycap sets (this space bar requirement will cause a lot of problems down the line). It also had the characteristic of making any keyboard using its layout very long, which wouldn't work well with my length requirement.

With these considerations, I went on to making my keyboard layout.

## Layouts
My layout was designed on the aptly named website [Keyboard Layout Editor](http://www.keyboard-layout-editor.com/). This will allow me to experiment with as many layouts as I can digitally before I commit to one physically. 
I started with an ANSI 104 preset as a base to make changes on (the keyboard layout most people think of).

# 2. Finding Parts
