${toc}

# KMK-Mechanical-Keyboard
This file serves to document my experience and process in making my first mechanical keyboard, mistakes and lessons included, for future reference when I inevitably build another one.

# 1. Making the Layout
## Requirements
The layout I would design had certain specifications for my use case. I needed:
1. A function row
2. A numpad
3. Insert and Delete Keys
4. Volume keys
5. Print screen key
6. The total width of the keyboard had to be as long as or shorter then a traditional full-size keyboard.
7. The cost of the keyboard should be ~$100 (this will become the biggest consideration of the entire build).

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
6. 22 gauge copper wire (at least 300ft)
7. Any extra tools needed to build the keyboard

Most of these parts will be bought on Amazon for meet their free shipping purchase requirement. 

The most important part of the keyboard is the switch, which can also be the most expensive part. This was especially true since I would be sourcing 104 switches. Therefore, my first order of business was to find the best value switch availabe on the market. Sound quality was an initial consideration, but I eventually dismissed it since it wasn't a priority, and finding good switches was a role better suited to a future keyboard design. I eventually found the Keychron K Pro switches, which came in a set of 110 switches for $16. Even after considering the shipping costs, its price per switch is still lower than any other switch on the market. This isn't even considering the fact that they came factory lubed, which will save hours of work. Since there were multiple colors to choose from, I chose brown because people who are unfamiliar with mechanical keyboards (me) generally prefer them. The only place to buy these are on Keychorn's official website, so that's where I purchased them.

Every single switch needs a diode so that the keyboard can support [n-key rollover](https://en.wikipedia.org/wiki/Key_rollover). All of the videos I have seen have used 1N4148 diodes. I don't know why, but there's no reason to start experimenting with others here. It's also only $5 for 125 on Amazon, which seems like a fair price.

Since my keyboard won't have a pcb, I couldn't buy pcb-mounted stabilizers, which are usually more secure. Instead, my only option are plate-mounted stabilizers, which are prone to popping out when being tossed around. Luckily, I don't intend on bringing my keyboard anywhere, so plate-mount should be just fine. In terms of stabilizer quality, there are many options that I think are unnecessarily expensive, as a few simple mods can make most pairs of stabilizers silent (which is the goal, you shouldn't ever hear stabilizer rattle). I chose the Epomaker Plate-Mounted Stabilizers on Amazon because they came with 7 stabilizers, some lubricant, and a brush all in one for $8. Lube is essential for silencing stabilizers, and I wouldn't have to pay extra for it. At that value, this set is hard to beat.

My layout will need a 1.75U shift, which isn't a standard key, but it is common enough among keycap sets that it shouldn't be a big problem. Especially for mechanical keyboards, keycap sets usually come with many extra keys to support lots of configurations because recently 65% boards have become quite popular (which uses a 1.75u shift). I also wanted keycaps with a 1.5mm wall thickness. It's pretty clear the sound benefits of using thick keycaps instead of thin ones, and the chances are a thick keycap set also accomodates many configurations, so it shouldn't be hard to find. I settled on the Honey Milk keycap set on Amazon for $18, since it was the cheapest set that fufilled my needs. In hindsight, I hate its looks and would much prefer to spend a little extra on a better looking set. Since the keycaps are the main contributor towards the overall look of a keyboard, my keyboard lost a lot of style points.

Next is 22 gauge copper wire. I need this gauge specifically since I will be using 3d printed hotswap sockets designed for this diameter. Honestly any wire will work. I only used copper because I intended to solder with it, but you will see later that that will not be the case. Without looking I bought some craft wire from the art store. This ended up being a monumental mistake that set my project back a year (due to school). Instead, you should just find an old ethernet cable with **solid-core** wire and strip them manually with wire strippers. It takes some time, but you can usually find those cables for free. It took me two tries to find a cable with solid core wire. I ended up actually needing the cable with stranded wire, but I could get away with just one if I were to do this project again.

To build the keyboard will also need extra parts. I couldn't predict them in advance, so I just bought what I needed as I needed them. The final list of things I *actually* used is:
1. wire strippers
2. mechanical switch puller
3. keycap puller (most sets come with one, like mine)
4. 3d printer and filament (this is expensive, but it's a given that you already have this if you are pursuing this project)
5. silicone caulk
6. M3 screws
7. sandpaper
8. superglue
