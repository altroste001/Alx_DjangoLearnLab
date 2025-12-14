# Deployment Documentation – Social Media API

## Hosting Platform
- Heroku

## Live URL
https://social-media-api-adef402aabbc.herokuapp.com/

## Deployment Steps
1. Project configured for production (DEBUG=False, ALLOWED_HOSTS set)
2. Gunicorn used as WSGI server
3. PostgreSQL database provisioned via Heroku
4. Static files handled using WhiteNoise
5. Application deployed using Heroku Git

## Environment Variables
- SECRET_KEY
- DATABASE_URL

## Maintenance & Monitoring
- Application logs monitored using `heroku logs --tail`
- Dependencies managed via `requirements.txt`

## Final Testing
- Admin panel accessible at `/admin`
- API endpoints tested and responsive
