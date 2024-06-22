import tkinter as tk
from tkinter import ttk, messagebox
import random
import csv
import os

flashcards = {
    "English": {
        "Easy": [{
            "Phrase": "HAPPY 😊",
            "Meaning": "Feeling or showing pleasure or contentment.",
            "Sentence": "He is happy today."
        }, {
            "Phrase": "SAD 😔",
            "Meaning": "Feeling of showing disappointment.",
            "Sentence": "I am very sad."
        }, {
            "Phrase": "ANGRY 😠",
            "Meaning":
            "Feeling or expressing strong displeasure, annoyance, or hostility.",
            "Sentence": "She slammed the door, her face twisted in anger."
        }, {
            "Phrase":
            "TIRED 😫",
            "Meaning":
            "Feeling exhausted or fatigued, often accompanied by a lack of energy or weariness.",
            "Sentence":
            "After a long day at work, she felt incredibly tired and just wanted to rest."
        }, {
            "Phrase":
            "AFRAID 😨",
            "Meaning":
            "Feeling of being scared or anxious about a potential threat or danger.",
            "Sentence":
            "She was afraid of the dark and always slept with a nightlight."
        }],
        "Moderate": [{
            "Phrase":
            "RESILIENT",
            "Meaning":
            "Able to recover quickly from difficult conditions.",
            "Sentence":
            "George Fraser was clearly a good soldier, calm and resilient."
        }, {
            "Phrase":
            "CONUNDRUM",
            "Meaning":
            "A confusing and difficult problem or question.",
            "Sentence":
            "The conundrum of the missing link was solved."
        }, {
            "Phrase":
            "PROLIFIC",
            "Meaning":
            "Producing a large amount of something.",
            "Sentence":
            "She is a prolific writer of novels and short stories."
        }, {
            "Phrase":
            "PRAGMATIC",
            "Meaning":
            "Dealing with things sensibly and realistically.",
            "Sentence":
            "That it was a pragmatic approach designed to allow him to escape with his reputation intact."
        }, {
            "Phrase":
            "AMBIGUOUS",
            "Meaning":
            "Open to more than one interpretation; having a double meaning.",
            "Sentence":
            "The instructions provided were ambiguous, leaving the team unsure about the next steps to take in the project."
        }],
        "Intermediate": [{
            "Phrase":
            "Hit the nail on the head",
            "Meaning":
            "To describe exactly what is causing a situation or problem.",
            "Sentence":
            "When discussing the project, Sarah hit the nail on the head by identifying the exact issue that was causing delays."
        }, {
            "Phrase":
            "Bite the bullet",
            "Meaning":
            "To endure a painful or difficult situation with courage.",
            "Sentence":
            "Despite his fear, Tom knew he had to bite the bullet and confront his boss about the mistake."
        }, {
            "Phrase":
            "Jump on the bandwagon",
            "Meaning":
            "To join or support something that has become fashionable or popular.",
            "Sentence":
            "After the team won the championship, many fans jumped on the bandwagon and started supporting them."
        }, {
            "Phrase":
            "The ball is in your court.",
            "Meaning":
            "It's your turn to make a decision or take action.",
            "Sentence":
            "I have given you all the information you need to make a decision; now the ball is in your court."
        }, {
            "Phrase":
            "Under the weather",
            "Meaning":
            "Feeling ill or unwell",
            "Sentence":
            "I won't be able to come to work today; I'm feeling a bit under the weather."
        }]
    },
    "Japanese": {
        "Easy": [{
            "Phrase": "KONNICHIWA",
            "Meaning": "Hello",
            "Sentence": "Konnichiwa, genki desu ka?"
        }, {
            "Phrase": "OHAYOU GOZAIMASU",
            "Meaning": "Good Morning",
            "Sentence": "Ohayou Gozaimasu, kaizoku-tachi no ka?"
        }, {
            "Phrase": "KONBANWA",
            "Meaning": "Good Evening",
            "Sentence": "Konbanwa, oishii tabemono o tabetai desu."
        }, {
            "Phrase": "YOROSHIKU ONEGAISHIMASU",
            "Meaning": "Yoroshiku onegaishimasu",
            "Sentence": "Ashita no kaigi de, yoroshiku onegaishimasu."
        }, {
            "Phrase": "SOYOUNARA",
            "Meaning": "Goodbye",
            "Sentence": "Sayounara, kaizoku-tachi no ka?"
        }],
        "Moderate": [{
            "Phrase": "IE",
            "Meaning": "House",
            "Sentence": "Watashi no ie wa ookikute shizuka desu."
        }, {
            "Phrase": "GAKKOU",
            "Meaning": "School",
            "Sentence": "Watashi no gakkou wa chikaku ni arimasu."
        }, {
            "Phrase": "BYOUIN",
            "Meaning": "Hospital",
            "Sentence": "Kanojo wa byouin de hataraiteimasu."
        }, {
            "Phrase": "EKI",
            "Meaning": "Station",
            "Sentence": "Eki made aruite ikemasu ka?"
        }, {
            "Phrase": "KUUKOU",
            "Meaning": "Airport",
            "Sentence": "Kuukou de tomodachi o demukaemasu."
        }],
        "Intermediate": [{
            "Phrase": "YASASHII",
            "Meaning": "Kind",
            "Sentence": "Kare wa totemo yasashii hito desu."
        }, {
            "Phrase":
            "TAISETSU",
            "Meaning":
            "Important",
            "Sentence":
            "Kazoku to no jikan wa watashi ni totte totemo taisetsu desu."
        }, {
            "Phrase":
            "SEIKOU",
            "Meaning":
            "Success",
            "Sentence":
            "Kanojo wa doryoku no sue ni seikou shimashita."
        }, {
            "Phrase":
            "KANDOU",
            "Meaning":
            "Touching/Moving",
            "Sentence":
            "Sono eiga wa watashi o fukaku kandou sasemashita."
        }, {
            "Phrase": "MUZUKASHII",
            "Meaning": "Difficult",
            "Sentence": "Kono mondai wa totemo muzukashii desu."
        }]
    }
}

