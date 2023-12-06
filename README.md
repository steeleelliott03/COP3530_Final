# Keep Your Eye on the Crime - Group 94

## Team Information
- **Team Name:** Group 94
- **Team Members:** Austin Markus, Steele Elliott, Nadzumie Flores
- **GitHub URL:** [COP3530_Final Project](https://github.com/steeleelliott03/COP3530_Final)
- **Video Demonstration:** [Project Overview Video](https://youtu.be/t-2wSQbUNTk)

## Final Project Proposal

### Problem
We aim to identify the Chicago districts with the highest incidence of crime, analyze the specific types of crimes prevalent in these areas, and ascertain the months during which these crimes are most prevalent.

### Motivation
By pinpointing districts with elevated rates of specific crimes during particular periods, we can gain valuable insights for devising targeted crime prevention strategies. This will enable us to allocate our prevention efforts more efficiently, focusing on areas where crime is more amplified.

### Features
- Computation of crime rates for specific districts and dates.
- Identification of areas vulnerable to particular types of crimes.
- Implementation of a Hash Table and a B-Tree for efficient data storage and retrieval.
- User interface using the TKinter library for user interaction.
- Options for selecting data structure, date, crime type, and search initiation.
- Time tracking for search and sorting operations to evaluate algorithm efficiency.

### Data Source
- **Link:** [Chicago Crime Dataset on Kaggle](https://www.kaggle.com/datasets/chicago/chicago-crime/data)
- **Description:** The dataset covers reported crimes in Chicago from 2001 to the present (excluding the last seven days), sourced from the Chicago Police Department's CLEAR system.

### Tools Used
- Python
- GitHub
- Kaggle
- Google BigQueryAPI
- TKinter (UI)

### Algorithms Implemented
- **Hash Table:** For mapping individual crime values to characteristics like date, district, and crime type.
- **B-Tree:** Employed for efficient storage based on attribute values.
- **UI Integration:** TKinter is used to integrate these algorithms into a dynamic platform for displaying crime information.

### Distribution of Responsibilities
- **Austin Markus:** Implementation of the hash table.
- **Steele Elliott:** Development of the B-tree.
- **Nadzumie Flores:** Design and implementation of the user interface using GUI/TKinter.

## Analysis
We analyzed the performance of the B-tree and the hash table on a dataset of 150,000 data points. The B-tree demonstrated significantly more efficient search capabilities compared to the hash table. The hash table operates at an average complexity of O(1) per insertion, while the B-Tree's insertion complexity is O(log n). For searches, the hash table's complexity is O(N), and the B-Tree search has a complexity of O(log n + M).

## Reflection
The project was a great success, marked by effective communication and collaboration. Each team member brought unique skills to the table, leading to a well-rounded solution. Challenges were met with teamwork, leading to innovative solutions and a more robust final product.

### Learning Outcomes
- **Nadzumie Flores:** Learned about UI implementation using GUI/TKinter and the complexities of implementing a B-tree.
- **Steele Elliott:** Gained deeper insights into B-tree data structures, especially in node splitting and balance management.
- **Austin Markus:** Advanced in optimizing data mapping within a hash table and selecting appropriate hash functions.

The project highlighted the effectiveness of proper work division and the value of collaborative problem-solving in a team setting.
