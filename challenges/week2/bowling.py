class Frame:
    def __init__(self, rolls):
        self.rolls = rolls
        self.__next_frame = None

    @property
    def next_frame(self):
        return self.__next_frame

    @next_frame.setter
    def next_frame(self, frame):
        self.__next_frame = frame

    @property
    def score(self):
        score = 0
        if self.rolls[0] == "X":
            score += 10
            if self.next_frame:
                if self.next_frame.rolls[0] == "X":
                    if self.next_frame.next_frame:
                        score += 10 + (10 if self.next_frame.next_frame.rolls[0] == "X" else int(self.next_frame.next_frame.rolls[0]))
                elif self.next_frame.rolls[1] == "/":
                    score += 10
                else:
                    score += self.next_frame.score
        elif self.rolls[1] == "/":
            score += 10
            if self.next_frame:
                score += 10 if self.next_frame.rolls[0] == "X" else int(self.next_frame.rolls[0])
        else:
            score += int(self.rolls[0]) + int(self.rolls[1])
        return score

    def __str__(self):
        return str(self.rolls)


def get_frames(data):
    frames_obj = []
    i = 0
    while i < len(data):
        if data[i] == "X":
            frames_obj.append(Frame(("X",)))
            i += 1
        else:
            if i + 1 >= len(data):
                frames_obj.append(Frame((data[i:])))
            else:
                frames_obj.append(Frame((data[i], data[i+1])))
            i += 2

        if len(frames_obj) > 1:
            frames_obj[-2].next_frame = frames_obj[-1]

    return frames_obj


line = input()
while line != "Game Over":
    rolls = line.split()
    score = 0
    frames = get_frames(rolls)
    for i, frame in enumerate(frames):
        if i < 10:
            score += frame.score
    print(score)
    line = input()