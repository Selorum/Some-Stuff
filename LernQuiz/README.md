LernQuiz

!Attention the for now there only exists the german version! 
!englisch will follow soon!

I used a realpython guide for most of the backend
Created by Selorum 

This project is a simple quiz application written in Python.
It uses Tkinter for the graphical user interface (GUI) and TOML files to store questions.


The quiz allows users to:

choose a topic

choose how many questions they want to answer

answer multiple-choice questions

receive feedback and explanations

The project is structured so that backend logic and GUI are clearly separated.

 Project Structure
project/
│
├── backend/
│   ├── quiz_logic.py      # Quiz logic (loading questions, evaluation)
│   └── fragen.toml        # Questions stored in TOML format
│
├── gui/
│   └── quiz_gui.py        # Tkinter GUI (frontend)
│
└── README.md

Requirements:

Python 3.11+ (recommended, because tomllib is built-in)

No external libraries required

Tkinter is included in standard Python installations

Questions are stored in fragen.toml  
they follow this structure (further explanation in the file)
[python]
label = "Python"

[[python.questions]]
question = "What keyword is used to define a function in Python?"
answer = "def"
alternatives = ["func", "function", "define"]
hint = "It's only three letters long."
explanation = """
The keyword 'def' is used to define a function in Python.
"""



To run use the given structure and run 
python gui/quiz_gui.py after you uploaded your questions in the toml file 

The split of front and backend makes it easyer to maintain and extende the code

Backend (quiz_logic.py)
Handles loading questions, selecting topics, and evaluating answers
→ no GUI code, no user input via input()

Frontend (quiz_gui.py)
Handles all user interaction using Tkinter
→ passes all user choices to the backend
