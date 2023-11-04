This is the README file of the random name project.
===

Overview
---
The random name project provides a program which can
read a namelist file and randomly call the roll.

Basic Usage
---
 - First, there should be a "name.txt" file in the working
dictionary of the program. A good example is as follows:
```
Tom
Jerry
Sam
Bobby
Alice
etc.
```
 - Second, run the program and choose the "随机" option.
 - Enjoy your random names!

Detailed Description about Commands
---
Open the control panel and type commands, to explore more
interesting features.  
The commands are as follows.

```
set
```
 - This command allows you to add members to the name list
and set the number of this member.

```
guess-number
```
 - This command allows you to play the guess number game.

```
bagels
```
 - This command allows you to play the bagels game.

```
tic-tac-toe-board
```
 - This command allows you to play the Tic Tac Toe game on a
present board. Remember that there isn't an algorithm to
detect if a place is dropped twice.And there are also some 
bugs in this program.

```
mine
```
 - Theoretically, you can type this command to play the 
minesweeper game. But in fact, there isn't a minesweeper
game, because the developer is too lazy.

```
about
```
 - This command allows you to check the "about" page.

```
edit
```
 - This command allows you to open the default namelist file,
usually the "name.txt", which can be changed in the config
file.

```
readme
```
 - This command allows you to open the README file (this file).

```
re-generate
```
 - This command allows you to regenerate the namelist with a new
namelist file, or the "name.txt" file which has been changed.

Detailed Descriptions about Name lists
---
 - Usually, there should be one default namelist file in the dictionary.
Its name can be changed in the config.txt file (see below).The default
name of the default namelist is "name.txt".  
 - There can be multiple name lists. You can use the "re-generate" command
to regenerate the built-in namelist with a new namelist file.  
 - There should be only one name in a line.  
 - There shouldn't be blank lines in the file.

Configurations
---
The config.txt file in the dictionary allows you to change the
default configurations of the program.  
A good config.txt file should be like this:
```
# config.txt, the configurations of random number program.
empty
# the default context of the control panel, 'empty' for blanks.
name.txt
# the default name of the namelist file.
README.md
# the default name of the README file.
0
# decide whether the control panel is hidden. 1 for true, 0 for false.
```
Writing tips:
 - All lines starting with hashes(#) are invalid, they're called
comments.Comments are used to make the file easier to read.  
 - All blank lines will be ignored.  
 - All lines with spaces will cause error, so don't do that.
The developer hasn't debugged the spaces-included-lines.  
 - The first line including significant contents determines
the default content of the control panel interface 
(type "empty" for blank).
 - The second line determines the default name list file
   (usually "name.txt").
 - The third line determines the default README file
   (usually "README.md", i.e. this file.)
 - The fourth line determines whether the control panel is hidden.
Type 0 for false (shown), and 1 or other positive numbers for
true (hidden).

Developers & Acknowledgements
---
 - Designed by CrazyAuF3
 - Programmed by CrazyAuF3
 - Debugged by Ww-yd
 - Thanks to Ww-yd for his contribution to the debugging part of
the program.