quiz_questions = {
    "English": [{
        "Question": "What is the meaning of 'Happy'?",
        "Options": ["Excited", "Sad", "Content"],
        "Answer": "Content"
    }, {
        "Question": "What is the meaning of 'Resilient'?",
        "Options": ["Weak", "Strong", "Flexible"],
        "Answer": "Flexible"
    }, {
        "Question": "What is the meaning of 'Bite the bullet'?",
        "Options": ["Avoiding", "Endure", "Bite"],
        "Answer": "Endure"
    }, {
        "Question": "What is the meaning of 'Jump on the bandwagon'?",
        "Options": ["Join", "Lead", "Avoid"],
        "Answer": "Join"
    }, {
        "Question": "What is the meaning of 'Hit the nail on the head'?",
        "Options": ["Understand", "Miss", "Accurate"],
        "Answer": "Accurate"
    }],
    "Japanese": [{
        "Question": "What is the meaning of 'Konnichiwa'?",
        "Options": ["Goodbye", "Hello", "Thank you"],
        "Answer": "Hello"
    }, {
        "Question": "What is the meaning of 'Byouin'?",
        "Options": ["School", "Hospital", "Restaurant"],
        "Answer": "Hospital"
    }, {
        "Question": "What is the meaning of 'Yasashii'?",
        "Options": ["Easy", "Difficult", "Kind"],
        "Answer": "Kind"
    }, {
        "Question": "What is the meaning of 'Seikou'?",
        "Options": ["Success", "Failure", "Luck"],
        "Answer": "Success"
    }, {
        "Question": "What is the meaning of 'Muzukashii'?",
        "Options": ["Simple", "Difficult", "Complex"],
        "Answer": "Difficult"
    }]
}


