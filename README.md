```
backend/
├── app/
│   ├── api/              # 路由层
│   │   ├── deps.py
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── blog.py
│   │       └── admin.py
│   │
│   ├── core/             # 核心组件
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── logging.py
│   │   └── metrics.py
│   │
│   ├── models/           # SQLModel
│   │   ├── user.py
│   │   ├── blog.py
│   │   └── tag.py
│   │
│   ├── schemas/          # Pydantic DTO
│   │   ├── user.py
│   │   ├── blog.py
│   │   └── tag.py
│   │
│   ├── repository/       # 数据访问层
│   │   ├── user_repo.py
│   │   ├── blog_repo.py
│   │   └── tag_repo.py
│   │
│   ├── services/         # 业务层
│   │   ├── auth_service.py
│   │   ├── blog_service.py
│   │   └── tag_service.py
│   │
│   ├── db.py
│   └── main.py
│
├── alembic/
├── tests/
├── Dockerfile
├── pyproject.toml
└── Makefile
```

# 总体路线

| 阶段      | 目标                    | 产物     |
| ------- | --------------------- | ------ |
| Phase 0 | 项目骨架 & 工程规范           | 可运行空服务 |
| Phase 1 | 配置 / 日志 / DB / 基础设施   | 工程内核完成 |
| Phase 2 | User + Auth           | JWT 登录 |
| Phase 3 | Blog 模块               | CRUD   |
| Phase 4 | 测试体系                  | pytest |
| Phase 5 | Docker / Makefile     | 本地工程化  |
| Phase 6 | Nginx / K8s / Metrics | 运维级    |

## Phase 0 
目标：
先跑起来一个“干净、规范、可扩展”的 FastAPI 工程骨架

1. 初始化项目目录结构
   ```sh
   mkdir aetherdock-backend
   cd aetherdock-backend
   uv init
   ```
2. 安装 FastAPI 及其依赖
   ```sh
   uv add fastapi uvicorn sqlmodel pydantic-settings structlog python-jose passlib[bcrypt]
   uv add pytest httpx --dev
   ```
3. 创建标准目录
    ```sh
    mkdir -p app/api/v1
    mkdir -p app/core
    mkdir -p app/models
    mkdir -p app/schemas
    mkdir -p app/repository
    mkdir -p app/services
    touch app/main.py
    ```
4. 写第一个工程级 `main.py` 并运行
5. 运行项目，确保能访问 `/docs` 查看 Swagger UI