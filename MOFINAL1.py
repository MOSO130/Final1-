class VotingSystem:
    """
    A system to manage voting for candidates.
    """

    def __init__(self):
        """
        Initializes the voting system with zero votes for each candidate.
        """
        self.votes = {'John': 0, 'Jane': 0}

    def vote_menu(self) -> str:
        """
        Displays the voting menu and validates the user's input.

        Returns:
            str: 'v' for vote or 'x' for exit.
        """
        while True:
            print('--------------------')
            print('VOTE MENU')
            print('--------------------')
            print('v: Vote')
            print('x: Exit')
            option = input('Option: ').lower().strip()
            if option in ['v', 'x']:
                return option
            print('Invalid (v/x):', option)

    def candidate_menu(self) -> str:
        """
        Displays the candidate menu and validates the user's input.

        Returns:
            str: '1' for John or '2' for Jane.
        """
        while True:
            print('--------------------')
            print('CANDIDATE MENU')
            print('--------------------')
            print('1: John')
            print('2: Jane')
            candidate = input('Candidate: ').strip()
            if candidate in ['1', '2']:
                return candidate
            print('Invalid (1/2):', candidate)

    def record_vote(self, candidate: str):
        """
        Records a vote for the chosen candidate.

        Args:
            candidate (str): '1' for John or '2' for Jane.
        """
        if candidate == '1':
            self.votes['John'] += 1
            print('Voted John')
        elif candidate == '2':
            self.votes['Jane'] += 1
            print('Voted Jane')

    def display_results(self):
        """
        Displays the voting results.
        """
        print('--------------------')
        print(f"John - {self.votes['John']}, Jane - {self.votes['Jane']}, Total - {self.votes['John'] + self.votes['Jane']}")
        print('--------------------')

    def run(self):
        """
        Executes the voting system.
        """
        while True:
            option = self.vote_menu()
            if option == 'v':
                candidate = self.candidate_menu()
                self.record_vote(candidate)
            elif option == 'x':
                break
        self.display_results()


if __name__ == "__main__":
    voting_system = VotingSystem()
    voting_system.run()