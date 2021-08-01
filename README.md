# inventory_management
Inventory Management

Steps to run project:
1. Clone code from git repo
   git clone https://github.com/RJAJU/inventory_management.git

2. Setup virtual environment
   virtualenv -p python3.7 venv

3. Activate this virtual environment
   source venv/bin/activate

4. move into your project
   cd inventory_management

5. Install all required packages using requirements.txt file
   pip install -r requirements.txt

6. setup PYTHONPATH to this project directory
   export PYTHONPATH=$(pwd)

7. Setup interprater for this project using this virtual environment

8. To enter into Admin panel, either create superuser or normal user using existing superuser 
   python manage.py createsuperuser
   provide required details and press Enter

9. Run the server
   python manage.py runserver

10. Data files can be uploaded using Django default UI
    Open http://localhost:8000/admin

11. Open http://localhost:8000 URL in browser for following actions:
    I: List all members
    II: Book new inventory for existing member
    III: Cancel existing inventory
    IV: Add new members

