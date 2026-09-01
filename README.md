<div align="center">

<img src="./assets/banner.svg" alt="Sunil Kumar Reddy — Python Software Engineer" width="100%"/>

<p>
  <a href="https://www.linkedin.com/in/sunilreddy-softwarengineer/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:sunilsoftwarengineer@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://leetcode.com/u/Sunilsoftwarengineer/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/></a>
</p>

📍 Bengaluru, Karnataka &nbsp;•&nbsp; 🟢 Immediate Joiner &nbsp;•&nbsp; ✈️ Open to relocate (Hyderabad)

</div>

<br>

## 📡 Live Stats
*Not a static badge — this table is regenerated daily by [`scripts/update_readme.py`](./scripts/update_readme.py) via [`.github/workflows/update-readme.yml`](./.github/workflows/update-readme.yml), pulling real numbers from the GitHub API.*

<!-- LIVE-STATS:START -->
| Metric | Value |
|---|---|
| Public repos | 3 |
| Total stars earned | 0 |
| Total forks | 0 |
| Most-used language | Dockerfile |

<sub>Auto-updated 2026-09-01 03:04 UTC by `scripts/update_readme.py`</sub>
<!-- LIVE-STATS:END -->

<br>

## 🖥️ `~/whoami`

```python
class PythonSoftwareEngineer:
    def __init__(self):
        self.name = "Sunil Kumar Reddy"
        self.role = "Python Software Engineer"
        self.location = "Bengaluru, India"
        self.core_stack = ["Python", "FastAPI", "SQLAlchemy", "Celery", "LangChain", "AWS"]
        self.believes = "Boring, observable systems beat clever, fragile ones."
        self.currently = ["Scaling RAG pipelines", "Vector search with pgvector", "AIOps tooling"]

    def say_hi(self) -> str:
        return "Thanks for stopping by — let's build something reliable."


if __name__ == "__main__":
    print(PythonSoftwareEngineer().say_hi())
```

<br>

## 🛠️ Tech Arsenal

<div align="center">

<img src="https://skillicons.dev/icons?i=python,fastapi,mysql,redis,aws,docker,nginx,githubactions,git,github,linux,postman,grafana&theme=dark" />

</div>

