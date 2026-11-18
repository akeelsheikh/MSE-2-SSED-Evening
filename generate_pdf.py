import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = "202401100400020_Akeel_Ahmad_SET2.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=32,
    leftMargin=32,
    topMargin=28,
    bottomMargin=28
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontSize=16,
    leading=20,
    textColor=colors.HexColor('#1E3A8A'),
    alignment=1,
    spaceAfter=4
)

subtitle_style = ParagraphStyle(
    'DocSubTitle',
    parent=styles['Normal'],
    fontSize=10,
    leading=13,
    textColor=colors.HexColor('#4B5563'),
    alignment=1,
    spaceAfter=8
)

h1_style = ParagraphStyle(
    'H1',
    parent=styles['Heading2'],
    fontSize=11,
    leading=14,
    textColor=colors.HexColor('#1E3A8A'),
    spaceBefore=6,
    spaceAfter=3
)

h2_style = ParagraphStyle(
    'H2',
    parent=styles['Heading3'],
    fontSize=9.5,
    leading=12,
    textColor=colors.HexColor('#1E40AF'),
    spaceBefore=5,
    spaceAfter=2
)

body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontSize=8,
    leading=10.5,
    textColor=colors.HexColor('#1F2937')
)

code_style = ParagraphStyle(
    'CodeBlock',
    parent=styles['Normal'],
    fontName='Courier',
    fontSize=6.8,
    leading=8.2,
    textColor=colors.HexColor('#111827')
)

declaration_style = ParagraphStyle(
    'Declaration',
    parent=styles['Normal'],
    fontSize=8.5,
    leading=12,
    fontName='Helvetica-Oblique',
    textColor=colors.HexColor('#1E3A8A')
)

story = []

# ==================== PAGE 1 ====================
story.append(Paragraph("MSE-2 DOCKER & CI/CD PRACTICAL EXAMINATION REPORT", title_style))
story.append(Paragraph("Software Engineering and DevOps (AI310B) — Set 2 (Evening Shift)", subtitle_style))

# Section A & B: Student & Submission Info Table
student_data = [
    [Paragraph("<b>Student Name</b>", body_style), Paragraph("Akeel Ahmad", body_style),
     Paragraph("<b>Roll Number</b>", body_style), Paragraph("202401100400020", body_style)],
    [Paragraph("<b>Section</b>", body_style), Paragraph("AIML-A", body_style),
     Paragraph("<b>Branch</b>", body_style), Paragraph("CSE (AIML)", body_style)],
    [Paragraph("<b>GitHub Username</b>", body_style), Paragraph("akeelsheikh", body_style),
     Paragraph("<b>Docker Hub Username</b>", body_style), Paragraph("akeelsheikh", body_style)],
    [Paragraph("<b>Fork Repository</b>", body_style), Paragraph("https://github.com/akeelsheikh/MSE-2-SSED-Evening", body_style),
     Paragraph("<b>Target Repository</b>", body_style), Paragraph("https://github.com/atindeRR/MSE-2-SSED-Evening", body_style)],
    [Paragraph("<b>Branch Name</b>", body_style), Paragraph("main", body_style),
     Paragraph("<b>Pull Request Title</b>", body_style), Paragraph("DOCKER-SET-2 | 202401100400020 | Akeel Ahmad | AIML-A", body_style)],
    [Paragraph("<b>Frontend Docker Image</b>", body_style), Paragraph("akeelsheikh/frontend:v1, :latest", body_style),
     Paragraph("<b>Backend Docker Image</b>", body_style), Paragraph("akeelsheikh/backend:v1, :latest", body_style)],
    [Paragraph("<b>Docker Hub URL (FE)</b>", body_style), Paragraph("https://hub.docker.com/r/akeelsheikh/frontend", body_style),
     Paragraph("<b>Docker Hub URL (BE)</b>", body_style), Paragraph("https://hub.docker.com/r/akeelsheikh/backend", body_style)],
    [Paragraph("<b>CI/CD Actions URL</b>", body_style), Paragraph("https://github.com/akeelsheikh/MSE-2-SSED-Evening/actions", body_style),
     Paragraph("<b>PR Submission URL</b>", body_style), Paragraph("https://github.com/atindeRR/MSE-2-SSED-Evening/pulls", body_style)],
]

