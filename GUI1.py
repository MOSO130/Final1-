import tkinter as tk
from tkinter import messagebox


class VotingSystemGUI:
    """
    A GUI-based voting system to manage votes for candidates.
    """

    def __init__(self, root):
        """
        Initializes the voting system and GUI components.
        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("Voting System")

        # Candidates and their votes
        self.votes = {"John": 0, "Jane": 0}

        # Title Label
        tk.Label(root, text="Voting System", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Buttons for Voting
        tk.Button(root, text="Vote for John", command=lambda: self.record_vote("John"), font=("Helvetica", 12)).pack(
            pady=5)
        tk.Button(root, text="Vote for Jane", command=lambda: self.record_vote("Jane"), font=("Helvetica", 12)).pack(
            pady=5)

        # Show Results Button
        tk.Button(root, text="Show Results", command=self.display_results, font=("Helvetica", 12)).pack(pady=5)

        # Exit Button
        tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 12)).pack(pady=5)

    def record_vote(self, candidate):
        """
        Records a vote for the chosen candidate.
        Args:
            candidate (str): Name of the candidate.
        """
        self.votes[candidate] += 1
        messagebox.showinfo("Vote Recorded", f"You voted for {candidate}!")

    def display_results(self):
        """
        Displays the voting results in a popup window.
        """
        results = "\n".join([f"{candidate}: {votes}" for candidate, votes in self.votes.items()])
        total_votes = sum(self.votes.values())
        results += f"\nTotal Votes: {total_votes}"
        messagebox.showinfo("Voting Results", results)


if __name__ == "__main__":
    root = tk.Tk()
    app = VotingSystemGUI(root)
    root.mainloop()