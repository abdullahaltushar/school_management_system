# school_management_system
<p> The school management system is a web-based application that allows users to manage classes, subjects, students, and their marks. It provides a dashboard summarizing the results based on the search filters. It has an authentication system that allows authorized persons to enter data while others can only view the results.</p>
<h3>Technologies Used</h3>
<li>Python 3.9</li>
<li>MongoDB 6.0</li>
<li>Django 3.2.15</li>
<li>Djongo 1.3.6</li>
<li>pymongo 3.12.3</li>
<h3>Installation</h3>
<li>1. Install MongoDB Compass <a href="https://www.mongodb.com/try/download/community">here</a></li>
<li>2. Install Python <a href="https://www.python.org/downloads/">here</a></li>
<li>3. Clone the repository: git clone https://github.com/your-username/school-management-system.git </li>

Clone the repository: git clone https://github.com/your-username/school-management-system.git
Navigate to the project directory: cd school-management-system
Install the required packages: pip install -r requirements.txt
Usage
Start the server: python app.py
Navigate to http://localhost:5000 in your web browser.
You will be redirected to the login page. Enter your credentials to log in.
Once you're logged in, you can add classes, subjects, students, and marks using the provided forms.
To view the dashboard, select a class from the dropdown menu. If no subject is selected, the dashboard will show the aggregated results. If a subject is selected, the dashboard will show the results for that subject.
