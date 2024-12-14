def main():
    """
    Main function to initialize and run the voting system.
    """
    print('Welcome to the Voting System!')

    # Optionally, customize the candidates here
    candidates = ['John', 'Jane', 'Alice', 'Bob']

    # Initialize the voting system with the given candidates
    voting_system = VotingSystem(candidates)

    # Run the voting system
    voting_system.run()

    print('Thank you for using the Voting System!')


if __name__ == "__main__":
    main()