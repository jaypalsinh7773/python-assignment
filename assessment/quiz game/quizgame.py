class QuizGame:
    def __init__(self):
        self.questions = {} 

    def master_menu(self):
        while True:
            print("\n--- Quiz Master Menu ---")
            print("1. Add Question")
            print("2. View Questions")
            print("3. Delete Question")
            print("4. Back to Main Menu")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_question()
            elif choice == "2":
                self.view_questions()
            elif choice == "3":
                self.delete_question()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please choose 1–4.")

    def add_question(self):
        qid = input("Enter Question ID: ").strip()
        if not qid or qid in self.questions:
            print("ID empty or already exists.")
            return
        qtext = input("Enter the question text: ").strip()
        opts = {}
        for opt in ["A","B","C","D"]:
            opts[opt] = input(f"Option {opt}: ").strip()
        ans = input("Correct answer (A–D): ").upper().strip()
        if ans not in opts:
            print("Invalid correct answer. Must be A–D.")
        else:
            self.questions[qid] = {"question":qtext, "options":opts, "answer":ans}
            print("Question added!")

    def view_questions(self):
        if not self.questions:
            print("No questions available.")
            return
        for qid, q in self.questions.items():
            print(f"\nID: {qid}\n  {q['question']}")
            for o,v in q["options"].items():
                print(f"   {o}. {v}")
            print(f"  Answer: {q['answer']}")

    def delete_question(self):
        qid = input("Enter ID to delete: ").strip()
        if qid in self.questions:
            if input("Sure? (Y/N): ").upper().strip() == "Y":
                del self.questions[qid]
                print("Question deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("ID not found.")

    def cracker_menu(self):
        if not self.questions:
            print("No questions—ask Quiz Master to add first.")
            return
        score = 0
        total = len(self.questions)
        for qid, q in self.questions.items():
            print(f"\nQuestion: {q['question']}")
            for o,v in q["options"].items():
                print(f" {o}. {v}")
                
            while True:
                ans = input("Your answer (A–D): ").upper().strip()
                try:
                    if ans not in ["A","B","C","D"]:
                        raise ValueError("Answer must be one of A, B, C, D.")
                    break
                except ValueError as e:
                    print(f" {e}")
            if ans == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct is {q['answer']}")
        print(f"\nYou scored {score}/{total}!")

    def main_menu(self):
        while True:
            print("\n===== Quiz Game =====")
            print("1. Quiz Master (manage questions)")
            print("2. Quiz Cracker (take quiz)")
            print("3. Exit")
            choice = input("Select option: ")
            try:
                if choice not in ["1","2","3"]:
                    raise ValueError("Please enter 1, 2, or 3.")
            except ValueError as e:
                print(e)
                continue

            if choice == "1":
                self.master_menu()
            elif choice == "2":
                self.cracker_menu()
            else:
                print("Goodbye!")
                break

game = QuizGame()
game.main_menu()
