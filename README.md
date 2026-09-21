# Cryptography Algorithms Implementation

**Internship Project**  
*Codec Technologies 1-Month Cyber Security Internship*  
*Submitted by: B.E. Cybersecurity Student*

---

## 1. Project Title
**Cryptography Algorithms Implementation & Interactive Security Dashboard**

## 2. Internship/Project Objective
The objective of this project is to implement, demonstrate, and analyze popular cryptography algorithms (**AES**, **RSA**, and **SHA-256**) alongside **OpenSSL** command-line tools. This hands-on project serves to build a deep, practical understanding of encryption, decryption, data integrity verification, key exchange, and secure communication protocols in a safe, educational, local environment.

## 3. Project Description
This application is a complete, interactive, web-based Cryptography Dashboard built with **Python (Flask)** on the backend and a premium **Dark Glassmorphism UI** on the frontend. Instead of simple command-line prompts, this dashboard provides a visual, real-time playground where students and evaluators can interact with:
*   **AES-256-GCM** (Symmetric Authenticated Encryption)
*   **RSA-2048 with OAEP Padding** (Asymmetric Key Cryptography)
*   **SHA-256** (One-way Hashing & Avalanche Effect comparison)
*   **OpenSSL Command Sandbox** (Executing local OpenSSL CLI commands securely via Python subprocesses)

Each section includes real-time inputs, outputs, console logs, and step-by-step educational explanations written in plain English.

---

## 4. Features
*   **AES Tab**: Generates a secure, cryptographically random 256-bit AES key. Encrypts plaintext using AES-GCM and displays ciphertext, nonce, and authentication tag in hexadecimal format. Decrypts and verifies the integrity of the ciphertext using GCM authentication.
*   **RSA Tab**: Generates a mathematically linked public/private key pair (2048-bit keys) and displays them in standard PEM format. Encrypts data using the public key and decrypts it using the private key.
*   **SHA-256 Tab**: Computes hashes in real-time. Features an **Avalanche Effect Visualizer** that compares two slightly different strings (e.g. differing by only a single character) and displays the count and percentage of characters that changed in the resulting hashes.
*   **OpenSSL sandbox**: Runs safe, pre-configured OpenSSL CLI commands (key generation, SHA-256 hashing, AES-256-CBC encryption/decryption) and captures stdout/stderr to show terminal-equivalent operations.
*   **Unit Test Suite**: Includes 16 comprehensive tests verifying key handling, invalid inputs, integrity tampering, and correct cryptographic operations.

---

## 5. Technologies & Tools Used
1.  **Python 3**: Main programming language.
2.  **Flask**: A micro-framework used to create the local web server and expose secure REST APIs for cryptography operations.
3.  **PyCryptodome**: A modern, actively maintained cryptographic library for Python. It provides high-entropy random key generation, AES-GCM, and RSA-OAEP implementations.
4.  **HTML5, Vanilla CSS3, & Modern Javascript**: Used to build a responsive, high-end dark glassmorphism dashboard UI.
5.  **OpenSSL**: Used via Python subprocesses to execute command-line cryptographic examples.

---

## 6. Installation Requirements
To run this project, you need:
*   **Python 3.8 or higher** installed on your system.
*   **pip** (Python package installer).
*   **OpenSSL** (optional, for the OpenSSL tab execution). If OpenSSL is not in your system path, the dashboard will display a friendly instruction on how to install it, while the rest of the Python-based tabs (AES, RSA, SHA) will function perfectly.

---

## 7. Installation Steps

### Step 1: Clone or Download the Project
Ensure the project files are located in your workspace directory:
```text
cryptography_project/
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   ├── __init__.py
│   ├── app.py
│   ├── crypto_aes.py
│   ├── crypto_rsa.py
│   ├── crypto_sha.py
│   └── openssl_demo.py
├── tests/
│   ├── __init__.py
│   ├── test_aes.py
│   ├── test_rsa.py
│   ├── test_sha.py
│   └── test_openssl.py
├── requirements.txt
├── run.py
└── README.md
```

