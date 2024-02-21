# Architecture
<img width="482" alt="image" src="https://github.com/piyu18/pdf_chat_openai/assets/20923057/7157cea7-8b3c-4588-96cb-4f97b4e810ab">

# First Time Setup

# Create the venv virtual environment
```
conda create -p venv python=3.11 -y
```

# Activate the virtual environment
```
conda activate venv/
```

# Install dependencies
```
pip install -r requirements.txt
```

# Initialize the database
```
flask --app app.web init-db
```


### To run the Python server


```
inv dev
```