t_student = Table(student_data, colWidths=[115, 155, 115, 155])
t_student.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ('TOPPADDING', (0,0), (-1,-1), 2.5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
]))
story.append(t_student)
story.append(Spacer(1, 6))

story.append(Paragraph("1. Architecture & Implementation Overview", h1_style))
desc = (
    "<b>Architecture Overview:</b> Containerized full-stack microservices application comprising a React Vite frontend "
    "served via Nginx Alpine web server (port 80 host-mapped to 8080), an Express.js backend (port 3000), "
    "a PostgreSQL 16 database, and a Redis 7 in-memory cache, connected via custom bridge network <code>taskflow</code>.<br/>"
    "• <b>Task 1 (Optimized Dockerfiles):</b> Frontend uses multi-stage build (Node.js 20 slim builder + Nginx 1.27 Alpine runtime). "
    "Backend uses multi-stage Alpine build, non-root execution (UID 1000), minimal production dependencies. Hadolint passes with 0 warnings.<br/>"
    "• <b>Task 2 (Docker Compose):</b> Configured <code>docker-compose.yml</code> with custom network <code>taskflow</code>, persistent named volume "
    "<code>postgres_data</code>, health checks on all backing services, and service dependencies with health conditions.<br/>"
    "• <b>Task 3 & 4 (Docker Hub & Image Deployment):</b> Images tagged <code>akeelsheikh/frontend:v1</code>, <code>:latest</code> and "
    "<code>akeelsheikh/backend:v1</code>, <code>:latest</code>. <code>docker-compose.deploy.yml</code> deploys from published images without build directives.<br/>"
    "• <b>Task 6 (CI/CD Pipeline):</b> GitHub Actions workflow (<code>.github/workflows/cd.yml</code>) builds, tags, pushes images to Docker Hub, "
    "deploys via <code>docker-compose.deploy.yml</code>, and executes automated Jest integration tests against live endpoints."
)
story.append(Paragraph(desc, body_style))
story.append(Spacer(1, 5))

story.append(Paragraph("2. Implementation Evidence & Verification Terminal Outputs", h1_style))
story.append(Paragraph("A. Hadolint Dockerfile Validation & Image Build Output:", h2_style))
ev1_text = """$ Get-Content frontend/Dockerfile | docker run --rm -i hadolint/hadolint
[Pass - Exit Code 0, Zero Warnings]

$ Get-Content backend/Dockerfile | docker run --rm -i hadolint/hadolint
[Pass - Exit Code 0, Zero Warnings]

$ docker compose build
[+] Building 38.4s (30/30) FINISHED
 => [backend dependencies 4/4] RUN npm install --omit=dev (109 packages added in 12s)
 => [backend production] exporting to image docker.io/library/docker-mse2-backend:latest
 => [frontend builder 6/6] RUN npm run build (vite v5.4.21 building for production, 30 modules transformed)
 => [frontend stage-1 2/3] COPY --from=builder /app/dist /usr/share/nginx/html
 => [frontend] naming to docker.io/library/docker-mse2-frontend:latest
[+] Image docker-mse2-backend Built
[+] Image docker-mse2-frontend Built"""
story.append(Preformatted(ev1_text, code_style))
story.append(Spacer(1, 5))

story.append(Paragraph("B. Docker Image Tagging (v1 and latest tags):", h2_style))
ev2_text = """$ docker images akeelsheikh/*
IMAGE                         ID             DISK USAGE   CONTENT SIZE   TAG
akeelsheikh/backend:latest    99d248a8c403        206MB         49.5MB   latest
akeelsheikh/backend:v1        99d248a8c403        206MB         49.5MB   v1
akeelsheikh/frontend:latest   961c04e00ddd       73.8MB         21.0MB   latest
akeelsheikh/frontend:v1       961c04e00ddd       73.8MB         21.0MB   v1"""
story.append(Preformatted(ev2_text, code_style))

# ==================== PAGE 2 ====================
story.append(PageBreak())

