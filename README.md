# Simple Password Generator

## Overview

Simple Password Generator is a Python desktop application built with Tkinter that generates secure and customizable passwords. Users can specify the desired password length and choose whether to include uppercase letters, lowercase letters, numbers, and special characters. The application also evaluates the generated password's strength and allows users to copy it directly to the clipboard.

This project demonstrates the implementation of Python GUI development, random password generation, input validation, and basic cybersecurity principles.

---

## Features

- Generate secure random passwords
- Customize password length
- Include or exclude:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Password strength indicator
- Copy generated password to clipboard
- Input validation and error handling
- Clean and user-friendly graphical interface

---

## Technologies Used

- Python 3.x
- Tkinter
- Random Module
- String Module

---

## Project Structure

```text
Simple-Password-Generator/
│
├── main.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── screenshots/
│   ├── home.png
│   ├── generated_password.png
│   └── strength_indicator.png
│
└── assets/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Simple-Password-Generator.git
```

### Navigate to the Project Directory

```bash
cd Simple-Password-Generator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python main.py
```

---

## How It Works

1. Enter the desired password length.
2. Select the character types to include.
3. Click the **Generate** button.
4. The application generates a secure password.
5. View the password strength indicator.
6. Copy the password using the **Copy Password** button.

---

## Password Strength Evaluation

The application evaluates password strength based on:

- Password length
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of numbers
- Presence of special characters

Strength levels:

| Score | Strength |
|--------|----------|
| 0 – 2 | Weak |
| 3 – 4 | Medium |
| 5 | Strong |

---

## Screenshots

Add screenshots of the application inside the `screenshots` folder.

Example:

```text
screenshots/
├── home.png
├── generated_password.png
└── strength_indicator.png
```

---

## Learning Outcomes

This project helped strengthen knowledge in:

- Python programming
- GUI development using Tkinter
- Random password generation
- Input validation
- Clipboard operations
- Basic cybersecurity concepts
- Exception handling
- Desktop application development

---

## Future Enhancements

- Password history
- Password save/export functionality
- Dark mode
- Password visibility toggle
- QR code generation for passwords
- Custom symbol selection
- Password entropy calculation
- Modern themed user interface

---

## License

This project is licensed under the MIT License.

---

## Author

**Anshu Kumar Tiwari**

B.Tech – Computer Science and Engineering (Artificial Intelligence & Machine Learning)

GitHub: https://github.com/your-username

LinkedIn: https://www.linkedin.com/in/anshu-tiwari-29b056383/

---

If you find this project useful, consider starring the repository.
