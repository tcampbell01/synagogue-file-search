# Synagogue File Search

A complete file browsing solution for synagogue document management, consisting of an AWS Lambda API backend and a web interface frontend.

## Components

### Lambda Function (`lambda_function.py`)
AWS Lambda function that provides a REST API to browse files stored in the `google-drivesync-backup` S3 bucket.

**Features:**
- Lists all files from S3 bucket with `drivesync/` prefix
- Returns file metadata including name, path, size, and last modified date
- Generates S3 URLs for each file
- CORS-enabled for web interface integration
- Handles pagination for large file collections

**API Response:**
```json
{
  "files": [
    {
      "name": "filename.pdf",
      "path": "drivesync/folder/filename.pdf",
      "size": "1.2 MB",
      "url": "https://bucket.s3.amazonaws.com/path",
      "modified": "2024-01-01T12:00:00"
    }
  ],
  "total": 1
}
```

### Web Interface (`index.html`)
Static HTML page that provides a user-friendly interface to search and browse files.

**Features:**
- Real-time search filtering
- Responsive design
- File count statistics
- Clean, accessible interface

## Deployment

1. Deploy `lambda_function.py` as AWS Lambda function with S3 read permissions
2. Set up API Gateway to trigger the Lambda function
3. Host `index.html` on any web server or S3 static website
4. Update the `API_URL` in `index.html` to point to your API Gateway endpoint
