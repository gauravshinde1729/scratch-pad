

# S3 Notes App

A minimal CLI notes app that stores everything in AWS S3 (via [Floci](https://floci.io/) local emulator). Built to learn how Python interacts with AWS services.

## Prerequisites

- Python 3.10+
- Docker (for Floci)
- [Floci CLI](https://floci.io/aws/#quickstart)
- AWS CLI

## Setup

**1. Start Floci**

```powershell
floci start
```

**2. Set environment variables (PowerShell)**

```powershell
$env:AWS_ENDPOINT_URL="http://localhost:4566"
$env:AWS_ACCESS_KEY_ID="test"
$env:AWS_SECRET_ACCESS_KEY="test"
$env:AWS_DEFAULT_REGION="us-east-1"
```

**3. Create the S3 bucket**

```powershell
aws s3 mb s3://test-bucket
```

**4. Create a virtual environment and install dependencies**

```powershell
python -m venv venv
.\venv\Scripts\Activate
pip install boto3
```

## Usage

```powershell
# Save a note
python main.py save

# List all notes
python main.py list

# Read a note
python main.py read

# Delete a note
python main.py delete
```

## Project Structure

```
task-queue-processor/
├── main.py          # CLI entry point + S3 operations
├── README.md
└── venv/            # Virtual environment (not committed)
```

## How It Works

Notes are stored as JSON files in an S3 bucket. Each note contains a title and body. The title is slugified to create the S3 object key.

```
save "My First Note" → my-first-note.json in S3
```

The app uses `boto3` to interact with S3, pointed at the local Floci emulator on `http://localhost:4566` instead of real AWS.

## Error Handling

The app uses custom exceptions for clean error reporting:

```python
NotesAppError          # Base exception
├── NoteNotFoundError  # Note doesn't exist in S3
└── InvalidTitleError  # Empty or invalid title
```

## Cleanup

```powershell
# Stop Floci
floci stop

# Deactivate venv
deactivate
```

## Tech Stack

- **Python** — CLI + app logic
- **boto3** — AWS SDK for Python
- **Floci** — local AWS emulator (S3)
- **AWS S3** — object storage for notes




<img width="959" height="542" alt="image" src="https://github.com/user-attachments/assets/e1bbb904-4652-4bfd-afce-31fd5ce3292a" />
