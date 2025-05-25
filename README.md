
# Task Tracker Flask Web App

🚀 A full-stack Task Management application powered by Flask, SQLite, Docker, and Azure.


## Demo

Insert gif or link to demo


## ⚙️ Tech Stack

**Backend: Flask:** 
- Handles API requests for task management.
- Provides CRUD operations for tasks (Add, View, Delete, Reset).
- Uses SQLite as a lightweight database.

**Frontend: HTML** 
- UI for viewing all tasks and adding new tasks.
- Allows users to delete all tasks and reset Task IDs.
- Styled for clean and intuitive interactions.

**Database: SQLite**
- Stores Task ID and Task Name.
- Provides a simple yet efficient task management system.

**Containerization: Docker**
- Encapsulates the backend API within a Docker container.
- Ensures portability and easy deployment across environments.

**Cloud Deployment: Azure**
- Hosted on Azure App Service with a container-based deployment.
- Docker images stored in Azure Container Registry (ACR).
- Uses Azure Service Principal for secure authentication.

**CI/CD: GitHub Actions**
- Automates Docker image builds & deployments to Azure.
- Pushes updates seamlessly from GitHub.
## 🔹 Features

- View all tasks from the frontend UI
- Add new tasks through the interface
- Reset Task ID numbering after deletion of all tasks
- Fully responsive UI for intuitive task management


## 🚀 Setup & Deployment

1️⃣ Clone the repository:

```bash
  git clone https://github.com/XPRX77/Personal-Task-Tracker.git
  cd TaskTrackerApp
```
2️⃣ Run the Flask app:

```bash
   python main.py
```
🔹 Docker Setup 

1️⃣ Build the Docker image:
```bash
   docker build -t flask-task-tracker .
```
2️⃣ Run the container:
```bash
   docker run -p 5000:5000 flask-task-tracker
```
3️⃣ Open the Frontend (index.html) in your browser.
```bash
   http://127.0.0.1:5000/
```

🔹 Azure Deployment

1️⃣ Push the Docker image to Azure:
```bash
   docker push <YOUR_ACR_NAME>.azurecr.io/flask-task-tracker:latest
```
2️⃣ GitHub Actions automates deployment to Azure App Service.

## API Reference

#### Get all tasks

```http
  GET http://<YOUR SERVER FQDN>/tasks
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `task` | `Json` | task field |

#### Add tasks

```http
  POST http://<YOUR SERVER FQDN>/add -H "Content-Type: application/json" -d '{"task": "<YOUR TASK VALUE>"}'
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `task`     | `json` | **Required**. Input value for task |

#### Update tasks

```http
  PUT http://<YOUR SERVER FQDN>/update/5 -H "Content-Type: application/json" -d '{"task": "<YOUR TASK VALUE"}'

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `task`       | `json` | **Required**. Input value for task |

#### Delete tasks

```http
  DELETE http://<YOUR SERVER FQDN>/delete/<taskID>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to delete |

## 🚀 Future Enhancements

- Add user authentication for secure access
- Expand task fields beyond Task ID & Task Name
- Deploy frontend separately on Azure Static Web Apps


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

