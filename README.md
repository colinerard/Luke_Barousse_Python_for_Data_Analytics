# Overview

This project serves as an introduction to the use of Python for data analysis and is based on the course offered by Luke Barousse (on Youtube and on his personal website). We will analyses data analytics global job market data to draw specific insights and understand the job market more effectively. 

The bulk of the analysis focuses on Data Analysts roles in the US. More specifically, it explores how salaries compare to other data roles, the various types of skills required and describes other characteristics of these types of jobs.  

# Questions answered

Here are the 4 main questions answered through this analysis:

1. What are the most demanded skills for the top 3 most popular data roles?
2. How are the most in-demand skills trending for Data Analysts in the US?
3. How well are data roles paying and what skills command a higher salary for Data Analysts?
4. What are the most optimal skills to learn for Data Analysts?

# Data and tools used

## Data

The data is from [Luke Barousse's python course](https://www.lukebarousse.com/python) and consolidates hundreds of thousands of job posting information for data roles across a vast array of countries. The data contains the following information:

- Job title
- Location
- Posted on which website
- Schedule type
- Work from home
- Job posted date
- Degree needed
- Health insurance offered
- Job country
- Salary (hourly or yearly)
- Company name
- Job skills needed

## Tools used

- Python: python is the language used for the entirety of the analysis and the following librairies were used.
    - Pandas: to analyse the data
    - Matplotlib: to visualise the data
    - Seaborn: to visualise the data
- Jupyter notebooks: the tool used to run python scripts and include notes to structure the analysis 
- VS Code: the code editor used to execute the scripts.
- Git and Github: for version control and share the work done

# The Analysis

## 1. What are the most demanded skills for the top 3 most popular data roles?

The first step is to identify the number of roles per job postings and identify which 3 are the most in demand. The next step is to evaluate what are the top 5 skills for each of these top 3 job types. The final step is to measure the relative importance (in % over all the job postings) of the top skills.

The notebook with the detailed calculations and python scripts is here: [2_Skills_Count.ipynb](3_Project\2_Skills_Count.ipynb)

### Python 

Here is the python script to obtain the visualisation identifying the top 3 job titles and key related skills. 

```python

fig, ax = plt.subplots(len(job_titles), 1)

sns.set_theme(style="ticks")

for i, job_title in enumerate(job_titles):
    df_plot = df_skills_perc[df_skills_perc["job_title_short"] == job_title].head(5)
    sns.barplot(data=df_plot, x="skill_percent", y="job_skills", ax=ax[i], hue="skill_count", palette="dark:b_r")
    ax[i].set_title(job_title)
    ax[i].set_ylabel("")
    ax[i].set_xlabel("")
    ax[i].get_legend().remove()
    ax[i].set_xlim(0,80)

    for n, v in enumerate(df_plot["skill_percent"]): 
        ax[i].text(v + 1, n, f"{v:.0f}%", va="center")

    if i != len(job_titles) -1:
        ax[i].set_xticks([])

fig.suptitle("Likelihood of Skills Requested in US Job Postings", fontsize=15)
fig.tight_layout(h_pad=0.5)
plt.show()

```
### Results

![Visualisation of top skills for key data roles](3_Project\Images\2_Top_Skills.png)

### Insights

1. Python and SQL are skills that are demanded for a majority of data roles, and they have an increasing importance for more demanding roles such as Data Engineer and Data Scientist.
2. SQL is the most demanded skill for Data Analyst (51%) and Data Engineer (68%), while Python is the most demanded skill for Data Scientist (72%)
3. Data management and visualisation tool such as Excel and Tableau are also important skills to possess for roles who need to communicate insights through data, such as Data Analyst and Data Scientist. Data Scientist requires more technical skills (AWS, Azure, Spark). 

## 2. How are the most in-demand skills trending for Data Analysts in the US?
 
 The first step is to evaluate the number of Data Analysts job postings and the top requested skills and then break it down by month. The next step is to evaluate the relative value (in %) of job monthly job postings that required the top skills. The final step is to plot the findings for the top 5 skills and see if there is any trend.

The notebook with the detailed calculations and python scripts is here: [3_Trending_Skills.ipynb](3_Project\3_Trending_Skills.ipynb)

### Python

Here is the main python script used to obtain the final visualisation.

```python

from matplotlib.ticker import PercentFormatter

df_plot = df_DA_US_percent.iloc[:, :5]
sns.lineplot(data=df_plot, dashes=False, legend='full', palette='tab10')
sns.set_theme(style='ticks')
sns.despine() # remove top and right spines

plt.title('Trending Top Skills for Data Analysts in the US')
plt.ylabel('Likelihood in Job Posting')
plt.xlabel('2023')
plt.gca().yaxis.set_major_formatter(PercentFormatter(decimals=0))
plt.legend(
    title="Job Skills",
    loc="upper center",
    bbox_to_anchor=(0.5, -0.15),
    ncol=5
)

plt.tight_layout()
plt.show()

```

### Results

![Trending Skills for Data Analysts in the US](3_Project\Images\3_Trending_Skills.png)

### Insights

1. All top 5 skills are relatively stable over the 12 months of 2023, with SQL and Excel being the two clear most in-demand skills over the entire year.
2. A slight downwards trend can be observed for SQL, but it still the most in-demand skill by far. 
3. Out of the 5 top skills, python is the one exhibiting a slight upwards trend.

## 3. How well are data roles paying and what skills command a higher salary for Data Analysts?

The first step was to select the six most popular roles (i.e. the roles with the highest number of job postings) and evaluate their median yearly salary. This allows to evaluate how Data Analyst roles compare to other roles. Then, filtering only for Data Analyst roles, we evaluated which skill allows them to get a higher salary on average.

The notebook with the detailed calculations and python scripts is here: [4_Salary_Analysis.ipynb](3_Project\4_Salary_Analysis.ipynb)

### Median salary per role

#### Python

Here is the main python script used to obtain the final visualisation.

```python
# plotting
sns.boxplot(data=df_US_top6, x="salary_year_avg", y="job_title_short", order=job_order)
sns.set_theme(style="ticks")

# formatting
plt.title("Salary Distribution in the United States")
plt.xlabel("Yearly Salary (USD)")
plt.ylabel("")
plt.xlim(0, 600000)
ticks_x = plt.FuncFormatter(lambda x, pos: f"${int(x/1000)}K")
plt.gca().xaxis.set_major_formatter(ticks_x)
plt.tight_layout()
plt.show()

```

#### Results

![Salary Distribution in the US](3_Project\Images\4_Salary_per_Role.png)

#### Insights

1. Their is a  significant difference in yearly median salary across the six roles. Data Scientist and Data Engineers (and the senior roles) earn more than the Data Analysts (and Senior Data Analysts). Senior Data Scientists, the highest paid roles, earn on average close to USD 150K a year and Data Analyst, the lowest paid roles, earn on average below USD 100K a year.
2. Salaries increase with seniority and specialisation of the roles. 
3. Senior Data Analyst roles still have a lower average yearly salary than Data Engineer and Data Scientist, identify a lower salary ceiling for these roles. Data analysts wanting to earn a higher salary should consider moving to other types of data roles rather than becoming a Senior Data Analyst.
3. Their is a large spread in yearly salaries across all roles, mostly seen for Data Scientists and Data Engineers. There is a large number of outliers for both these roles, suggesting that exceptional skills or qualifications for these roles can lead to a  compensation outside of the normal range.

### Median Salary per Skill for Data Analyst Roles

#### Python

Here is the main python script used to obtain the final visualisation.

```python

# plotting the graph
fig, ax = plt.subplots(2, 1)
sns.set_theme(style="ticks")

# plotting the top 10 paying skills
sns.barplot(data=df_DA_top_pay, x="median", y=df_DA_top_pay.index, hue="median", ax=ax[0], palette="dark:b_r")
ax[0].legend().remove()
ax[0].set_title("Top 10 Most Paying Skills for Data Analyst Roles")
ax[0].set_xlabel("")
ax[0].set_ylabel("")
ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${int(x/1000)}K"))

# plotting the top 10 most popular skills
sns.barplot(data=df_DA_most_pop, x="median", y=df_DA_most_pop.index, hue="median", ax=ax[1], palette="light:b")
ax[1].legend().remove()
ax[1].set_xlim(ax[0].get_xlim())
ax[1].set_title("Top 10 Most Popular Skills for Data Analyst Roles")
ax[1].set_xlabel("")
ax[1].set_ylabel("")
ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${int(x/1000)}K"))

plt.tight_layout()
plt.show()

```

#### Results

![Salary Per Skill](3_Project\Images\4_Salary_per_skill.png)

#### Insights

1. Highly technical skills (i.e. AI, programming, deep learning, automation, etc.) for Data Analysts command a salary premium far higher than the median yearly salary, sometimes close to doulbe the median baseline. Jobs demanding these skills are however very scarce and the scope of these roles is likely to go above and beyond what is expected for an average Data Analyst role.
2. From the 10 most popular skills for Data Analysts, data manupilation and data visualisation skills are the most important to obtain a higher salary. The salary for these skills is aligned with the median yearly salary for Data Analyst roles. 
3. Some less specialised skills (i.e. powerpoint, excel, word) allow Data Analysts to round up their profile as they are still very popular. Relying solely on these skills will however lead to much lower salaries and Data Analysts would be wise to learn other skills.
4. There is a clear distinction between the highest paying skills and the most popular skills (i.e. no skill appears in both charts). Data Analysts wanting to maximise their hiring and salary potential would be wise to have a diverse skillset made of some of the core skills and also choose a couple of highly-specialised skills.

## 4. What are the most optimal skills to learn for Data Analysts?

The first step is to calculate evaluate which skill is most demanded (in % of total job postings) and also evaluate their average median salary. Then, we plot the results to identify which skills are both in high-demand and command a high salary.

The notebook with detailed calculations and python scripts is here: [5_Most_Optimal_Skills](3_Project\5_Most_Optimal_Skill.ipynb)

### Python

Here is the main python script used to obtain the final visualisation.

```python
# set-up the plot
sns.scatterplot(
    data=df_DA_skills_tech_high_demand,
    x='skill_percent',
    y='median_salary',
    hue='technology'
)

sns.despine()
sns.set_theme(style='ticks')

# Set axis labels, title, and legend
plt.xlabel('Percent of Data Analyst Jobs')
plt.ylabel('Median Yearly Salary')
plt.title('Most Optimal Skills for Data Analysts in the US')
plt.legend(title='Technology')

from matplotlib.ticker import PercentFormatter
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, pos: f'${int(y/1000)}K'))
ax.xaxis.set_major_formatter(PercentFormatter(decimals=0))

# Prepare texts for adjustText
texts = []
for i, txt in enumerate(df_DA_skills_high_demand.index):
    texts.append(plt.text(df_DA_skills_high_demand['skill_percent'].iloc[i], df_DA_skills_high_demand['median_salary'].iloc[i], txt))

# Adjust text to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray'))

# Adjust layout and display plot 
plt.tight_layout()
plt.show()

```

### Results

![Optimal Skills](3_Project\Images\5_Optimal_Skills.png)

### Insights

1. Skills in high-demand and high-priority (i.e. top-right quarter of the chart) should be in the main priority for data analysts. Programming skills, such as Python and SQL, should therefore be high on the priority list of any current or aspiring data analysts. 
2. Out of the two main business intelligence / visualisation tools, Tableau seems to be to most optimal in comparison to power bi as it is both more in-demand and provides a higher salary on average.
3. More technical tools, such as databases management tools or cloud tools, allow analysts to earn a higher salary, but are however a lot less in demand in comparison to programming and other analyst tools. This illustrates a higher valuation associated to the management and manipulation of large databases. 

# Key Insights

1. **Not all skills are equal for Data Analysts.** Aspiring data analysts should do well focusing on programming (SQL, python) and data visualisation (tableau, power BI) skills to increase their likelihood of getting hired and obtain a higher average yearly salary. Highly specialised technical skills (cloud technologies, AI, machine & deep learning, etc.) can help analysts reach much higher salaries as compensation for the knowledge and skills, but these demands are more of an exception than the norm.

2. **Data Analysts are good entry-level position that can be good stepping stones for more technical roles.** Data Analyst is by far the most in demand and common role in the data field, as illustrated by the consistently large amount of job postings for this position type, and they offer lower salaries than other role types. Experienced Data Analysts aiming to advance in the field and / or increase revenues should consider other data roles such as Data Engineers or Data Scientists positions. Data Analysts could aspire to these roles with sufficient experience and the skills acquired in their Data Analyst roles would definitely come in handy. 

3. **There is a high degree of certainty that data analysts roles will remain available for those who posses the right skills.** Data Analysts is the most common role advertised in job postings and, over time, there seems to be a large number of open roles requiring similar skills.  

# What I learned
This project what my introduction to Python. Although a lot of room for improvement and familiarisation with the language remains, it was a great basis to learn the fundamentals of the language, how to make use of the different packages and librairies and become more familiar with tools such as VS Code and Git & Github.

- **Python usage for data analytics.** I've learned how to use the various librairies related to data analysis such as pandas, matplotlib and seaborn as well as how to apply various python terms, such as functions, methods, etc. to manipulate, analyse and visualise data in python.

- **The importance of understanding the underlying data set and knowing what questions you are aiming to answer before starting your analysis.** 

- **AI is your friend.** ChatGPT proved to be a very useful tool to improve productivity, identify errors, find alternative ways of completing specific tasks or even explaining complex pieces of code.

# Challenges I faced

- **Understanding complex python scripts.** Some code scripts used to achieve certain functions are quite complex and I needed to be have them explained in multiple different ways through ChatGPT to grasp their meaning and understand their impact.

- **Incomplete / missing data.** The analysis relies on data which is sometimes not as complete as one would want to (i.e. missing salary information) to obtain an accurate picture.

# Outro

As this project was my personal introduction to python in the data analysis sphere, it showed me how much there is still to learn and how it is a complete and flexible tool that can accomplish a wide array of tasks, from data cleaning to calculations and data visualisation. Python is one of the most and in-demand popular tool for data analysis and, as such, I'll seek to continue further my knowledge of it through additional data analysis projects on different data sets.