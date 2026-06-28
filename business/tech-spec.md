```markdown
# Tech Spec: project-boundary

## Stack
- **Language**: TypeScript (Node.js 18+)
- **Framework**: Express.js (REST API) + Next.js (admin dashboard)
- **Runtime**: Node.js 18 LTS
- **Database**: PostgreSQL 15 (with JSONB support)
- **ORM**: Prisma ORM
- **Frontend**: React 18 + Tailwind CSS
- **Authentication**: Auth.js (NextAuth.js)
- **Deployment**: Docker + Kubernetes (k3s for dev)

## Hosting
- **Free Tier First**: GitHub Pages + Vercel for frontend, Railway for backend
- **Production Platforms**: 
  - Primary: AWS (EC2 + RDS + S3)
  - Backup: GCP (Compute Engine + Cloud SQL)
- **CI/CD**: GitHub Actions + ArgoCD for deployment orchestration
- **Monitoring**: Prometheus + Grafana (self-hosted)

## Data Model
### Tables/Collections
1. **projects**
   - id (UUID, PK)
   - name (string)
   - description (text)
   - owner_id (UUID, FK to users)
   - created_at (timestamp)
   - updated_at (timestamp)
   - status (enum: active, archived)

2. **boundaries**
   - id (UUID, PK)
   - project_id (UUID, FK to projects)
   - title (string)
   - description (text)
   - type (enum: feature, bug, enhancement)
   - status (enum: proposed, approved, rejected, implemented)
   - created_at (timestamp)
   - updated_at (timestamp)

3. **users**
   - id (UUID, PK)
   - email (string, unique)
   - name (string)
   - avatar_url (string)
   - created_at (timestamp)
   - updated_at (timestamp)

4. **project_members**
   - project_id (UUID, FK to projects)
   - user_id (UUID, FK to users)
   - role (enum: admin, maintainer, contributor)
   - joined_at (timestamp)

5. **boundary_changes**
   - id (UUID, PK)
   - boundary_id (UUID, FK to boundaries)
   - changed_by (UUID, FK to users)
   - change_type (enum: status_change, description_update)
   - old_value (JSONB)
   - new_value (JSONB)
   - created_at (timestamp)

## API Surface
1. **GET /api/projects** - List all projects for authenticated user
2. **POST /api/projects** - Create new project
3. **GET /api/projects/{id}** - Get project details
4. **PUT /api/projects/{id}** - Update project metadata
5. **DELETE /api/projects/{id}** - Archive project
6. **GET /api/projects/{id}/boundaries** - List project boundaries
7. **POST /api/projects/{id}/boundaries** - Create new boundary
8. **GET /api/boundaries/{id}** - Get boundary details
9. **PUT /api/boundaries/{id}** - Update boundary status/description
10. **DELETE /api/boundaries/{id}** - Delete boundary

## Security Model
- **Authentication**: JWT tokens via Auth.js (OAuth2 providers: GitHub, GitLab)
- **Authorization**: Role-based access control (RBAC) with project-level permissions
- **Secrets Management**: Vault (HashiCorp) for sensitive data
- **IAM**: GitHub OAuth for identity provider, with custom roles for project members
- **Data Encryption**: AES-256 encryption at rest for sensitive fields
- **Rate Limiting**: 1000 req/hour per IP, 100 req/min per authenticated user

## Observability
- **Logs**: Winston + ELK stack (Elasticsearch, Logstash, Kibana)
- **Metrics**: Prometheus + Grafana dashboards
- **Traces**: OpenTelemetry + Jaeger
- **Alerting**: Alertmanager + Slack integration
- **Health Checks**: Liveness/readiness probes on all services

## Build/CI
- **Build System**: npm scripts + Webpack
- **Testing**: Jest (unit), Cypress (e2e)
- **Code Quality**: ESLint + Prettier + SonarQube
- **Security Scanning**: Snyk + OWASP ZAP
- **CI Pipeline**: GitHub Actions with stages:
  1. Code linting & formatting
  2. Unit tests (coverage > 80%)
  3. Integration tests
  4. Security scan
  5. Deploy to staging
  6. Manual approval for production deploy
```