# Instructions

Given the number of pins that somebody knocks over each roll, calculate their final score in a game of bowling.


## Calculating Bowling Scores

There are ten frames in a game of bowling. A player gets two rolls per frame to try to knock down all 10 pins. If they knock down all 10 pins on the first roll of the frame then they don't roll a second time that frame (see below).

* When all 10 pins are knocked down on the first roll of a frame, a strike has occurred. The total value of a strike is 10 plus the number of pins knocked down in the next two rolls. If two strikes are rolled in a row, then the score from the first strike cannot be calculated until the next roll.

* When all 10 pins are knocked down by the second roll of a frame, a spare has occurred. The total value of a spare is 10 plus the number of pins knocked down in the next roll.
  
* When neither a strike or a spare occurs in a frame, it is declared to be an open frame. The total value of an open frame is the number of pins knocked down during that frame.

* If a strike or spare occurs during the tenth frame, the player gets three total rolls that frame.  The total value of the tenth frame is the number of pins knocked down during that frame.


## Requirements

Calculate a player's final score in a game of bowling based on the number of pins knocked down each roll. 

Remember: A strike occurs when 10 pins are knocked down on the player's first roll of a frame and a spare occurs when the number of pins knocked over on their first and second rolls equals 10.
