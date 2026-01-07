# Synagogue-file-search

AWS Lambda function that provides a web API to browse files stored in an S3 bucket. Originally designed for synagogue document management, this service lists files from the `google-drivesync-backup` bucket and provides file metadata.

## Features

- Lists all files from S3 bucket with `drivesync/` prefix
- Returns file metadata including name, size, and last modified date
- Generates S3 URLs for each file
- CORS-enabled for web interface integration
- Handles pagination for large file collections

## API Response

Returns JSON with:
- `files`: Array of file objects with name, path, size, S3 URL, and modified date
- `total`: Total number of files found

## Deployment

Deploy as AWS Lambda function with S3 read permissions for the target bucket.
