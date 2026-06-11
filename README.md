# Spam Mail Detector

[![CI](https://github.com/samridhikamal2007-ai/spam_mail_detector/actions/workflows/ci.yml/badge.svg)](https://github.com/samridhikamal2007-ai/spam_mail_detector/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/samridhikamal2007-ai/spam_mail_detector)](https://github.com/samridhikamal2007-ai/spam_mail_detector/releases)

Simple project to train a spam vs ham classifier using public SMS/Email datasets, provide a REST API, and run a minimal web UI.

Quick start

1. Create and activate a Python virtual environment

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Download data and train

```powershell
python src/data_loader.py --download
python src/train.py
```

3. Run the API

```powershell
python app.py
```

4. Open http://127.0.0.1:5000

Deployment

- Push this repository to GitHub.
- Use Render, Heroku, or other cloud provider to deploy `app.py` as a web service (Gunicorn recommended).
- Alternatively, build a Docker image and push to a cloud container registry.

Deployment (Docker + GitHub Actions)

Prereqs: create GitHub repository and push this project.

1) Build & push image to GitHub Container Registry (GHCR)

- The included workflow `.github/workflows/docker-publish.yml` builds and pushes an image tagged `ghcr.io/<owner>/spam-detector:latest` on pushes to `main`.
- No secrets required for GHCR when using `GITHUB_TOKEN` for publishing packages, but you may need to enable GitHub Packages in your org settings.

Manual test (local Docker):
```powershell
docker build -t spam-detector:local .
docker run -p 8080:8080 spam-detector:local
# then open http://localhost:8080
```

2) Deploy to Heroku via GitHub Actions

- The workflow `.github/workflows/deploy-heroku.yml` deploys to Heroku on pushes to `main`.
- Set these repository secrets: `HEROKU_API_KEY`, `HEROKU_APP_NAME`, `HEROKU_EMAIL`.

3) Checklist before making the repo public

- [ ] Add a `LICENSE` file (e.g., MIT) if you want public reuse.
- [ ] Remove any sensitive data from `data/` or `models/` (they are gitignored).
- [ ] Add a concise `CONTRIBUTING.md` if you expect collaborators.
- [ ] Create GitHub repository and enable GitHub Pages or enable Actions as needed.
- [ ] Add repository secrets for Heroku if you want automatic deploys.

Optional: Render / Railway / DigitalOcean

- You can also deploy the Docker image to Render or Railway; both support connecting directly to a GitHub repo or a container registry.