def show_flashcards(language, level):
    if language in flashcards and level in flashcards[language]:
        selected_flashcards = flashcards[language][level]
    else:
        messagebox.showerror(
            "Error",
            "No flashcards available for the selected language and level.")
        return

    flashcard_window = tk.Toplevel(root)
    flashcard_window.title(f"{language} - {level} Flashcards")

    flashcard_frame = tk.Frame(flashcard_window,
                               bg="#FFE033",
                               bd=2,
                               relief="solid",
                               highlightbackground="#d8b90d")
    flashcard_frame.pack(padx=20, pady=20)

    current_card_index = 0
    current_card = tk.StringVar()
    current_card.set(selected_flashcards[current_card_index]["Phrase"])

    def show_card():
        flashcard_label.config(text=current_card.get())

    def next_card():
        nonlocal current_card_index
        if current_card_index < len(selected_flashcards) - 1:
            current_card_index += 1
            current_card.set(selected_flashcards[current_card_index]["Phrase"])
            show_card()
        else:
            messagebox.showinfo(
                "Finished",
                "You have completed all flashcards for this level.")

    def previous_card():
        nonlocal current_card_index
        if current_card_index > 0:
            current_card_index -= 1
            current_card.set(selected_flashcards[current_card_index]["Phrase"])
            show_card()
        else:
            messagebox.showinfo("Start", "You are at the first flashcard.")

    def show_meaning():
        meaning = selected_flashcards[current_card_index].get(
            "Meaning", "Meaning not available.")
        messagebox.showinfo("Meaning", meaning)

    def show_sentence():
        sentence = selected_flashcards[current_card_index].get(
            "Sentence", "Sentence not available.")
        messagebox.showinfo("Sentence", sentence)

    flashcard_label = tk.Label(flashcard_frame,
                               textvariable=current_card,
                               font=("Arial", 24),
                               bg="#FF5E33",
                               padx=20,
                               pady=10,
                               borderwidth=4,
                               relief="groove")
    flashcard_label.pack(pady=20)

    button_frame = tk.Frame(flashcard_frame, bg="#FFE033")
    button_frame.pack(pady=(10, 0))

    meaning_button = tk.Button(button_frame,
                               text="Meaning",
                               command=show_meaning,
                               bg="#28a745",
                               fg="white",
                               relief="flat",
                               activebackground="#218838",
                               activeforeground="white",
                               padx=10,
                               pady=5)
    meaning_button.pack(side=tk.LEFT, padx=10)

    sentence_button = tk.Button(button_frame,
                                text="Sentence",
                                command=show_sentence,
                                bg="#007bff",
                                fg="white",
                                relief="flat",
                                activebackground="#0056b3",
                                activeforeground="white",
                                padx=10,
                                pady=5)
    sentence_button.pack(side=tk.LEFT, padx=10)

    back_button_frame = tk.Frame(flashcard_window)
    back_button_frame.pack(pady=10)

    back_button = tk.Button(back_button_frame,
                            text="Back",
                            command=previous_card,
                            font=("Arial", 14))
    back_button.pack(side=tk.BOTTOM, padx=10)

    next_button = tk.Button(flashcard_frame,
                            text="Next",
                            command=next_card,
                            font=("Arial", 14))
    next_button.pack(side=tk.BOTTOM, pady=10, padx=10)

    show_card()


