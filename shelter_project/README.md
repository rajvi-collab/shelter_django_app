# Shelter Donations - Django App (Ready to Run)

## Overview

This is a minimal Django web application for tracking donations and distributions for a local shelter.
It uses SQLite (no extra DB setup). The app includes pages to add donations, record distributions,
and view inventory and donor reports.

## Quick start

Requirements: Python 3.9+ and pip.

1. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. Install Django:
   ```
   pip install django
   ```

3. Generate migration files for the donations app:
   ```
   python manage.py makemigrations
   ```

4. Run migrations and start the server:
   ```
   python manage.py migrate
   python manage.py createsuperuser  # For Admin access
   python manage.py runserver
   ```
5. Add Donation Type from Admin site:
   ```
   - http://127.0.0.1:8000/admin/donations/donationtype/
   ```

5. Open your browser:
   - http://127.0.0.1:8000/donations/add/       → Add donations
   - http://127.0.0.1:8000/donations/distribute/ → Distribute donations
   - http://127.0.0.1:8000/donations/inventory/  → Inventory report
   - http://127.0.0.1:8000/donations/donors/     → Donor report
   - http://127.0.0.1:8000/admin/               → Admin site (create superuser with `python manage.py createsuperuser`)

## Notes

- Donor names are unique (duplicates ignored).
- The app prevents distributing more than available inventory and shows an error message.
- Bootstrap is loaded from CDN for decent default styling.

-- End.
