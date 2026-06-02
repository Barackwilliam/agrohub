# East Africa AgroHub Export Ltd - Website

A full-stack Django website with PostgreSQL (Supabase), premium UI, and full admin panel.

---

## 🚀 Quick Setup

### 1. Clone & Setup Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your actual values
```

### 2. Configure Supabase Database
1. Go to [supabase.com](https://supabase.com) → Create project
2. Go to **Settings → Database → Connection string → URI**
3. Copy the URI and paste in `.env` as `DATABASE_URL`

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 5. Load Initial Data
```bash
python manage.py shell < initial_data.py
```

### 6. Collect Static Files
```bash
python manage.py collectstatic
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit: http://localhost:8000

---

## 🔐 Admin Panel

URL: http://localhost:8000/admin/

**What you can manage:**
- ⚙️ **Site Settings** — Company info, tagline, about text, contact details, vision, mission
- 🖼️ **Hero Slides** — Homepage hero banners
- 🌾 **Products** — Add/edit/delete products with images and details
- 🏷️ **Product Categories** — Manage product categories
- ⭐ **Why Choose Us** — Edit the "Why Choose Us" section items
- 💎 **Core Values** — Edit company core values
- 📊 **Statistics** — Homepage stats numbers
- 🔗 **Social Links** — Social media links
- 📩 **Inquiries** — View and manage buyer inquiries from contact form

---

## 🌐 Deploy to Render

### Option 1: Using render.yaml (Recommended)
1. Push code to GitHub
2. Go to [render.com](https://render.com) → New → Blueprint
3. Connect your GitHub repo
4. Render will auto-detect `render.yaml` and deploy

### Option 2: Manual Render Setup
1. New Web Service → Connect GitHub repo
2. **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
3. **Start Command:** `gunicorn agrohub.wsgi:application`
4. Add environment variables from `.env.example`

### After Deployment
```bash
# SSH into Render shell and load initial data
python manage.py shell < initial_data.py
```

---

## 🔗 Domain Setup (eastafricaagrohub.co.tz)

1. On Render: Settings → Custom Domains → Add `eastafricaagrohub.co.tz` and `www.eastafricaagrohub.co.tz`
2. Render gives you DNS records (CNAME or A record)
3. At your domain registrar (where .co.tz is registered), add those DNS records
4. Wait 24-48 hours for propagation

---

## 📁 Project Structure

```
agrohub/
├── agrohub/           # Main Django config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/              # Homepage, About, Contact views
├── products/          # Products & Categories
├── inquiries/         # Contact form & inquiry management
├── siteconfig/        # Site-wide settings (CMS)
├── templates/         # All HTML templates
│   ├── base.html      # Base template with navbar & footer
│   ├── core/
│   │   ├── home.html
│   │   ├── about.html
│   │   └── contact.html
│   └── products/
│       └── list.html
├── static/            # Static files (CSS, JS, images)
├── initial_data.py    # Initial data setup script
├── requirements.txt
├── render.yaml        # Render deployment config
└── .env.example       # Environment variables template
```

---

## 📸 Adding Product Images

1. Login to Admin: `/admin/`
2. Go to **Products → Products**
3. Click any product → Upload image
4. Save

For production, images are stored in Render's disk or you can configure Supabase Storage.

---

## 🆘 Troubleshooting

**Database connection error:**
- Check `DATABASE_URL` in `.env`
- Make sure Supabase project is active
- For local development, you can use `sqlite:///db.sqlite3`

**Static files not loading:**
- Run `python manage.py collectstatic`
- Check `STATIC_ROOT` setting

**Admin CSS broken:**
- Make sure `jazzmin` is in `INSTALLED_APPS` (before `django.contrib.admin`)
- Run `python manage.py collectstatic`
