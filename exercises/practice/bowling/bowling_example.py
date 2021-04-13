from z3 import*

NUM_FRAMES = 10
MIN_STRIKE_OR_SPARE_SCORE = 10

def bowlingScore(pins_per_roll):
    # Calculate the indices in 'pins_per_roll' list that indicate the start of a frame
    frame_start_indices = get_frame_start_indices(pins_per_roll)

    # Declare lists to append Z3 equations
    constants = []
    equations = []

    # Add Number of Pins per Roll as their own variables
    num_pins_per_roll = [Int(f"num_pins_per_roll{roll_number}") for roll_number in range(len(pins_per_roll) + 1)]
    for roll_number in range(len(pins_per_roll)):
        constants.append(num_pins_per_roll[roll_number] == pins_per_roll[roll_number])

    # Add additional 'Number of Pins per Roll' to ensure no list overbound error occurs below (set to 0 so it doesn't interfere with calculations)
    constants.append(num_pins_per_roll[len(pins_per_roll)] == 0)

    # Calculate and Add Number of Rolls per Frame as their own variables
    rolls_per_frame = [Int(f"rolls_per_frame{frame_number}") for frame_number in range(NUM_FRAMES)]
    for frame_number in range(NUM_FRAMES - 1):
        constants.append(rolls_per_frame[frame_number] == (frame_start_indices[frame_number + 1] - frame_start_indices[frame_number]))

    constants.append(rolls_per_frame[NUM_FRAMES - 1] == (len(pins_per_roll) - frame_start_indices[NUM_FRAMES - 1]))

    # Determine score equation for each frame depending on strike, spare, or open frame
    frame_scores = [Int(f"frame_score{i}") for i in range(NUM_FRAMES)]
    for frame_number in range(NUM_FRAMES - 1):
        frame_start_index = frame_start_indices[frame_number]

        # If Strike or Spare, add 3 rolls (Strike: 1 + 2 extra) (Spare: 2 + 1 extra)
        # Else (If Open), add 2 rolls
        frame_equation = If(num_pins_per_roll[frame_start_index] + num_pins_per_roll[frame_start_index + 1] >= MIN_STRIKE_OR_SPARE_SCORE,
                frame_scores[frame_number] == num_pins_per_roll[frame_start_index] + num_pins_per_roll[frame_start_index + 1] + num_pins_per_roll[frame_start_index + 2],
                frame_scores[frame_number] == num_pins_per_roll[frame_start_index] + num_pins_per_roll[frame_start_index + 1])

        equations.append(frame_equation)

    # Frame 10 has a different equation
    frame_start_index = frame_start_indices[NUM_FRAMES - 1]

    # No list overbound error occurs if there is no third roll in Frame 10 because an extra 'Number of Pins per Roll' was added (set to 0 so it doesn't interfere with calculations)
    frame_equation = (frame_scores[NUM_FRAMES - 1] == num_pins_per_roll[frame_start_index] + num_pins_per_roll[frame_start_index + 1] + num_pins_per_roll[frame_start_index + 2])
    equations.append(frame_equation)

    # Add Equations to Solver and Find Model
    s = Solver()
    s.add(constants + equations)
    s.check()
    m = s.model()

    # Sum scores for each frame to calculate total score
    total_score = 0
    for frame_number in range(NUM_FRAMES):
        total_score += int(str(m.eval(frame_scores[frame_number])))

    return total_score

def get_frame_start_indices(pins_per_roll):
    #Determine indices in input list where each of the 10 frames start in standard bowling game
    frame_start_indices = [0] * NUM_FRAMES
    roll_count = 0
    for i in range(NUM_FRAMES):
        frame_start_indices[i] = roll_count
        if pins_per_roll[roll_count] == 10:
            roll_count += 1
        else:
            roll_count += 2
    return frame_start_indices