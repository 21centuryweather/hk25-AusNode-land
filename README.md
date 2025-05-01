# Precipitation/soil moisture feedback: positive or negative?  <img src='https://21centuryweather.org.au/wp-content/uploads/Hackathon-Image-WCRP-Positive-1536x736.jpg' align="right" height="139" />

**Project leads:** Mathew Lipson (@matlipson), 21st Century Weather, UNSW Sydney /

**Project members:** TBC

**Collaborators:**
Other hackathon land project: https://github.com/digital-earths-global-hackathon/hk25-teams/tree/main/hk25-Land

## Background

There is ongoing debate on whether soil moisture is positively or negatively correlated with precipitation. This has huge implications for future climate, storms, drought and land cover change: i.e. will lower soil moisture lead to lower local precipitation, leading to lower soil moisture and so on? Our current global climate models (e.g. for CMIP6) indicate a strong positive feedback, while km-scale models indicate a weak or negative feedback.

A recent study (Lee and Hohenegger, 2024) compared global year-long 5km simulations with 60-year 160 km resolution simulations more typical of climate simulations, both using the ICON model. They examined the northern hemisphere (boreal) summer, and found weaker and more negative soil moisture/ precipitation feedback in high resolution simulations, with some regional differences. While interesting, the results have little bearing on Australia, as results are analysed during our northern dry season with little to no rain.

This Hackathon provides the necessary data to test whether resolution is important in soil moisture/ precipitation feedbacks, and how important that is for Australia

Lee and Hohenegger, 2024: https://doi.org/10.1073/pnas.2314265121
Weaker land–atmosphere coupling in global storm-resolving simulation

![Lee2024](https://github.com/user-attachments/assets/97fe3414-d4ed-4a45-825d-0f2cba6cbaf8)

**Primary research question:**
Can we reproduce the results of Lee and Hohenegger 2024 for an Austral summer?
If so, what are the implications for Australia?

**Secondary research questions:**
How do the correlation differences compare across different models?
Can we resolve the important processes and precedent conditions that lead to positive/negative feedback?
What are the timescales of important feedbacks? (hours, days, weeks?)
What is the impact of soil moisture differences on storm/ hail/ precip conditions

**Methods:**
All read Lee and Hohenegger, 2024 methods and discuss with group
Split up to read other relevant literature and summarise to group
Read over Lee and Hohenegger github python code for paper, discuss problems
Split into groups of two to write code to 1) reproduce Lee and Hohenegger 2) analyse ACDC observations for Australia 3) if not part of available outputs, calculate CAPE, CIN (hopefully other groups need these variables also)
Come together to write draft paper

**Further reading:**
 - On the Physics of High CAPE (Emanuel 2023): https://doi.org/10.1175/JAS-D-23-0060.1
 - Influence of land-atmosphere feedbacks on temperature and precipitation extremes in the GLACE-CMIP5 ensemble (Lorenz et al., 2016) 10.1002/2015JD024053
 - Intraseasonal versus interannual measures of land-atmosphere coupling strength in a global climate model: GLACE-1 versus GLACE-CMIP5 experiments in ACCESS1.3b (Lorenz et al., 2015): 10.1175/JHM-D-14-0206.1





**Data:**
* Name, link
* Name, link

## Contributing Guidelines

> The group will decide how to work as a team. This is only an example. 

This section outlines the guidelines to ensure everyone can work and collaborate. All project members have write access to this repository, to avoid overlapping and merge issues make sure you discuss the plan and any changes to existing code or analysis.

### Project organisation

All tasks and activities will be managed through GitHub Issues. While most discussions will take place face-to-face, it is important to document the main ideas and decisions on an issue. Issues will be assigned to one or more people and classified using labels. If you want to work on an issue, comment and make sure is assigned to you to avoid overlapping. If you find a problem in the code or a new task, you can open an issue. 

### How to collaborate

* **Main branch:** We want to keep things simple, if you are working on a notebook alone you can push changes to the main branch. Make sure to 1) only add and ccommit that file and nothing else, 2) pull from the remote repo and 3) push.

* **Working on a branch:** if you want to fix or propose a change to someone else code you will need to create a branch and open a pull request. Make sure you explain your suggestion in the pull request message. **This also applies to collaborators outside the project team.**

### Repository structure

This is how the project should look like but make sure to change the name `template-hackathon-project` to something meaningful. 

```bash
template-hackathon-project/
├── LICENCE
├── README.md
├── template_project_hackathon
│   ├── analysis.py
│   ├── __init__.py
│   └── read.py
└── tests
    ├── test_analysis.py
    └── test_read.py
```
* `template_hackathon_project/` this folder will include the code to analysis the data.
* `tests/` this folder contains test code that verifies that your code does what it should.

