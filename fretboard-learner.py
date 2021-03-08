import random
import time

notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
random.seed()

def main():
    print("###################################")
    print("## Welcome to Fretboard Trainer! ##")
    print("###################################")
    print("Press c if you got it correct and w for wrong")
    print("Type q to quit")
    correct = 0
    correctTime = 0.
    wrongTime = 0.
    wrong = 0
    response = ""
    print("----------------------------------")
    while response != "q":
        randomNote = notes[random.randint(0, len(notes) - 1)]
        print("Play: " + randomNote)
        start = time.time()
        response = input()
        end = time.time()
        if response == "c":
            correctTime = end - start
            correct = correct + 1
        else:
            wrongTime = end - start
            wrong = wrong + 1
        print("----------------------------------")
    print("Final result: ")
    print("Correct: " + str(correct) + ", avg response time: " + str(round(correctTime / correct, 5)) + " s")
    print("Wrong: " + str(wrong) + ", avg response time: " + str(round(wrongTime / wrong, 5)) + " s")


if __name__ == "__main__":
    main()