<table>
<tr><td><b>Languages & Core</b></td><td>

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/-SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![OOP](https://img.shields.io/badge/-OOP-333333?style=flat-square)
![REST APIs](https://img.shields.io/badge/-REST_API_Design-333333?style=flat-square)

</td></tr>
<tr><td><b>Frameworks</b></td><td>

![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-D71F00?style=flat-square)
![Celery](https://img.shields.io/badge/-Celery-37814A?style=flat-square&logo=celery)
![LangChain](https://img.shields.io/badge/-LangChain-1C3C3C?style=flat-square)

</td></tr>
<tr><td><b>Databases</b></td><td>

![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/-Redis-DC382D?style=flat-square&logo=redis)
![pgvector](https://img.shields.io/badge/-pgvector-336791?style=flat-square&logo=postgresql)

</td></tr>
<tr><td><b>Cloud & DevOps</b></td><td>

![AWS EC2](https://img.shields.io/badge/-EC2-232F3E?style=flat-square&logo=amazon-aws)
![AWS RDS](https://img.shields.io/badge/-RDS-232F3E?style=flat-square&logo=amazon-aws)
![AWS S3](https://img.shields.io/badge/-S3-232F3E?style=flat-square&logo=amazon-aws)
![AWS SQS](https://img.shields.io/badge/-SQS-232F3E?style=flat-square&logo=amazon-aws)
![CloudWatch](https://img.shields.io/badge/-CloudWatch-232F3E?style=flat-square&logo=amazon-aws)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker)
![Nginx](https://img.shields.io/badge/-Nginx-009639?style=flat-square&logo=nginx)
![Gunicorn](https://img.shields.io/badge/-Gunicorn/Uvicorn-499848?style=flat-square&logo=gunicorn)

</td></tr>
<tr><td><b>Testing & CI/CD</b></td><td>

![Pytest](https://img.shields.io/badge/-Pytest-0A9EDC?style=flat-square&logo=pytest)
![GitHub Actions](https://img.shields.io/badge/-GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Locust](https://img.shields.io/badge/-Locust_(Load_Testing)-000000?style=flat-square)

</td></tr>
<tr><td><b>Tools</b></td><td>

![Git](https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git)
![Postman](https://img.shields.io/badge/-Postman-FF6C37?style=flat-square&logo=postman)
![Linux](https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Grafana](https://img.shields.io/badge/-Grafana-F46800?style=flat-square&logo=grafana)

</td></tr>
</table>

<br>

## 🚀 Featured Projects — with system design

<details>
<summary><b>🏗️ Multi-Tenant SaaS API Platform</b> <sub>· Jan 2024 – Apr 2024</sub></summary>
<br>

`Python` `FastAPI` `MySQL` `Redis` `Docker` `Nginx` `AWS (EC2, RDS)` `GitHub Actions`

A backend platform serving isolated tenant workloads through a shared API layer — tenant resolution, connection pooling, and caching handled centrally.

```mermaid
flowchart LR
    Client([Client Apps]) --> Nginx[Nginx Reverse Proxy]
    Nginx --> API[FastAPI App Servers]
    API --> Resolver{Tenant Resolver}
    Resolver --> Cache[(Redis Cache)]
    Resolver --> DB[(MySQL — per-tenant schema)]
    API -.CI/CD.-> GHA[GitHub Actions]
    GHA -.deploy.-> EC2[AWS EC2]
    DB --- RDS[AWS RDS]
```

**Engineering focus:** request-scoped tenant isolation, cache-aside pattern with Redis, zero-downtime deploys via GitHub Actions → EC2.

</details>

<details>
<summary><b>🧠 AI-Powered Enterprise Knowledge Assistant (RAG)</b> <sub>· May 2024 – Aug 2024</sub></summary>
<br>

`Python` `FastAPI` `LangChain` `pgvector` `MySQL` `AWS EC2` `Docker`

A retrieval-augmented assistant that answers questions grounded in internal company documents.

```mermaid
flowchart LR
    Docs[(Internal Docs)] --> Chunk[Chunk + Embed]
    Chunk --> VectorDB[(pgvector)]
    User([User Query]) --> API[FastAPI Endpoint]
    API --> Retrieve[LangChain Retriever]
    Retrieve --> VectorDB
    Retrieve --> LLM[LLM Completion]
    LLM --> API
    API --> User
    MySQL[(MySQL — chat history)] --- API
```

**Engineering focus:** chunking strategy for retrieval quality, vector similarity search at scale, responses traceable back to source documents.

</details>

<details>
<summary><b>📈 AIOps Log Anomaly Detection & Alerting System</b> <sub>· Sep 2024 – Dec 2024</sub></summary>
<br>

`Python` `Celery` `Redis` `MySQL` `Docker` `Grafana` `AWS CloudWatch`

A background pipeline that ingests application logs, flags statistical anomalies, and pushes alerts before they become incidents.

```mermaid
flowchart LR
    Logs[Log Sources] --> Collector[Log Collector]
    Collector --> Queue[(Redis Queue)]
    Queue --> Workers[Celery Workers]
    Workers --> Detect{Anomaly Detection}
    Detect -->|normal| Store[(MySQL)]
    Detect -->|anomaly| Alert[Alert Dispatcher]
    Alert --> CloudWatch[AWS CloudWatch]
    Store --> Dash[Grafana Dashboards]
```

**Engineering focus:** async task orchestration with Celery, alert-fatigue reduction via thresholding, real-time observability in Grafana.

</details>

<br>

## 🎓 Education

```
MCA — Maharaja Agrasen Himalayan Garhwal University  (2021–2023)  |  GPA 8.0/10
BCA — Maharaja Agrasen Himalayan Garhwal University  (2019–2021)  |  GPA 7.55/10
```

<br>

## 📊 GitHub & LeetCode

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=Sunilsoftwarengineer&show_icons=true&theme=synthwave&hide_border=true&count_private=true" />
<img height="165" src="https://leetcard.jacoblin.cool/Sunilsoftwarengineer?theme=dark&font=Fira%20Code&ext=heatmap" />

<img src="https://github-readme-activity-graph.vercel.app/graph?username=Sunilsoftwarengineer&theme=react-dark&hide_border=true" width="100%"/>

<img src="https://github-profile-trophy.vercel.app/?username=Sunilsoftwarengineer&theme=dracula&no-frame=true&row=1&column=6&margin-w=8" width="100%"/>

</div>

<br>

## 📈 Currently Exploring

```
Focus for 2026
├── 🤖 LLM-powered backends with LangChain
├── 🔎 Vector search at scale (pgvector)
├── ⚙️  Performance & load testing with Locust
└── ☁️  Deeper AWS infra: EC2, SQS, CloudWatch
```

<br>

<div align="center">

<img src="https://komarev.com/ghpvc/?username=Sunilsoftwarengineer&style=flat-square&color=00ff9c" alt="Profile views"/>

</div>
