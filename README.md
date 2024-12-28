
# Expense Management and Forecasting System



# Expense Management System  

This **Django-based Expense Management System** provides users with a comprehensive platform to manage, track, and visualize their expenses efficiently. The application integrates data visualization, machine learning, and advanced database management for an intuitive user experience.  

## Key Features  
- **Expense Management**: Log, categorize, and manage expenses with ease.  
- **Monthly Expense Forecasting**: Implemented a machine learning algorithm to predict monthly expenses, helping users plan and control spending.  
- **Interactive Dashboard**: Utilized Chart.js for insightful and interactive visualizations of expenses across different categories.  
- **Advanced Search**: AJAX-based searching for seamless and real-time expense tracking.  
- **Database Management**: Leveraged PostgreSQL with Django ORM for scalable and efficient storage of expense data.  
- **User Authentication**: Verified registration emails and authorized users using Django’s authentication system, including email-based verification.  

## Technologies Used  
- **Backend**: Django, Python  
- **Frontend**: Chart.js, AJAX, HTML, CSS  
- **Database**: PostgreSQL  
- **Machine Learning**: Predictive model for expense forecasting using exponential moving average


This system empowers users with effective tools to track their spending habits and improve financial planning.  

## How to Run  
1. Clone the repository:  
   ```bash
   git clone <repository-url>
   cd <repository-folder>
2. Set up the virtual Environment
    ```bash
    python3 -m venv env  
3. Activate the Environment
    ```bash
   ./env/Scripts/activate.ps1
   OR
   ./env/Scripts/activate.bat

4. install dependencies
    ```bash
    pip install -r requirements.txt
5. Configure the PostgreSQL database in the settings.py file.
6. Apply migrations:
    ```bash
    python manage.py makemigrations  
    python manage.py migrate  
7. Run the development server:
    ```bash
    python manage.py runserver

## Links:
- google colab link for ML algorithm: https://colab.research.google.com/drive/1jO0D7SKp5V4xM1gG2133Yt-jbbA5wppu#scrollTo=Mz1c5Ep35aq5
- Demo video: https://www.youtube.com/watch?v=MFXV4T8wdDI

## Screenshots


![image](https://github.com/user-attachments/assets/1e5d5a36-a086-47d6-8278-4039d84ca994)
![image](https://github.com/user-attachments/assets/e806d627-b242-46a0-9115-a6084caf9342)
![image](https://github.com/user-attachments/assets/a6b9d307-014d-4aad-8b7f-221f15a6af5c)
![image](https://github.com/user-attachments/assets/b25f642b-345a-4ff9-aae3-aae290a1ac4d)



