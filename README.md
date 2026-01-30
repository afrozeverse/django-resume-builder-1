# Django Resume Builder

A web-based application built with Django that allows users to create, customize, and download professional resumes using predefined templates.

## Features

- User registration and login system  
- Create, edit, and delete resumes  
- Multiple resume templates  
- Responsive design for desktop and mobile  
- Download resumes as PDF  
- Support for multiple resumes per account  

## Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite  

## Installation and Setup

### 1. Clone the repository
git clone https://github.com/afrozeverse/django-resume-builder-1.git

cd django-resume-builder

python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

http://127.0.0.1:8000/


## Screenshots
<img width="1366" height="628" alt="Screenshot (192)" src="https://github.com/user-attachments/assets/26cb7ce4-b242-4b1f-86ab-8f34261baeed" />
<img width="1345" height="624" alt="Screenshot (193)" src="https://github.com/user-attachments/assets/e1df3a92-ec77-4f60-a828-4995f9c30ab2" />
<img width="1343" height="633" alt="Screenshot (194)" src="https://github.com/user-attachments/assets/1bf906c8-0f2b-411d-9c57-26010b865514" />
<img width="1343" height="629" alt="Screenshot (195)" src="https://github.com/user-attachments/assets/0aec6556-6abc-4856-adeb-1dc34557feda" />
<img width="1345" height="628" alt="Screenshot (196)" src="https://github.com/user-attachments/assets/50186b91-b1cf-4f85-b557-29443848d570" />
<img width="1344" height="631" alt="Screenshot (197)" src="https://github.com/user-attachments/assets/b891e201-0a91-4939-b1d1-b302855c5e81" />
<img width="1345" height="626" alt="Screenshot (198)" src="https://github.com/user-attachments/assets/05f1c8b7-3ab7-428d-aa55-2becaa9387e7" />

## Project Structure

- `django-resume-builder/`
  - `authentication/` — Authentication app
  - `coreBuilder/` — Main application
  - `home/` — Home application
  - `static/` — CSS, JavaScript, images
  - `templates/` — HTML templates
  - `db.sqlite3` — Database (ignored in Git)
  - `manage.py`


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to improve.

## License

This project is licensed under the MIT License.
