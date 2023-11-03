![icon48](https://github.com/it21026416/CyberLearn/assets/87382380/48b9a2f2-d77f-47e5-b7ff-97e36edd8254) 
# CyberLearn


CyberLearn is an innovative platform designed to scrape and analyze cybersecurity courses and news, providing real-time recommendations through a browser extension.

# Features
1. Course Recommendations: Get the latest course recommendations tailored to your interests.
2. Data Scraping: Automated scraping from popular cybersecurity platforms.
3. Real-time Cyber Attack News: Stay updated with the latest cyber attack news from trusted sources.
4. Admin Controls: Manual data refresh capabilities and detailed logs for administrators.
5. Docker Containerization: Ensures a consistent environment for deployment.
6. Python Scheduler: Automated tasks to ensure data is always up to date.
7. Browser Extension: Access CyberLearn recommendations directly from your browser.

# Getting Started
# Prerequisites
Docker
Python 3.8+

# Installation
1. Clone the repository: git clone https://github.com/it21026416/CyberLearn.git
2. Navigate to the project directory: cd CyberLearn
3. Install the required packages: pip install -r requirements.txt
4. Build the Docker container: docker build -t cyberlearn .
5. Start the Docker container: docker run -p 5000:5000 cyberlearn
5. Access the web interface at: http://localhost:5000

# Usage
1. For Users: Install the browser extension and access course recommendations directly.
2. For Admins: Log in to the admin panel to trigger data scraping, refresh data, and check logs.

# Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change. Please ensure your PRs are well-documented.
