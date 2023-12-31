# CodeForces problemset data visualization and analysis

## Problem Statement

The goal of this project is to gather problemset information of [this website](https://codeforces.com/problemset).
Later we utilized the scraped data to understand the following demographics and correlations using Tableau Dashboard:

1. Category-wise average difficulty of the problems.
2. Total problem solve count according to the Problems Category.
3. Total solves in overall contest.
4. Category-wise total problems.
5. Category-wise Problems Tags and relation.
6. Tags-wise problems details.

To see the visualization and findings you can visit the public dashboard here[ [1-4](https://public.tableau.com/app/profile/md.tanvir.hossain/viz/CF_visualizer_1/visualization), 
[5](https://public.tableau.com/app/profile/md.tanvir.hossain/viz/CF_visualizer_2/Sheet3), [6](https://public.tableau.com/app/profile/md.tanvir.hossain/viz/CF_visualizer_3/Sheet5) ].

**Findings From Problem Difficulties:** <br/>
<img src = "images/findings_from_problem_difficulties.PNG" width="700" height="350"><br/>

**Findings From Problem Tags:** <br/>
<img src = "images/findings_from_problem_tags.PNG" width="700" height="350"><br/>

**Findings From Problem Categories and Tags:** <br/>
<img src = "images/findings_from_problem_categories_and_tags.PNG" width="700" height="350"><br/>



## Findings and Observations

1. Mostly, difficulty of the categories increases alphabetically. For instance - B is difficult than A. On the other hand C is difficult than both A & B. Category A1, B1, G2, G3,.. which has a number on it's       prefix didn't follow this criteria.

2. If the problems difficulty increases, mostly count of total solve decreses. You can find the difficulty of the problem from point 1. Difficulty of problems cateogry - A, B, C are less than G3, I, J etc.
   So, A, B. C, D has highest solve count.

3. Solve counts in contest mostly depend on problems difficulty rathan than total contest occured overall. We see if the problem has less difficulty, then it got higher solves. e.g - A & B have the same          contest count but as A is less difficult than B, so contestant love to solve A rather than a bit difficult problem B.

4. Category wise problems count is same as the no of contest occured. All contest have problem A, B. So, it has the same count. C, D also occur almost every contest but in the problemset those problems were not maintain any serail. So, most probably this scenario occures for C, D also. But, G3, O, M, N category problem occurs rarely.

5. We see a list of tags and problems category. From here one can get a rough idea about what type of problems belongs to which type of problem topics/tags. But from the data it's really hard to come up with     a decision because it shows arbitrary results.

6. One can get more clear idea about a problem. One can find the difficulty of a problem and it's category. Difficulty level again depends on the category(vice-versa). A problem has low difficulty than B, C,     D etc. But, here also we can't take any decision about the tags. One category problem contains multiple tags.



## Build From Sources and Run the Code

1. Clone the repository
   `git clone https://github.com/MdTanvirHossainTusher/CF_visualizer.git`

2. Open the repository in your preferable editor and enter to `CF_visualizer` directory.

3. Create a virtual environment with these commands in windows-
   `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
   `.\venv\Scripts\activate`

4. Install selenium web driver and pandas into the virtual environment by the below commands-
   `pip install selenium webdriver_manager`
   `pip install pandas`

5. Run `scraper.py` with this command-
   `python scraper.py`

6. To deactivate the virtual environment type this command-
   `deactivate`

   
## To run `notebooks/CF_VISUALIZER.ipynb` -

1. Open the file in Google colab or Jupyter notebook and run all the cells sequentially.


N.B: You will get the `data/cf_problem_details.csv` file after running successfully `scraper.py`. On the other hand, after running `notebooks/CF_VISUALIZER.ipynb` you will get the cleaned dataset as `data/clean_cf_problem_details_dataset.csv`





