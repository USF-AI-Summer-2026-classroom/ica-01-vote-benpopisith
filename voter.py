class Voter:

    def __init__(self, id, leaning):
        self.id = id
        self.leaning = leaning
        self.ranked_votes = []

    def __repr__(self):
        return (
            f"Voter with ID={self.id}, "
            f"leaning: {self.leaning:.3f}"
        )
    
    def rank_candidates(self, candidates):
        ranked_candidates = []
        for candidate in candidates:
            abs_dist = abs(self.leaning - candidate.leaning)
            candidate_tuple = (abs_dist, candidate)
            ranked_candidates.append(candidate_tuple)
        self.ranked_votes = sorted(ranked_candidates)
        


