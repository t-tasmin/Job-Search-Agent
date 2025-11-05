# Canadian Job Search Agent

## Project Overview
The **Job Search Agent** automates the extraction of job information from Canadian job sites.  
It collects structured data from job postings and matches them against a user’s skills to help identify the best opportunities.

**Extracted Data Includes:**  
- Job Title  
- Employer  
- Location  
- Work Mode (Onsite/Hybrid)  
- Experience Needed  
- Tools  
- Technical Skills  
- Other Relevant Skills  


## Objective
- Make the job search process faster and more efficient  
- Provide structured, searchable datasets of current job listings  
- Highlight key skills and tools required in the market  
- Assess the match between a user’s skills and the required skills using a **similarity score**

---

## Tools & Technologies
- **Selenium** – Browser automation  
- **XPath** – Locating elements on web pages  
- **Gemini 2.5 + Prompt Engineering** – Extracting structured information from job descriptions  
- **NumPy & Pandas** – Data cleaning and manipulation  
- **Scikit-learn** – Feature extraction and calculating skill similarity  

---

## How It Works
1. The agent visits job portals and extracts job postings.  
2. Extracted information is cleaned and structured into a dataset.  
3. Skills listed in job descriptions are compared with the user’s skills.  
4. A similarity score is calculated to assess the match.  
5. The results can be visualized or exported for further analysis.  

---

## Future Improvements
- Add support for more job portals (e.g., LinkedIn, Glassdoor)  
- Implement a web dashboard for real-time results  
- Add trend analysis for in-demand skills and roles  
