# HTTPS Deployment Configuration

This document explains how to configure a production server to serve a Django application securely using HTTPS, SSL/TLS certificates, and Nginx.

**Note**: For this ALX task, you do not need to actually deploy the application. This document serves as a reference for the deployment process.

---

## Step 1: Install Certbot and Obtain SSL Certificate

To enable HTTPS, the server must have a valid SSL/TLS certificate. The easiest way to obtain one is using Let's Encrypt and Certbot.

### Install Certbot and the Nginx plugin:
```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx -y
```

### Obtain and install an SSL certificate:

Replace `yourdomain.com` with your actual domain name.
```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

This command will:
- Verify domain ownership
- Download a free SSL certificate from Let's Encrypt
- Automatically configure Nginx for HTTPS
- Set up automatic HTTP to HTTPS redirection

---

## Step 2: Configure Nginx for Django Application

After obtaining the certificate, configure Nginx to serve your Django application over HTTPS.

### Create or edit the Nginx configuration file:
```bash
sudo nano /etc/nginx/sites-available/django_app
```

### Add the following configuration:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    add_header X-Frame-Options "DENY" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;

    location /static/ {
        alias /path/to/django/staticfiles/;
    }

    location /media/ {
        alias /path/to/django/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Enable the configuration:
```bash
sudo ln -s /etc/nginx/sites-available/django_app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## Step 3: Configure Firewall

Ensure your firewall allows HTTPS traffic.
```bash
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

---

## Step 4: Set Up Automatic Certificate Renewal

Let's Encrypt certificates expire after 90 days. Certbot automatically sets up a renewal process.

### Test automatic renewal:
```bash
sudo certbot renew --dry-run
```

### Manual renewal if needed:
```bash
sudo certbot renew
sudo systemctl reload nginx
```

---

## Summary

This configuration provides:
- Encrypted HTTPS connections using SSL/TLS certificates
- Automatic HTTP to HTTPS redirection
- Security headers to protect against common web attacks
- Automatic certificate renewal
- Proper proxy configuration for Django applications running behind Nginx