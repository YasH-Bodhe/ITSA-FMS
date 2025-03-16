# 🎉 College Event Management System

A web-based application built using **Django** to manage college events and registrations.  
This system allows **users to register for events**, while **admins can create and manage events**.  

---

## 🚀 Features  
- ✅ **User Registration & Login** – Secure authentication system.  
- ✅ **Event Management** – Admins can **add, edit, and delete** events.  
- ✅ **QR Code for Registrations** – Users receive **QR codes** for event check-ins.  
- ✅ **Admin Dashboard** – Manage event details and view registrations.  
- ✅ **Profile Management** – Users can view their registered events.  

---

## ⚡ Tech Stack  
- **Backend:** Django 5.1.2  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (Can be migrated to PostgreSQL)  
- **Other:** QR Code Generator (`qrcode[pil]`)  

---

## 📌 Setup Instructions  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/YasH-Bodhe/ITSA-FMS.git
cd ITSA-FMS
2️⃣ Install Python (If Not Installed)
Windows: Download from python.org and install.
Mac/Linux: Python is usually pre-installed. Verify by running:
bash
Copy
Edit
python --version
3️⃣ Set Up a Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # (Windows)
source venv/bin/activate  # (Mac/Linux)
4️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
5️⃣ Apply Migrations
bash
Copy
Edit
python manage.py migrate
6️⃣ Create a Superuser (Admin Access)
bash
Copy
Edit
python manage.py createsuperuser
7️⃣ Run the Server
bash
Copy
Edit
python manage.py runserver
🔹 Open http://127.0.0.1:8000/ in your browser.

🖼 Screenshots
📌 (Add screenshots here manually)

Example:

md
Copy
Edit
![Home Page](https://your-image-link.com/homepage.png)
🌍 Live Demo
🚀 Live Version: 🔗 Coming Soon (Will be updated after deployment)

🤝 Contributing
Feel free to fork this repo and contribute!

📌 To contribute:

Fork the repo
Create a branch: git checkout -b feature-name
Commit your changes: git commit -m "Added new feature"
Push to your branch: git push origin feature-name
Open a Pull Request!
📜 License
This project is open-source under the MIT License.