def start_quiz():

    def start_quiz_game():
        username = quiz_name_entry.get()
        if username:
            quiz_name_window.withdraw()
            selected_questions = []
            for language in quiz_questions:
                selected_questions.extend(
                    random.sample(quiz_questions[language], 5))

            quiz_window = tk.Toplevel(root)
            quiz_window.title("Quiz")
            quiz_window.geometry("400x300")

            score = tk.IntVar()
            current_question_index = 0

            def show_question():
                question_label.config(
                    text=selected_questions[current_question_index]
                    ["Question"])
                # Clear previous options
                for widget in options_frame.winfo_children():
                    widget.destroy()

                # Dynamically create radio buttons for each option
                for i, option in enumerate(
                        selected_questions[current_question_index]["Options"]):
                    tk.Radiobutton(options_frame,
                                   text=option,
                                   variable=option_var,
                                   value=option,
                                   bg="#FFE033",
                                   font=("Arial", 12)).grid(row=0,
                                                            column=i,
                                                            padx=5)

            def check_answer():
                answer = selected_questions[current_question_index]["Answer"]
                selected_answer = option_var.get()
                if selected_answer == answer:
                    messagebox.showinfo("Correct", "Correct answer!")
                    score.set(score.get() + 2)
                else:
                    messagebox.showerror("Incorrect", "Incorrect answer!")

                next_question()

            def next_question():
                nonlocal current_question_index
                if current_question_index < len(selected_questions) - 1:
                    current_question_index += 1
                    show_question()
                else:
                    messagebox.showinfo("Quiz Completed",
                                        f"Your score: {score.get()}")
                    log_score(username, score.get())

            quiz_frame = tk.Frame(quiz_window)
            quiz_frame.pack(padx=20, pady=20)

            question_label = tk.Label(quiz_frame,
                                      font=("Arial", 14),
                                      wraplength=350)
            question_label.pack(pady=10)

            option_var = tk.StringVar()
            options_frame = tk.Frame(quiz_frame, bg="#FFE033")
            options_frame.pack(pady=10)

            submit_button = tk.Button(quiz_frame,
                                      text="Submit",
                                      command=check_answer,
                                      font=("Arial", 12))
            submit_button.pack(pady=10)

            show_question()

        else:
            messagebox.showerror("Error", "Please enter your name.")

    quiz_name_window = tk.Toplevel(root)
    quiz_name_window.title("Quiz - Enter Your Name")
    quiz_name_window.geometry("300x100")
    quiz_name_window.resizable(False, False)

    quiz_name_label = tk.Label(quiz_name_window,
                               text="Enter your name:",
                               font=("Arial", 12))
    quiz_name_label.pack(pady=5)

    quiz_name_entry = tk.Entry(quiz_name_window, font=("Arial", 12))
    quiz_name_entry.pack(pady=5)

    start_quiz_button = tk.Button(quiz_name_window,
                                  text="Start Quiz",
                                  command=start_quiz_game,
                                  font=("Arial", 12))
    start_quiz_button.pack(pady=5)


def log_score(username, score):
    with open('quiz_scores.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, score])


def view_scores():
    if os.path.exists('quiz_scores.csv'):
        with open('quiz_scores.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    else:
        messagebox.showerror("Error", "No scores available.")


root = tk.Tk()
root.title("Language Learning App")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

language_label = tk.Label(root,
                          text="Select Language:",
                          bg="#f0f0f0",
                          font=("Arial", 14))
language_label.pack(pady=10)

language_var = tk.StringVar(root)
language_menu = ttk.Combobox(root,
                             textvariable=language_var,
                             values=list(flashcards.keys()),
                             font=("Arial", 12),
                             state="readonly")
language_menu.pack()

level_label = tk.Label(root,
                       text="Select Level:",
                       bg="#f0f0f0",
                       font=("Arial", 14))
level_label.pack(pady=10)

level_var = tk.StringVar(root)
level_menu = ttk.Combobox(root,
                          textvariable=level_var,
                          values=["Easy", "Moderate", "Intermediate"],
                          font=("Arial", 12),
                          state="readonly")
level_menu.pack()

start_flashcards_button = tk.Button(
    root,
    text="Start Flashcards",
    command=lambda: show_flashcards(language_var.get(), level_var.get()),
    bg="#007bff",
    fg="white",
    relief="flat",
    activebackground="#0056b3",
    activeforeground="white",
    font=("Arial", 14))
start_flashcards_button.pack(pady=10)

start_quiz_button = tk.Button(root,
                              text="Start Quiz",
                              command=start_quiz,
                              bg="#dc3545",
                              fg="white",
                              relief="flat",
                              activebackground="#c82333",
                              activeforeground="white",
                              font=("Arial", 14))
start_quiz_button.pack(pady=10)

view_scores_button = tk.Button(root,
                               text="View Scores",
                               command=view_scores,
                               bg="#6c757d",
                               fg="white",
                               relief="flat",
                               activebackground="#5a6268",
                               activeforeground="white",
                               font=("Arial", 14))
view_scores_button.pack(pady=10)

root.mainloop()
