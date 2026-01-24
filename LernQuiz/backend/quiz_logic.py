from typing import runtime_checkable
from string import ascii_lowercase
import random
import pathlib
from pathlib import Path
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

def erlauterung_abfragen():
    antwort = input("Erklärung? JA/NEIN").string().lower()
    return 1 if antwort == "ja" else 0


def Fragen_anzahl(): #
    while True:
        Nummer = input("Anzahl der Fragen?")

        if Nummer.isdigit():
            return int(Nummer)
        else:
            print("Bitte gebe eine valide Zahl an!")



def das_quiz():
    QUESTIONS_PATH = pathlib.Path(__file__).parent / "fragen.toml"

    # vorbereitung
    NUM_QUESTIONS_PER_QUIZ = Fragen_anzahl()
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ
    )
    #erlauterung_abfragen()

    # haupteil
    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nFrage {num}:")
        num_correct += ask_question(question)

    # Ende
    print(f"\nDu hast {num_correct} von {num} Fragen richtig.")


def prepare_questions(path, num_questions, topic_label):
    path = Path(path)
    topic_info = tomllib.loads(path.read_text())
    topics = {topic["label"]: topic["questions"] for topic in topic_info.values()}



    questions = topics[topic_label]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)

def ask_question(question):
    correct_answer = question["answer"]
    alternatives = [question["answer"]] + question["alternatives"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(
        question=question["question"],
        alternatives=ordered_alternatives,
    )

    if correct := (set(answer) == set(correct_answer)):
        print("Richtig!")

    else:
        print(f"Die Antwort ist {correct_answer!r}, nicht {answer!r}")

    if "explanation" in question:
        print(f"\nErklärung:\n{question['explanation']}")

    return 1 if correct else 0

def get_answer(question, alternatives):
    print(f"{question}")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternatives in labeled_alternatives.items():
        print(f"  {label}) {alternatives}")

    while (answer_label := input("\nAntwort? ")) not in labeled_alternatives:
        print(f"Bitte wähle aus von {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

if __name__ == "__main__":
    das_quiz()
