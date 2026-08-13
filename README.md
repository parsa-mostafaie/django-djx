# 🐦 djx – A Modern X (Twitter) Clone Built with Django

[![Django](https://img.shields.io/badge/Django-6.0-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**djx** is a full‑featured social media platform inspired by X (formerly Twitter). Built with Django, it offers a sleek dark‑mode interface, real‑time interactions, nested replies, and a modern user experience that mimics the original platform while adding unique touches like cover‑image backgrounds for tweets.

---

## ✨ Features

- 🔐 **Authentication** – Register, login, logout, and profile editing
- ✍️ **Tweet Creation** – Post new tweets with a clean, minimal interface
- 💬 **Nested Replies** – Reply to tweets and replies with full threading support
- ❤️ **Like System** – AJAX‑powered likes with real‑time counter updates
- 👤 **User Profiles** – Custom avatars, cover images, bio, and stats (followers/following)
- 🔄 **Follow System** – Follow/unfollow users to build your timeline
- 📱 **Responsive Design** – Seamlessly works on mobile, tablet, and desktop
- 🌙 **Dark Theme** – Beautiful dark interface with accent colors (adjustable)
- 🎨 **Persian Localization** – Full RTL support with Persian typography and relative time
- 🖼️ **Cover‑Image Tweets** – Each tweet displays the author's cover image as background
- ⚡ **Optimized Performance** – Minimal JavaScript, native HTML/CSS, and Django best practices

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| **Backend** | Django 6.0, Python 3.12+ |
| **Frontend** | HTML5, CSS3 (Custom), Vanilla JavaScript (minimal) |
| **Database** | SQLite (default), easily switchable to PostgreSQL/MySQL |
| **Typography** | Vazirmatn (Persian), Inter (English), Lalezar/Yekan (Fancy) |
| **Icons** | Font Awesome 6 |
| **Localization** | Django i18n + custom Persian relative‑time filter |

---

## 📋 Prerequisites

- Python 3.12 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/parsa-mostafaie/django-djx.git
cd django-djx
```

### 2. Create and Activate a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to **http://127.0.0.1:8000**

---

## 🗺️ Routes & Pages

| URL Pattern | View | Description |
|-------------|------|-------------|
| `/` | `home_view` | Timeline of followed users + own tweets |
| `/create/` | `create_tweet_view` | Create a new tweet or reply |
| `/tweet/<id>/` | `tweet_detail_view` | Single tweet view with nested replies |
| `/like/<id>/` | `like_tweet_view` | AJAX like/unlike handler |
| `/follow/<username>/` | `follow_view` | Follow/unfollow a user |
| `/login/` | `login_view` | User login |
| `/register/` | `register_view` | User registration |
| `/logout/` | `logout_view` | User logout |
| `/edit-profile/` | `edit_profile_view` | Edit profile (name, bio, avatar, cover) |
| `/<username>/` | `profile_view` | Public profile page |

---

## 🎨 Key Design Decisions

### Dark Theme & UI
- **Color Palette**: `#0a0e17` (primary), `#141d2b` (secondary), `#6c5ce7` (brand)
- **Typography**: Vazirmatn (Persian) + Inter (English) + Lalezar/Yekan (fancy)
- **RTL Support**: Fully right‑to‑left optimized for Persian

### Tweet Cover Images
Each tweet uses the author's cover image as a subtle background overlay (opacity: 0.12), creating a personalized and visually engaging feed.

### Persian Time Display
A custom `persian_timesince()` utility converts Django's `timesince` output to fully Persian text (e.g., "۳ ساعت پیش" instead of "3 hours ago").

### Minimal JavaScript
Most interactions are handled via CSS transitions and native HTML. JavaScript is only used for:
- AJAX likes
- Mobile sidebar toggle
- Preventing event propagation on nested links

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Code Style
- Follow PEP 8 for Python
- Use descriptive variable names
- Comment complex logic
- Keep templates DRY (use includes and inheritance)

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by X (formerly Twitter)
- Fonts: [Vazirmatn](https://github.com/rastikerdar/vazirmatn), [Inter](https://fonts.google.com/specimen/Inter), [Lalezar](https://fonts.google.com/specimen/Lalezar)
- Icons: [Font Awesome](https://fontawesome.com/)
- Built with [Django](https://www.djangoproject.com/)

---

## 📬 Contact

- **Developer**: Parsa Mostafaie
- **Email**: pmostafaie1390@gmail.com
- **GitHub**: [@parsa-mostafaie](https://github.com/parsa-mostafaie)

---

⭐ **If you like this project, give it a star on GitHub!** ⭐