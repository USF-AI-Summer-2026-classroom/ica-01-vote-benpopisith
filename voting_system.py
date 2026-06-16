from candidate import Candidate
from voter import Voter

import random


class VotingSystem:
    def __init__(self):
        self.candidates = []
        self.voters = []
        self.eliminated_candidates = []

    def generate_candidates(self, count):
        names = ['Aang', 'Katara', 'Sokka', 'Zuko', 'Iroh', 'Appa', 'Momo', 'Toph', 'Azula', 'Suki', 'Ozai', 'Mai', 'Ty']
        self.candidates = [
            Candidate(
                name=names[i],
                leaning=random.uniform(-1.0, 1.0)
            )
            for i in range(count)
        ]

    def generate_voters(self, count):
        self.voters = [
            Voter(
                id=i + 1,
                leaning=random.uniform(-1.0, 1.0)
            )
            for i in range(count)
        ]
    
    def generate_winner(self):
        # call rank_candidates for every voter
        for voter in self.voters:
            voter.rank_candidates(self.candidates)
        
        has_winner = False
        self.eliminated_candidates = []
        winner = ''
        round_count = 0

        while not has_winner:
            round_count += 1
            vote_count = {}
            print(f'Round {round_count}!')
            for voter in self.voters:
                for ranked_vote in voter.ranked_votes:
                    candidate = ranked_vote[1]
                    if candidate not in self.eliminated_candidates:
                        vote_count[candidate] = vote_count.get(candidate, 0) + 1
                        break
            
            for candidate ,votes in vote_count.items():
                percent_of_votes = 100 * (votes / (len(self.voters)))
                print(f"{candidate}, {percent_of_votes:.2f}%")
                if votes > .5 * (len(self.voters)):
                    has_winner = True
                    winner = candidate
            if not has_winner:
                least_voted = min(vote_count, key=vote_count.get)
                self.eliminated_candidates.append(least_voted)
        
        print(f'The winner is: {winner.name}')

            

if __name__ == "__main__":
    voting_system = VotingSystem()

    voting_system.generate_candidates(5)
    voting_system.generate_voters(100)

    print("Candidates:")
    for candidate in voting_system.candidates:
        print(candidate)

    print("\nVoters:")
    for voter in voting_system.voters:
        print(voter)

    voting_system.generate_winner()
