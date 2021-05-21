import random
import time

notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
random.seed()

def main():
    print("###################################")
    print("## Welcome to Fretboard Trainer! ##")
    print("###################################")
    print("Press enter to go to next note, type \"w\" if you want to track \"wrongs\"")
    print("Type q to quit")
    correct = 0
    correctTime = 0.
    wrongTime = 0.
    wrong = 0
    response = ""
    includeStrings = input("Do you want to include strings? (Y/n): ")
    rounds = input("Enter amount of rounds (leave blank for endless): ")
    if rounds != '':
        rounds = int(rounds)
    else:
        rounds = -1
    print("----------------------------------")
    while response != "q" and ((rounds == -1) or (rounds > (correct + wrong))):
        randomNote = notes[random.randint(0, len(notes) - 1)]
        randomString = random.randint(1, 6)
        if includeStrings == "n":
            print("Play: " + randomNote)
        else:
            print("Play: " + randomNote + " on string: " + str(randomString))
        start = time.time()
        response = input()
        end = time.time()
        if response == "w":
            wrongTime = wrongTime + (end - start)
            wrong = wrong + 1
        else:
            correctTime = correctTime + (end - start)
            correct = correct + 1
        print("----------------------------------")
    print("Final result: ")
    print("Correct: " + str(correct) + ", avg response time: " + str(round(correctTime / correct, 5) if correct else 0) + " s")
    print("Wrong: " + str(wrong) + ", avg response time: " + str(round(wrongTime / wrong, 5) if wrong else 0) + " s")
    response = input("Press any key to close")


if __name__ == "__main__":
    main()
