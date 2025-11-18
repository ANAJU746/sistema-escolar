# Sistema Escolar

A simple school management system (Sistema Escolar) built with Python.

## Features

- Student management (registration, updates, queries)
- Course management
- Enrollment system
- Grade tracking

## Project Structure

```
sistema-escolar/
├── src/
│   ├── __init__.py
│   ├── student.py      # Student class and management
│   ├── course.py       # Course class and management
│   ├── enrollment.py   # Enrollment system
│   └── main.py         # Main application entry point
├── tests/
│   ├── __init__.py
│   ├── test_student.py
│   ├── test_course.py
│   └── test_enrollment.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ANAJU746/sistema-escolar.git
cd sistema-escolar
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main application:
```bash
python src/main.py
```

## Running Tests

```bash
python -m pytest tests/
```

## License

This project is open source and available under the MIT License.