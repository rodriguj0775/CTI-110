#Jose Rodriguez
 # November 13, 2026
 # LLM_LAB1
 # Solo Leveling - Shadow Monarch Quiz
 #The program will ask the user 5 questions about the Solo Leveling Anime by entering A, B, C, or D. 
 # The program will then calculate the score and display the user's rank based on their performance. 
 # The program will also include ASCII art.


# SOLO LEVELING - SHADOW MONARCH QUIZ
# Python Quiz Game with ASCII Art

def show_intro():
    print(r"""
    =========================================
          S O L O   L E V E L I N G
    =========================================

                /\     /\
               /  \___/  \
              |  O     O  |
              |     ^     |
               \  _____  /
                |  ___  |
             ___| |   | |___
            /    /     \    \
           /____/       \____\

             SHADOW MONARCH
                SUNG JINWOO

    =========================================
         [ SYSTEM ACTIVATED ]
         WELCOME, HUNTER!
    =========================================
    """)


def show_victory():
    print(r"""
          * * * LEVEL UP! * * *

             \   |   /
              \  |  /
           ----  *  ----
              /  |  \
             /   |   \

          QUEST COMPLETED!
    """)


def show_defeat():
    print(r"""
          [ QUEST FAILED ]

              _______
             /       \
            |  X   X  |
            |    _    |
             \_______/

          TRAIN HARDER, HUNTER!
    """)


def play_quiz():
    questions = [
        {
            "question": "Who is the main character of Solo Leveling?",
            "options": [
                "A. Naruto",
                "B. Sung Jinwoo",
                "C. Goku",
                "D. Gojo"
            ],
            "answer": "B"
        },
        {
            "question": "What was Jinwoo's original hunter rank?",
            "options": [
                "A. S-Rank",
                "B. A-Rank",
                "C. E-Rank",
                "D. B-Rank"
            ],
            "answer": "C"
        },
        {
            "question": "What is Jinwoo's famous command?",
            "options": [
                "A. Arise",
                "B. Attack",
                "C. Transform",
                "D. Bankai"
            ],
            "answer": "A"
        },
        {
            "question": "What is the name of Jinwoo's ant shadow?",
            "options": [
                "A. Igris",
                "B. Beru",
                "C. Iron",
                "D. Tank"
            ],
            "answer": "B"
        },
        {
            "question": "What title does Jinwoo eventually receive?",
            "options": [
                "A. Fire Monarch",
                "B. Dragon King",
                "C. Shadow Monarch",
                "D. Ice Emperor"
            ],
            "answer": "C"
        }
    ]

    score = 0

    print("\n[SYSTEM] Your quest has begun!")
    print("[SYSTEM] Answer 5 questions to level up!")

    for number, item in enumerate(questions, start=1):
        print("\n" + "=" * 40)
        print("QUEST", number)
        print(item["question"])

        for option in item["options"]:
            print(option)

        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("[SYSTEM] Invalid choice. Try again!")

        if answer == item["answer"]:
            print("\n[ CORRECT! ] +20 XP")
            score += 20
        else:
            print("\n[ INCORRECT! ]")
            print("Correct answer:", item["answer"])

    print("\n=========================================")
    print("             QUEST RESULTS")
    print("=========================================")
    print("Total XP:", score, "/ 100")

    if score == 100:
        show_victory()
        print("HUNTER RANK: S")
        print("TITLE: SHADOW MONARCH")
    elif score >= 80:
        show_victory()
        print("HUNTER RANK: A")
    elif score >= 60:
        print("HUNTER RANK: B")
        print("Good work, Hunter!")
    elif score >= 40:
        print("HUNTER RANK: C")
        print("Keep training!")
    else:
        show_defeat()
        print("HUNTER RANK: E")


# Main program
show_intro()

while True:
    play_quiz()

    again = input("\nPlay again? (Y/N): ").strip().upper()

    if again != "Y":
        print("\n[SYSTEM] Logging out...")
        print("Farewell, Hunter!")
        break
