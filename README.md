# Group 94
## Members
- Austin Markus
- Steele Elliott
- Nadzumie Flores

## Final Project Proposal
### Keep Your Eye on the Crime

#### Problem
We want to determine which Chicago districts are experiencing the highest crime rates, which types of crimes are occurring in these areas, and in which months these crimes occur the most.

#### Motivation
If we can determine which districts have the highest rates of certain types of crimes at certain times, then it will provide insight into addressing crime prevention in specific areas. This will allow us to allocate our prevention efforts more efficiently to areas with heightened crime.

#### Features
We will have solved the problem once we have calculated the crime rates for specific districts and dates and determined which areas are most susceptible to certain types of crimes.

#### Data
[Chicago Crime Dataset](https://www.kaggle.com/datasets/chicago/chicago-crime/data) – Our plan is to utilize the most recent year of crime reported in this dataset (2017).

#### Tools
- C++
- GitHub
- Kaggle

#### Visuals
Users will have the following options:
1. **Search by crime type**
   - Enter crime type
   - Options:
     - Sort by monthly totals
     - Sort by district totals
     - Show top 10 dates
2. **Search by month**
   - Enter month
   - Options:
     - Sort by crime type totals
     - Sort district totals
     - Show top 10 dates
3. **Search by specific date**
   - Enter specific date
   - Options:
     - Sort by crime type totals
     - Sort by district totals
     - Show top 10 dates
4. **Search by district number**
   - Enter district number
   - Options:
     - Sort by crime type totals
     - Sort by monthly totals
     - Show top 10 dates

#### Strategy
We plan on potentially using a hash table and a B+ tree, since the hash table may allow us to map the values for each individual crime to other associated characteristics (date, district, crime type) and the B+ tree will allow us to store items based on their values.

#### Distribution of Responsibility and Roles
- **Austin Markus**: Developing the hash table implementation.
- **Steele Elliott**: Developing the B+ tree implementation.
- **Nadzumie Flores**: Developing the user interface and analysis documentation.
  
Note: Most of our roles will be cross-disciplinary, assisting each other to complete all the necessary tasks as a unit.
