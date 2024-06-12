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

prioritozed compact layout over keycap compatability due to microcontroller pins

# 2. Finding Parts
After watching many handwired keyboard videos, I have determined the minimum list of parts that I need:
1. micro-controller (which has already been decided as a Pi Pico)
2. 104 switches (based on the planned layout)
3. at least 104 1N4148 diodes
4. 7 plate-mount stabilizers (6 2u and 1 6.25u)
5. keycaps (with a 1.75u spacebar and at least 3 bonus/media keys)
6. 22 gauge copper wire

The most important part of the keyboard is the switch, which can also be the most expensive part. This was especially true since I would be sourcing 104 switches. Therefore, my first order of business was to find the best value switch availabe on the market. Sound quality was an initial consideration, but I eventually dismissed it since it wasn't a priority, and finding good switches was a role better suited to a future keyboard design. I eventually found the Keychron K Pro switches, which came in a set of 110 switches for $16. Even after considering the shipping costs, its price per switch is still lower than any other switch on the market. Since there were multiple colors to choose from, I chose brown because people who are unfamiliar with mechanical keyboards (me) generally prefer them.

Every single switch needs a diode so that the keyboard can support [n-key rollover](https://en.wikipedia.org/wiki/Key_rollover). All of the videos I have seen have used 1N4148 diodes. I don't know why, but there's no reason to start experimenting with others here. It's also only $5 for 125, which seems like a fair price.

My layout will need a 1.75U shift, which isn't a standard key, but it is common enough among keycap sets that it shouldn't be a problem. Especially for mechanical keyboards, 
