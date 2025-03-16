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

## 🌟 Tech Stack  
- **💻 Backend:** Django 5.1.2  
- **📅 Frontend:** HTML, CSS, JavaScript  
- **📂 Database:** SQLite (Can be migrated to PostgreSQL)  
- **🤖 Other:** QR Code Generator (`qrcode[pil]`)  

---

## 📀 Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/YasH-Bodhe/ITSA-FMS.git
cd ITSA-FMS
```

### 2️⃣ Install Python (If Not Installed)  
- **Windows:** Download from [python.org](https://www.python.org/) and install.  
- **Mac/Linux:** Python is usually pre-installed. Verify by running:  
  ```bash
  python --version
  ```

### 3️⃣ Set Up a Virtual Environment  
```bash
python -m venv venv
venv\Scripts\activate  # (Windows)
source venv/bin/activate  # (Mac/Linux)
```

### 4️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 5️⃣ Apply Migrations  
```bash
python manage.py migrate
```

### 6️⃣ Create a Superuser (Admin Access)  
```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Server  
```bash
python manage.py runserver
```
🔹 **Open:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.  

---

## 🖼️ Screenshots  
📌 **(Add screenshots here manually)**  

Example:  
```md
![Home Page](https://your-image-link.com/homepage.png)
```

---

## 🌐 Live Demo  
🚀 **Live Version:** 🔗 _Coming Soon_ (Will be updated after deployment)  

---

## 🤝 Contributing  
We welcome contributions! Follow these steps:  

1. **Fork the repository**  
2. **Create a new branch:**  
   ```bash
   git checkout -b feature-name
   ```
3. **Make your changes and commit:**  
   ```bash
   git commit -m "Added new feature"
   ```
4. **Push to your branch:**  
   ```bash
   git push origin feature-name
   ```
5. **Open a Pull Request!**  

---

## 📚 License  
This project is open-source under the **MIT License**.  

