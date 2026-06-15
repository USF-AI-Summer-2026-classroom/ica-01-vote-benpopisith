class Voter:

    def __init__(self, id, leaning):
        self.id = id
        self.leaning = leaning

    def __repr__(self):
        return (
            f"Voter with ID={self.id}, "
            f"leaning: {self.leaning:.3f}"
        )

