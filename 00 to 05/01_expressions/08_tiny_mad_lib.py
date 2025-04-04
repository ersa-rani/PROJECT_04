# Sentence beginning provided as a constant
SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "  # adjective noun verb

def main():
    # Prompt user for word inputs
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")

    # Combine and print the full sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# Required call to run the program
if __name__ == '__main__':
    main()