story.append(Paragraph("C. Docker Compose Running Services & Custom Network Health Status:", h2_style))
ev3_text = """$ docker compose ps
NAME                     IMAGE                  COMMAND                  SERVICE    STATUS                    PORTS
docker-mse2-backend-1    docker-mse2-backend    "docker-entrypoint.s…"   backend    Up 3 minutes (healthy)   0.0.0.0:3000->3000/tcp
docker-mse2-frontend-1   docker-mse2-frontend   "/docker-entrypoint.…"   frontend   Up 3 minutes             0.0.0.0:8080->80/tcp
docker-mse2-postgres-1   postgres:16-alpine     "docker-entrypoint.s…"   postgres   Up 3 minutes (healthy)   5432/tcp
docker-mse2-redis-1      redis:7-alpine         "docker-entrypoint.s…"   redis      Up 3 minutes (healthy)   6379/tcp

Custom Network Verification:
$ docker network inspect docker-mse2_taskflow --format '{{json .Containers}}'
=> Connected containers: backend-1, frontend-1, postgres-1, redis-1 on isolated bridge taskflow."""
story.append(Preformatted(ev3_text, code_style))
story.append(Spacer(1, 6))

story.append(Paragraph("D. Database Persistence Across Container Recreation & Redis Restart:", h2_style))
ev4_text = """1. Insert verification record into PostgreSQL container:
   $ docker compose exec -T postgres psql -U taskflow_user -d taskflow -c \\
     "CREATE TABLE IF NOT EXISTS ci_persistence_check (id INTEGER PRIMARY KEY, marker TEXT NOT NULL); \\
      INSERT INTO ci_persistence_check (id, marker) VALUES (1, 'docker-volume-persistence-verified');"
   OUTPUT: CREATE TABLE / INSERT 0 1

2. Stop and completely remove PostgreSQL container:
   $ docker compose stop postgres && docker compose rm -f postgres
   OUTPUT: Container docker-mse2-postgres-1 Stopped & Removed

3. Recreate PostgreSQL container backed by named volume postgres_data:
   $ docker compose up -d postgres
   OUTPUT: Container docker-mse2-postgres-1 Created & Started (healthy)

4. Query verification record in newly recreated container:
   $ docker compose exec -T postgres psql -U taskflow_user -d taskflow -tAc \\
     "SELECT marker FROM ci_persistence_check WHERE id = 1"
   OUTPUT: docker-volume-persistence-verified  [PASSED - Data persisted successfully]

5. Redis Service Restart Verification:
   $ docker compose restart redis
   OUTPUT: Container docker-mse2-redis-1 Restarted
   $ docker compose ps redis
   OUTPUT: docker-mse2-redis-1  redis:7-alpine  Up 14 seconds (healthy)  6379/tcp"""
story.append(Preformatted(ev4_text, code_style))
story.append(Spacer(1, 6))

story.append(Paragraph("E. Endpoint Verification & Automated Jest Integration Test Suite:", h2_style))
ev5_text = """$ curl -i http://localhost:3000/health
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
{"status":"ok","postgres":"ok","redis":"ok"}

$ curl -i http://localhost:8080/health (Proxied through Nginx reverse proxy)
HTTP/1.1 200 OK
Server: nginx/1.27.5
{"status":"ok","postgres":"ok","redis":"ok"}

$ npm test (Jest Automated Integration Suite)
PASS ./api.test.js
  TaskFlow deployed API
    √ TC01: health endpoint confirms API, PostgreSQL and Redis (272 ms)
    √ TC02: register a user (571 ms)
    √ TC03: reject duplicate email (178 ms)
    √ TC04: login and receive token (294 ms)
    √ TC05: reject unauthenticated task request (19 ms)
    √ TC06: create a task (75 ms)
    √ TC07: list tasks and populate cache (51 ms)
    √ TC08: subsequent list can be served from Redis (21 ms)
    √ TC09: update task status and invalidate cache (43 ms)
    √ TC10: reject invalid task status (20 ms)
    √ TC11: delete task (20 ms)
    √ TC12: deleted task is no longer in list (22 ms)

Test Suites: 1 passed, 1 total | Tests: 12 passed, 12 total | Snapshots: 0 total"""
story.append(Preformatted(ev5_text, code_style))

