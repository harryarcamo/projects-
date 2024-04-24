import random

words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "of"},
    {"spanish": "que", "english": "that"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to"},
    {"spanish": "en", "english": "in"},
    {"spanish": "un", "english": "a"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "reflexive pronoun"},
    {"spanish": "no", "english": "no"},
    {"spanish": "haber", "english": "to have"},
    {"spanish": "por", "english": "for"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his, her, its, your "},
    {"spanish": "para", "english": "for"},
    {"spanish": "como", "english": "like, as"},
    {"spanish": "estar", "english": "to be "},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "le", "english": "indirect object pronoun"},
    {"spanish": "lo", "english": "it, him, you, the "},
    {"spanish": "todo", "english": "all"},
    {"spanish": "pero", "english": "but"},
    {"spanish": "más", "english": "more"},
    {"spanish": "hacer", "english": "to do, to make"},
    {"spanish": "o", "english": "or"},
    {"spanish": "poder", "english": "to be able to, can"},
    {"spanish": "decir", "english": "to say, to tell"},
    {"spanish": "este", "english": "this"},
    {"spanish": "ir", "english": "to go"},
    {"spanish": "otro", "english": "other"},
    {"spanish": "ese", "english": "that"},
    {"spanish": "la", "english": "the"},
    {"spanish": "si", "english": "if"},
    {"spanish": "me", "english": "me"},
    {"spanish": "ya", "english": "already"},
    {"spanish": "ver", "english": "to see"},
    {"spanish": "porque", "english": "because"},
    {"spanish": "dar", "english": "to give"},
    {"spanish": "cuando", "english": "when"},
    {"spanish": "él", "english": "he"},
    {"spanish": "muy", "english": "very"},
    {"spanish": "sin", "english": "without"},
    {"spanish": "vez", "english": "time"},
    {"spanish": "mucho", "english": "much, a lot"},
    {"spanish": "saber", "english": "to know"},
    {"spanish": "qué", "english": "what"},
    {"spanish": "sobre", "english": "about, on"},
    {"spanish": "mi", "english": "my"},
    {"spanish": "alguno", "english": "some, any"},
    {"spanish": "mismo", "english": "same"},
    {"spanish": "yo", "english": "I"},
    {"spanish": "también", "english": "also"},
    {"spanish": "hasta", "english": "until, up to"},
    {"spanish": "año", "english": "year"},
    {"spanish": "dos", "english": "two"},
    {"spanish": "querer", "english": "to want"},
    {"spanish": "entre", "english": "between, among"},
    {"spanish": "así", "english": "thus, so"},
    {"spanish": "primero", "english": "first"},
    {"spanish": "desde", "english": "from, since"},
    {"spanish": "grande", "english": "big, large"},
    {"spanish": "eso", "english": "that"},
    {"spanish": "ni", "english": "neither, nor"},
    {"spanish": "nos", "english": "us"},
    {"spanish": "parte", "english": "part"},
    {"spanish": "bien", "english": "well"},
    {"spanish": "poco", "english": "little, few"},
    {"spanish": "llegar", "english": "to arrive, to come"},
    {"spanish": "menos", "english": "less"},
    {"spanish": "pasar", "english": "to pass, to happen"},
    {"spanish": "tiempo", "english": "time"},
    {"spanish": "ella", "english": "she"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "día", "english": "day"},
    {"spanish": "uno", "english": "one"},
    {"spanish": "bajo", "english": "low, under"},
    {"spanish": "todo", "english": "everything"},
    {"spanish": "cada", "english": "each, every"},
    {"spanish": "otra", "english": "other, another"},
    {"spanish": "eso", "english": "that"},
    {"spanish": "decir", "english": "to say, to tell"},
    {"spanish": "ella", "english": "she"},
    {"spanish": "tanto", "english": "so much, so many"},
    {"spanish": "él", "english": "he"},
    {"spanish": "ese", "english": "that"},
    {"spanish": "esto", "english": "this"},
    {"spanish": "mujer", "english": "woman"},
    {"spanish": "vida", "english": "life"},
    {"spanish": "él", "english": "he"},
    {"spanish": "nada", "english": "nothing"}, 
    {"spanish": "pues", "english": "well, then"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "tener", "english": "to have"},

]



def quiz_user(words):
    """Quiz the user with words."""
    random.shuffle(words)  # Shuffle the list of words
    score = 0 

    for word in words:
        print(f"What is the English translation of '{word['spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")
            score -= 1

    return score  # Return the score after all words are quizzed

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    final_score = quiz_user(words)  # Get the final score from the quiz_user function
    print(f"Quiz complete! Your score: {final_score}/{len(words)}")

if __name__ == "__main__":
    main()


