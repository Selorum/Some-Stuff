import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import random
from backend.quiz_logic import prepare_questions  #bestehende Funktion

class QuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz GUI")
        self.questions = []
        self.q_index = 0

        # Start-Frame
        self.start_frame = tk.Frame(root, padx=20, pady=20)
        self.start_frame.pack()

        tk.Label(self.start_frame, text="Willkommen zum Quiz!").pack(pady=10)
        tk.Button(self.start_frame, text="Quiz starten", command=self.show_topic_choice).pack()

    # Schritt 1: Themenwahl
    def show_topic_choice(self):
        self.start_frame.destroy()
        self.topic_frame = tk.Frame(self.root, padx=20, pady=20)
        self.topic_frame.pack()

        # TOML laden, nur Labels für Themen holen
        QUESTIONS_PATH = Path(__file__).parent.parent / "backend" / "fragen.toml"
        self.path = QUESTIONS_PATH

        import tomllib
        topic_info = tomllib.loads(QUESTIONS_PATH.read_text())
        self.topic_labels = sorted([t["label"] for t in topic_info.values()])

        tk.Label(self.topic_frame, text="Wähle ein Thema:").pack(pady=5)
        self.topic_var = tk.StringVar()
        self.topic_var.set(self.topic_labels[0])

        for topic in self.topic_labels:
            tk.Radiobutton(self.topic_frame, text=topic, variable=self.topic_var, value=topic).pack(anchor="w")

        tk.Button(self.topic_frame, text="Weiter", command=self.ask_num_questions).pack(pady=10)

    # Schritt 2: Anzahl der Fragen
    def ask_num_questions(self):
        self.topic_frame.destroy()
        self.num_frame = tk.Frame(self.root, padx=20, pady=20)
        self.num_frame.pack()

        tk.Label(self.num_frame, text="Anzahl der Fragen:").pack(pady=5)
        self.num_entry = tk.Entry(self.num_frame)
        self.num_entry.pack(pady=5)
        tk.Button(self.num_frame, text="OK", command=self.start_quiz).pack(pady=10)

    # Schritt 3: Quiz starten
    def start_quiz(self):
        try:
            num_questions = int(self.num_entry.get())
        except ValueError:
            messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben!")
            return

        self.num_frame.destroy()
        # prepare_questions aus Backend aufrufen
        selecte_topic = self.topic_var.get()
        self.questions = prepare_questions(self.path, num_questions, selecte_topic)
        # Filter nach gewähltem Thema
        self.questions = [q for q in self.questions if q in self.questions and q in self.questions]
        self.q_index = 0
        self.show_question()

    # Schritt 4: Frage anzeigen
    def show_question(self):
        if hasattr(self, 'q_frame'):
            self.q_frame.destroy()

        self.q_frame = tk.Frame(self.root, padx=20, pady=20)
        self.q_frame.pack()

        q = self.questions[self.q_index]
        self.current_question = q

        tk.Label(self.q_frame, text=q["question"], wraplength=400, font=("Arial", 12)).pack(pady=10)

        # Antworten mischen
        self.ordered_alternatives = random.sample([q["answer"]] + q["alternatives"], k=len(q["alternatives"])+1)

        self.answer_var = tk.StringVar()
        for ans in self.ordered_alternatives:
            tk.Radiobutton(self.q_frame, text=ans, variable=self.answer_var, value=ans).pack(anchor="w")

        tk.Button(self.q_frame, text="Antwort prüfen", command=self.check_answer).pack(pady=5)
        tk.Button(self.q_frame, text="Nächste Frage", command=self.next_question).pack(pady=5)

        self.feedback_label = tk.Label(self.q_frame, text="", fg="green")
        self.feedback_label.pack(pady=5)

    # Schritt 5: Antwort prüfen
    def check_answer(self):
        correct = self.answer_var.get() == self.current_question["answer"]
        if correct:
            self.feedback_label.config(text="✔ Richtig!", fg="green")
        else:
            self.feedback_label.config(
                text=f"✘ Falsch! Richtige Antwort: {self.current_question['answer']}",
                fg="red"
            )

        # Erklärung anzeigen, falls vorhanden
        if "explanation" in self.current_question:
            messagebox.showinfo("Erklärung", self.current_question["explanation"])

    # Schritt 6: Nächste Frage
    def next_question(self):
        self.q_index += 1
        if self.q_index < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Ende", "Alle Fragen beantwortet!")
            self.q_frame.destroy()
            self.__init__(self.root)  # GUI zurück zum Start

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGUI(root)
    root.mainloop()
