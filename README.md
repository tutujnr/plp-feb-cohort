
# 💼 Django Portfolio

This is a Django-powered personal portfolio website designed to showcase your bio, skills, tech stack, experience, education, certifications, and projects. 
All content is easily managed through Django Admin. It features a working contact form, a sleek responsive UI, and is ready for deployment.

## 🚀 Features

- **About Me** section with profile image and dynamic bio
- **Technology stack** with icons and names
- **Filterable Portfolio** (Projects, Certifications)
- **Experience and Education** timelines with nested descriptions
- **Functional contact form** with email integration
- **Admin panel** to manage all site content
- **Responsive and mobile-friendly design**

## ⚙️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, Bootstrap
- **Database:** SQLite3 (default)


## 🛠️ Getting Started

Follow these steps to set up the project on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/tutujnr/plp-feb-cohort.git
cd portfolio 
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up the database (for the first time)

```bash
python manage.py migrate
```

### 4. Create a superuser to access the Django Admin

```bash
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

Now, visit `http://127.0.0.1:8000` to see your project in action!

## 📋 Usage

Once the server is running, you can access the portfolio site at `http://127.0.0.1:8000/`.

You can manage the site content (About Me, Experience, etc.) via the Django Admin interface, accessible at `http://127.0.0.1:8000/admin/`. Make sure to log in with the superuser account you created earlier.

## 🛠️ Features in Detail

### About Me
The "About Me" section includes a profile image and a description. This section can be easily updated through Django Admin.

### Technologies
This section displays icons and names for technologies you’ve worked with, allowing you to showcase your technical skills.

### Portfolio
You can filter and showcase projects, certifications, and other key accomplishments in the Portfolio section. These items are grouped by issuer and sorted by year.

### Experience & Education
The Experience and Education sections include timelines with detailed descriptions of your work and academic history.

### Contact Form
The contact form integrates with Django’s `send_mail` function, sending the submitted form data to a specified email address.


## 👥 Contributing

If you’d like to contribute to this project, follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request to merge your changes
