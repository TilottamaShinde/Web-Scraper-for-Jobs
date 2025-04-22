# Web Scraper for Jobs

This project is a simple **web scraper** designed to scrape job listings related to **PL/SQL** from **Naukri**. It extracts job details such as title, company, location, experience, salary, and job URL, and saves the results in a CSV file.

##  **Technologies Used**

- Python
- **BeautifulSoup** (for web scraping)
- **Requests** (for HTTP requests)
- **Pandas** (for saving data in CSV format)

##  **Features**

- Scrapes job listings related to **PL/SQL** from Naukri.
- Extracts the following details from each job:
  - Job title
  - Company name
  - Location
  - Experience required
  - Salary (if available)
  - Job URL
- Saves the extracted data in a **CSV** format for further analysis.

##  **Installation**

To run this project, follow these steps:

### 1. Clone the repository


git clone https://github.com/your-username/web-scraper-for-jobs.git
cd web-scraper-for-jobs

## 2. Create a virtual environment (optional but recommended)**

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

## 3. Install the required dependencies

pip install -r requirements.txt
Note: If you don't have a requirements.txt file yet, you can manually install the required packages:


pip install requests beautifulsoup4 pandas

## 4. Run the scraper

python web_scraper_for_jobs.py