### Step 2: Install Dependencies
Open your terminal (PowerShell, Command Prompt, or terminal of your choice), navigate to the project directory, and run:
```bash
pip install -r requirements.txt
```
This command will automatically download and install `Flask` and `pycryptodome`.

---

## 8. How to Run the Project

### Starting the Web Dashboard
From your terminal in the project directory, run:
```bash
python run.py
```
You will see output indicating the server has started:
```text
============================================================
  Cryptography Algorithms Implementation Project Web Server
  Internship: Codec Technologies 1-Month Cyber Security
============================================================
  Running locally at: http://127.0.0.1:5000/
  Press Ctrl+C to stop the server.
============================================================
```

Open your web browser and go to: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 9. Understanding the Cryptography Concepts

### A. Advanced Encryption Standard (AES)
*   **What it is**: AES is a **symmetric key algorithm**, which means the **same key** is used to encrypt and decrypt the data. It is extremely fast and is the global standard used by governments and enterprises.
*   **How GCM Mode Works**:
    *   **AES-GCM (Galois/Counter Mode)** is an *authenticated encryption* mode. It does two things: it hides the message (confidentiality) and guarantees the message hasn't been altered (integrity/authenticity).
    *   **Nonce (Number used Once)**: A random 12-byte initialization vector. If you encrypt the same word twice with the same key, a different nonce ensures the output looks completely different. You must never reuse a nonce with the same key.
    *   **Authentication Tag**: A 16-byte cryptographic code generated during encryption. When decrypting, AES-GCM recalculates this tag. If even one letter of the ciphertext was changed by an attacker, the tags won't match, and the decryption will fail.

### B. Rivest-Shamir-Adleman (RSA)
*   **What it is**: RSA is an **asymmetric key algorithm**. It uses a **mathematically linked key pair**:
    *   **Public Key**: Can be shared with anyone. Used to **encrypt** data.
    *   **Private Key**: Must be kept secret. Only this key can **decrypt** data encrypted by the matching public key.
*   **Difference between Public and Private Keys**:
    *   Think of the public key as an open padlock. Anyone can use it to lock a box (encrypt a message), but only the person holding the private key (the key owner) has the physical key to unlock it (decrypt the message).
*   **Padding (OAEP)**: Optimal Asymmetric Encryption Padding. Raw RSA is weak to mathematical attacks. OAEP adds structured randomness to the plaintext before encrypting, making it highly secure.
*   **Note**: Because RSA requires complex prime number math, it is slow. In secure communication protocols (like HTTPS), RSA is used to exchange a temporary AES key, and then AES is used for the rest of the conversation.

### C. Secure Hash Algorithm (SHA-256)
*   **What Hashing is**: Hashing is a **one-way function**. It takes an input of any size and converts it into a fixed-length string of characters (for SHA-256, it is always a 64-character hexadecimal string representing 256 bits).
*   **How Hashing differs from Encryption**:
    *   Encryption is a **two-way** process (Plaintext $\leftrightarrow$ Ciphertext).
    *   Hashing is a **one-way** process (Plaintext $\rightarrow$ Hash). You cannot "decrypt" or reverse a hash back to its original input.
*   **Avalanche Effect**: If you change just one character in the input (e.g., changing "Password123" to "password123"), the resulting hash changes completely. The dashboard's comparison tool shows that around 50% or more of the hash changes, indicating that the new hash has no correlation to the old one.

---

## 10. OpenSSL Demonstration
To show your evaluator how command-line cryptography works, the dashboard's **OpenSSL tab** allows running these commands locally. Here is what each command does:

1.  **Generate Secure Random Bytes**:
    ```bash
    openssl rand -hex 16
    ```
    *Explainer*: Generates 16 random bytes (represented as 32 hex characters) using OpenSSL's secure random number generator. Used for generating symmetric keys.
2.  **Calculate Message Hash**:
    ```bash
    echo -n "message" | openssl dgst -sha256
    ```
    *Explainer*: Passes the string to OpenSSL's digest tool (`dgst`) to calculate and output its SHA-256 hash.
3.  **Symmetric Encryption (AES-256-CBC)**:
    ```bash
    echo "message" | openssl enc -aes-256-cbc -a -pbkdf2 -k "mypassword"
    ```
    *Explainer*: Encrypts input using AES-256 in CBC mode. The `-pbkdf2` flag derives a secure key from the password `"mypassword"` using a password-based key derivation function. The `-a` flag encodes the output in Base64 (printable ASCII).
4.  **Symmetric Decryption**:
    ```bash
    echo "base64_ciphertext" | openssl enc -aes-256-cbc -d -a -pbkdf2 -k "mypassword"
    ```
    *Explainer*: Decrypts (`-d`) the Base64 (`-a`) encoded ciphertext using the password `"mypassword"`.

---

## 11. Testing

### Run Automated Unit Tests
The project contains 16 unit tests that check for AES, RSA, SHA, invalid inputs, and tampered data.
To execute all tests, open your terminal in the project directory and run:
```bash
python -m unittest discover -s tests
```

You should see output similar to this:
```text
................
----------------------------------------------------------------------
Ran 16 tests in 5.8s

OK
```

---

## 12. Screenshots Section (For Your Report)
When documenting this project for your internship folder, you can take screenshots of:
1.  **AES Panel**: Generating key, encrypting text, tampering with ciphertext in the decryption box to show how authentication tag verification fails.
2.  **RSA Panel**: Generating the public/private key block, encrypting with public key, and decrypting with private key.
3.  **SHA-256 Panel**: Live typing to show real-time hash updates, and showing the Avalanche Effect comparison card.
4.  **OpenSSL Panel**: Output of generating random bytes or running AES encryption command.

---

## 13. Security Considerations & Limitations
*   **Educational Use Only**: This project is built for a local educational sandbox environment. It does not run HTTPS or include authentication for the local UI port.
*   **Memory Secrets**: Keys are generated and stored in memory or in browser forms. In a production environment, private keys must be stored in secure Key Vaults or hardware security modules (HSMs).
*   **No Password Hardcoding**: All password inputs in the OpenSSL sandbox are custom-entered by the user and never hardcoded in the source code.

---

## 14. Future Improvements
*   **HTTPS Support**: Configure Flask with a self-signed SSL/TLS certificate to demonstrate secure data-in-transit (HTTPS).
*   **Digital Signatures**: Implement RSA private key signing and public key signature verification.
*   **Key Exchange Demo**: Visually demonstrate Diffie-Hellman Key Exchange steps.
*   **File Hashing**: Add a drag-and-drop file upload to calculate SHA-256 checksums of actual files.

---

## 15. How to Publish This Project on GitHub
To submit this project as part of your internship portfolio, follow these steps to upload it to your GitHub profile:

1.  **Create a GitHub Account**: Sign up at [github.com](https://github.com/) if you haven't already.
2.  **Install Git**: Make sure Git is installed on your local computer.
3.  **Initialize Git Repository Locally**:
    Open terminal in the project folder and run:
    ```bash
    git init
    ```
4.  **Add a `.gitignore` file**:
    Create a file named `.gitignore` in the project root to prevent uploading temporary cache files. Put this content inside it:
    ```text
    __pycache__/
    *.pyc
    .venv/
    env/
    ```
5.  **Commit the Code**:
    ```bash
    git add .
    git commit -m "Initial commit: Codec Technologies Cryptography Internship Project"
    ```
6.  **Create a New Repository on GitHub**:
    *   Click "New" on GitHub.
    *   Name it `cryptography-algorithms-implementation`.
    *   Keep it Public, do **not** initialize with a README, gitignore, or license.
7.  **Link and Push**:
    Copy the commands displayed on GitHub and run them in your terminal (replacing your username):
    ```bash
    git remote add origin https://github.com/YOUR_GITHUB_USERNAME/cryptography-algorithms-implementation.git
    git branch -M main
    git push -u origin main
    ```
8.  Your project is now live on GitHub! You can share the repository link with your evaluator.
