📄 Django Resume Builder

A web-based application built with Django that allows users to create, customize, and download professional resumes using predefined templates.

🚀 Features

User registration & login system

Create, edit, and delete resumes

Multiple resume templates to choose from

Responsive design for desktop & mobile

Download resume as PDF

Multiple resumes per account

🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript

Database: SQLite

⚙️ Installation & Setup

Clone the repo

git clone https://github.com/your-username/django-resume-builder.git
cd django-resume-builder


Create virtual environment & activate

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Start the development server

python manage.py runserver


Open in browser → http://127.0.0.1:8000/

📸 Screenshots
<img width="1366" height="628" alt="Screenshot (192)" src="https://github.com/user-attachments/assets/26cb7ce4-b242-4b1f-86ab-8f34261baeed" />
<img width="1345" height="624" alt="Screenshot (193)" src="https://github.com/user-attachments/assets/e1df3a92-ec77-4f60-a828-4995f9c30ab2" />
<img width="1343" height="633" alt="Screenshot (194)" src="https://github.com/user-attachments/assets/1bf906c8-0f2b-411d-9c57-26010b865514" />
<img width="1343" height="629" alt="Screenshot (195)" src="https://github.com/user-attachments/assets/0aec6556-6abc-4856-adeb-1dc34557feda" />
<img width="1345" height="628" alt="Screenshot (196)" src="https://github.com/user-attachments/assets/50186b91-b1cf-4f85-b557-29443848d570" />
<img width="1344" height="631" alt="Screenshot (197)" src="https://github.com/user-attachments/assets/b891e201-0a91-4939-b1d1-b302855c5e81" />
<img width="1345" height="626" alt="Screenshot (198)" src="https://github.com/user-attachments/assets/05f1c8b7-3ab7-428d-aa55-2becaa9387e7" />
<img width="476" height="627" alt="Screenshot (199)" src="https://github.com/user-attachments/assets/7fc6acb3-c3eb-4789-b9d6-90a789b08a25" />
<img width="480" height="627" alt="Screenshot (200)" src="https://github.com/user-attachments/assets/deb2c1b1-a89d-407d-9445-9964c32a6a8b" />
<img width="475" height="628" alt="Screenshot (201)" src="https://github.com/user-attachments/assets/82ecde8f-132a-4494-828a-4d816f7e6e5c" />
<img width="471" height="631" alt="Screenshot (202)" src="https://github.com/user-attachments/assets/c73951d1-d64b-4355-9863-b3fc7d74618b" />


📂 Project Structure
django-resume-builder/
│-- authentication/   # Authentication app
│-- coreBuilder/      # Main app
│-- home/             # Home app
│-- static/           # CSS, JS, Images
│-- templates/        # HTML templates
│-- db.sqlite3        # Database (ignored in Git)
│-- manage.py

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to improve.

📜 License

This project is licensed under the MIT License.
