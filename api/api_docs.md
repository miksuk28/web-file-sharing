# files.sukhanik.no - API Documentation

## Endpoints

### POST: api/upload
Uploads a new file

Headers:
```
token:  string
```

JSON-body:
```
{
    # Required:
    "filename": string,
    "file": fileObject,
    "qr": boolean,
    
    # One of these is required
    "deleteAfterDownloads": integer,
    "deleteAfterTime": integer

    # Optional
    "downloadLink": string,
    "description": string
}
```

### GET: api/uploads/\<fileId>
Return information about a file

URL-parameters:
```
fileId:   string
```

Headers:
```
token:  string
```

Returned JSON-body:
```
{
    "filename": string,
    "fileId": string,
    "qr": image,
    "ownerName": string,
    "ownerId": integer,
    "uploadedDate": string,
    "validUntill": [
        "downloads": integer,
        "time": integer
    ]
}
```

### GET: /dl/\<fileId>
Downloads a file  

URL-parameters:
```
fileId:  string
```

Returns:  
*file with filename*
