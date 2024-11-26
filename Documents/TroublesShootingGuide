
---

# Troubleshooting Guide: Running the Chatbot and Frontend from README Instructions

This document provides solutions to common issues encountered when setting up and testing the chatbot software described in the repository. Follow these steps to resolve potential errors and ensure the application runs smoothly.

---

## **1. Setting Up the Virtual Environment**

### Issue:
Running `python -m venv venv` resulted in **"access denied"**.

### Solution:
Use the following command instead:
```bash
python -m venv myenv
```
This successfully creates a virtual environment named `myenv`.

---

## **2. Dependency Conflicts During Installation**

### Issue:
While installing dependencies with pip, the following error occurred:
```plaintext
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. 
This behaviour is the source of the following dependency conflicts. 
rasa 3.6.20 requires packaging <21.0, >=20.0, but you have packaging 24.1 which is incompatible.
```

### Solution:
Downgrade the `packaging` library to a compatible version:
```bash
pip install "packaging>=20.0,<21.0"
```

---

## **3. Training the Chatbot**

### Issue:
Running `rasa train` in the root folder resulted in:
```plaintext
ERROR: The path ‘config.yml’ does not exist. Please make sure to use the default location (‘config.yml’) or specify it with ‘--config’.
```

### Solution:
1. Navigate to the `Chatbot` folder, where `config.yml` is located:
   ```bash
   cd Chatbot
   ```
2. Run the training command again:
   ```bash
   rasa train
   ```
   Training works successfully when executed from the `Chatbot` folder.

---

## **4. Running Rasa Actions**

### Issue:
Running `rasa run actions` produced an error:
```plaintext
ERROR: Cannot import ‘LegacyVersion’ from 'packaging.version'.
```

### Solution:
This error occurs due to an incompatible version of the `packaging` library. To fix it:
1. Uninstall the existing `packaging` library:
   ```bash
   pip uninstall packaging
   ```
2. Install a compatible version:
   ```bash
   pip install "packaging>=20.0,<21.0"
   ```

---

## **5. Running the Frontend**

### Issue:
Running `python main.py` resulted in the following error:
```plaintext
ModuleNotFoundError: No module named ‘flask_babel’
```

### Solution:
Install the missing `flask_babel` package:
```bash
pip install flask_babel
```

### Verification:
Run the frontend again:
```bash
python main.py
```
The frontend should now start successfully.

---

## **Summary of Key Commands**
Here is a summary of key commands used to resolve issues:

1. **Create a virtual environment:**
   ```bash
   python -m venv myenv
   ```

2. **Resolve dependency conflicts:**
   ```bash
   pip install "packaging>=20.0,<21.0"
   ```

3. **Train the chatbot:**
   ```bash
   cd Chatbot
   rasa train
   ```

4. **Run Rasa actions:**
   ```bash
   rasa run actions
   ```

5. **Install missing dependencies:**
   ```bash
   pip install flask_babel
   ```

6. **Run the frontend:**
   ```bash
   python main.py
   ```

---

--- 