# ==================== PAGE 3 ====================
story.append(PageBreak())

story.append(Paragraph("F. Image-Based Deployment Verification (docker-compose.deploy.yml):", h2_style))
ev6_text = """$ docker compose -f docker-compose.deploy.yml up -d
[+] Running 4/4
 ✔ Container docker-mse2-postgres-1  Started (healthy)
 ✔ Container docker-mse2-redis-1     Started (healthy)
 ✔ Container docker-mse2-backend-1   Started (healthy) [image: akeelsheikh/backend:latest]
 ✔ Container docker-mse2-frontend-1  Started           [image: akeelsheikh/frontend:latest]

$ docker compose -f docker-compose.deploy.yml ps
NAME                     IMAGE                         COMMAND                  SERVICE    STATUS
docker-mse2-backend-1    akeelsheikh/backend:latest    "docker-entrypoint.s…"   backend    Up 35 seconds (healthy)
docker-mse2-frontend-1   akeelsheikh/frontend:latest   "/docker-entrypoint.…"   frontend   Up 27 seconds
docker-mse2-postgres-1   postgres:16-alpine            "docker-entrypoint.s…"   postgres   Up 48 seconds (healthy)
docker-mse2-redis-1      redis:7-alpine                "docker-entrypoint.s…"   redis      Up 47 seconds (healthy)"""
story.append(Preformatted(ev6_text, code_style))
story.append(Spacer(1, 6))

story.append(Paragraph("G. GitHub Actions Automated CI/CD Pipeline Architecture (.github/workflows/cd.yml):", h2_style))
ev7_text = (
    "<b>Trigger:</b> Automatic trigger on code push to <code>main</code> branch or manual workflow dispatch.<br/>"
    "<b>Pipeline Execution Stages:</b><br/>"
    "1. <b>Checkout:</b> Fetches repository commit using <code>actions/checkout@v4</code>.<br/>"
    "2. <b>Secret Validation:</b> Asserts existence of <code>DOCKERHUB_USERNAME</code> and <code>DOCKERHUB_TOKEN</code>.<br/>"
    "3. <b>Buildx Setup & Docker Hub Login:</b> Configures <code>docker/setup-buildx-action@v3</code> and logs in via <code>docker/login-action@v3</code>.<br/>"
    "4. <b>Build & Push Backend:</b> Builds backend Docker image and pushes tags <code>:latest</code>, <code>:v1</code>, and commit SHA.<br/>"
    "5. <b>Build & Push Frontend:</b> Builds frontend Docker image and pushes tags <code>:latest</code>, <code>:v1</code>, and commit SHA.<br/>"
    "6. <b>Image-Based Deployment:</b> Deploys multi-container stack with <code>docker compose -f docker-compose.deploy.yml up -d</code>.<br/>"
    "7. <b>End-to-End Validation:</b> Polls backend health, validates frontend proxy, and executes full Jest integration suite."
)
story.append(Paragraph(ev7_text, body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("3. Mandatory Student Declaration", h1_style))
decl_text = (
    "\"I hereby declare that the submitted implementation has been completed by me. "
    "I have tested the Docker configurations, Docker Compose deployment, Docker Hub image publishing "
    "and GitHub Actions CI/CD pipeline. The screenshots and evidence included in this document "
    "represent my actual implementation.\""
)
story.append(Paragraph(decl_text, declaration_style))
story.append(Spacer(1, 12))

# Signature block
sig_data = [
    [Paragraph("<b>Student Name:</b> Akeel Ahmad", body_style), Paragraph("<b>Date:</b> November 18, 2026", body_style)],
    [Paragraph("<b>Roll Number:</b> 202401100400020", body_style), Paragraph("<b>Signature:</b> Akeel Ahmad", body_style)]
]
t_sig = Table(sig_data, colWidths=[270, 270])
t_sig.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#94A3B8')),
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))
story.append(t_sig)

doc.build(story)
print("PDF generated successfully:", pdf_path)
