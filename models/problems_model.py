class Problem:
    def __init__(self, problem_no, problem_category, problem_name, tags, difficulty, total_solve):
        self.problem_no = problem_no
        self.problem_category = problem_category
        self.problem_name = problem_name
        self.tags = tags
        self.difficulty = difficulty
        self.total_solve = total_solve

    def __repr__(self):
        return f"Problem(problem_no={self.problem_no}, problem_category={self.problem_category}, " \
               f"problem_name={self.problem_name}, tags={self.tags}, difficulty={self.difficulty}, " \
               f"total_solve={self.total_solve})"
