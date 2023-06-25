from selenium.webdriver.common.by import By

from browser.driver_manager import driver
from models.problems_model import Problem
import pandas as pd
import os

# driver_path = os.path.join(os.path.dirname(__file__), "../browser/driver_manager.py")


# problem_set = driver.find_element(
#     By.XPATH, "//div[contains(@class,'menu-box')]//li[6]//a"
# )
# problems = driver.find_elements(By.XPATH, "//table[contains(@class,'problems')]//tr")
# highest_page_no = driver.find_elements(
#     By.XPATH, f"//span[contains(@class,'page-index')]//a"
# )


columns = [
    "Problem No",
    "Problem Category",
    "Problem Name",
    "Tags",
    "Difficulty",
    "Total solve",
]
# url = "https://codeforces.com/"

pages = 2
page_no_start = 1
page_no_end = pages + 1

each_page_problem_start_no = 2


# class ProblemScraper:
#     def __init__(self):
#         self.driver = self.create_driver()
#         self.columns = [
#             "Problem No",
#             "Problem Category",
#             "Problem Name",
#             "Tags",
#             "Difficulty",
#             "Total solve",
#         ]


def get_problems_details(row):
    problem = Problem(*row)
    contents = {}
    contents["Problem No"] = problem.problem_no
    contents["Problem Category"] = problem.problem_category
    contents["Problem Name"] = problem.problem_name
    contents["Tags"] = problem.tags
    contents["Difficulty"] = problem.difficulty
    contents["Total solve"] = problem.total_solve
    return contents


# def init():
#     options = Options()
#     options.add_argument("--incognito")
#     options.add_experimental_option("excludeSwitches", ["enable-logging"])
#     driver = webdriver.Chrome(
#         service=ChromeService(ChromeDriverManager().install()), options=options
#     )
#     driver.get(url)
#     return driver


def exit():
    driver.quit()


def split_string(prb_no_category):
    if not str(prb_no_category[-1]).isdigit():
        prb_no = str(prb_no_category[:-1])
        prb_category = str(prb_no_category[-1])
    else:
        prb_no = str(prb_no_category[:-2])
        prb_category = str(prb_no_category[-2:])
    return prb_no, prb_category


def click_on_problem_set_menu():
    problem_set = driver.find_element(
        By.XPATH, "//div[contains(@class,'menu-box')]//li[6]//a"
    )
    problem_set.click()


def get_prb_no_and_category(j):
    prb_no_and_category = driver.find_element(
        By.XPATH,
        f"//table[contains(@class,'problems')]//tr[{j}]//td[contains(@class,'id')]",
    ).text
    return split_string(prb_no_and_category)


def get_prb_name_and_tags(j):
    if j % 2 == 0:
        prb_name = driver.find_element(
            By.XPATH,
            f"//table[contains(@class,'problems')]//tr[{j}]//td[contains(@class,'dark')]//div[1]//a",
        ).text
        prb_tags = driver.find_elements(
            By.XPATH,
            f"//table[contains(@class,'problems')]//tr[{j}]//td[contains(@class,'dark')]//div[2]//a",
        )
    else:
        prb_name = driver.find_element(
            By.XPATH,
            f"//table[contains(@class,'problems')]//tr[{j}]//td[2]//div[1]//a",
        ).text
        prb_tags = driver.find_elements(
            By.XPATH,
            f"//table[contains(@class,'problems')]//tr[{j}]//td[2]//div[2]//a",
        )
    if len(prb_tags) == 0:
        prb_tags = ""
    return prb_name, prb_tags


def store_prb_tags(prb_tags):
    store_tag = []
    for k in range(len(prb_tags)):
        store_tag.append(prb_tags[k].text)
    return store_tag


def get_prb_difficulty(j):
    difficulty = driver.find_element(
        By.XPATH, f"//table[contains(@class,'problems')]//tr[{j}]//td[4]"
    ).text
    if len(difficulty) == 0:
        difficulty = ""
    else:
        difficulty = driver.find_element(
            By.XPATH,
            f"//table[contains(@class,'problems')]//tr[{j}]//td[4]//span[contains(@class,'ProblemRating')]",
        ).text
    return difficulty


def get_prb_solve_cnt(j):
    try:
        solves = driver.find_element(
            By.XPATH,
            f"//table[contains(@class,'problems')]//tr[{j}]//td[contains(@class,'right')]//a",
        ).text
        solves = solves[2:]
    except Exception:
        solves = ""
    return solves


def click_next_page(i):
    return driver.find_element(
        By.XPATH,
        f"//div[contains(@class,'pagination')]//ul//span[contains(@class,'page-index')]//a[text()='{i+1}']",
    ).click()


def save_prb_details_as_dataset(problems_details):
    df = pd.DataFrame(data=problems_details, columns=columns)
    df.to_csv("cf_problem_details1.csv", index=False)


def get_total_problem_in_each_page():
    problems = driver.find_elements(
        By.XPATH, "//table[contains(@class,'problems')]//tr"
    )
    return len(problems) + 1


def get_highest_page_no():
    highest_page_no = driver.find_elements(
        By.XPATH, f"//span[contains(@class,'page-index')]//a"
    )
    return max(
        [int(highest_page_no[page_no].text) for page_no in range(len(highest_page_no))]
    )


def fetch_problem_details():
    problems_details = []
    total_pages = get_highest_page_no()

    for i in range(page_no_start, page_no_end):
        each_page_problem_end_no = get_total_problem_in_each_page()

        for j in range(each_page_problem_start_no, each_page_problem_end_no):
            prb_no, prb_category = get_prb_no_and_category(j)
            prb_name, prb_tags = get_prb_name_and_tags(j)
            store_tags = store_prb_tags(prb_tags)
            difficulty = get_prb_difficulty(j)
            total_solve_cnt = get_prb_solve_cnt(j)

            data = [
                prb_no,
                prb_category,
                prb_name,
                store_tags,
                difficulty,
                total_solve_cnt,
            ]
            problems_details.append(get_problems_details(data))

        click_next_page(i)
    return problems_details
