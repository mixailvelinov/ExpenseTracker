
# Expense Tracker
**The application is live at [ExpenseTracker production](https://expensetracker-production-2afe.up.railway.app/)**

Expense Tracker is a web app that acts ad a diary for your expenses. You can deposit, register expenses, create a wishlist and monitor your total expenses. Whenever you buy something from your wishlist, you can mark it as bought and the amount will be retraced from your total funds.

## Setup Instructions
Follow these steps to run the project locally:

### 1. Clone/Download
Clone or download the repo to your local machine.

### 2. Create the .env File

Use the provided .env template in the project to create your .env file.
  
### 3. Set Up the Virtual Environment
Run the following commands to set up your Python virtual environment:

```python -m venv venv```
``` venv\Scripts\activate ```

### 4. Install Dependencies
Install the required Python packages using the requirements.txt file:

```pip install -r requirements.txt```

### 5. Run Database Migrations
Apply the database migrations to set up the required tables. The migrations contain some pre-filled content for games:

```python manage.py migrate```

### 6. Start project

Apply the following command to run the project locally:

```python manage.py runserver```
