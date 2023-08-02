import pages.problem_set_page as problem_set_page


def main():
    problem_set_page.click_on_problem_set_menu()
    problems_details = problem_set_page.fetch_problem_details()
    problem_set_page.exit()
    problem_set_page.save_prb_details_as_dataset(problems_details)
    return


if __name__ == "__main__":
    main()
