# Secure Message Hiding in Images

## Overview
**Secure Message Hiding in Images** is a web-based steganography application that allows users to hide secret text messages inside images and retrieve them using a password.  
All processing is done in real time, and no user data is stored.

## Key Features
- Hide text messages inside images securely
- Password-protected encoding and decoding
- No database or file storage
- Simple and user-friendly web interface
- Processes images in memory only

## How It Works

### Encoding
- The user uploads an image
- The user enters a secret message
- The user sets a password
- The message is embedded into the image using steganography

### Decoding
- The user uploads the encoded image
- The user enters the same password
- The hidden message is extracted and displayed

## Technology Stack
- **Python**
- **Flask**
- **OpenCV**
- **HTML, CSS, JavaScript**
- **Gunicorn (for production deployment)**

## Privacy and Security
- No images are stored
- No messages are saved
- No passwords are stored
- All data exists only during the request lifecycle

## Hosting
- Hosted on **Render**
- Uses **Gunicorn** as the production server
- Automatically binds to the port provided by the hosting platform
