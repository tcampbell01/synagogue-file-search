import json
import boto3
from urllib.parse import quote

def lambda_handler(event, context):
    """Lambda function to list all files in S3 bucket for web interface"""
    
    s3 = boto3.client('s3')
    bucket_name = 'google-drivesync-backup'
    
    try:
        files = []
        paginator = s3.get_paginator('list_objects_v2')
        
        for page in paginator.paginate(Bucket=bucket_name, Prefix='drivesync/'):
            if 'Contents' in page:
                for obj in page['Contents']:
                    key = obj['Key']
                    
                    # Skip folders (keys ending with /)
                    if key.endswith('/'):
                        continue
                    
                    # Extract filename from path
                    filename = key.split('/')[-1]
                    
                    # Create download URL
                    download_url = f"https://{bucket_name}.s3.amazonaws.com/{quote(key)}"
                    
                    # Format file size
                    size_bytes = obj['Size']
                    if size_bytes < 1024:
                        size_str = f"{size_bytes} B"
                    elif size_bytes < 1024 * 1024:
                        size_str = f"{size_bytes / 1024:.1f} KB"
                    else:
                        size_str = f"{size_bytes / (1024 * 1024):.1f} MB"
                    
                    files.append({
                        'name': filename,
                        'path': key,
                        'size': size_str,
                        'url': download_url,
                        'modified': obj['LastModified'].isoformat()
                    })
        
        # Sort by filename
        files.sort(key=lambda x: x['name'].lower())
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',  # Enable CORS
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({
                'files': files,
                'total': len(files)
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }