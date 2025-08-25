# 🧬 Gene Predictor 🧬

A full-stack web application that predicts the potential genetic traits of an offspring based on the phenotypes of two parents. This project is fully containerized with Docker and ready for deployment on Kubernetes.

![Gene Predictor Screenshot](./path-to-your-screenshot.png)
*(Replace the path above with a real screenshot of your app!)*

---

## ✨ Features

*   **Interactive Trait Selection:** Select phenotypes for 20 different genetic traits for both parents.
*   **Simple, Intuitive UI:** A clean and modern user interface built with React.
*   **Progress Tracking:** A visual progress bar shows how many traits you have completed.
*   **Instant Predictions:** (Describe what happens at the end - e.g., "View a summary of potential offspring phenotypes.")

---

## 🛠️ Tech Stack

This project is built with a modern, container-based architecture.

*   **Frontend:**
    *   [React](https://reactjs.org/) (with Vite) - A JavaScript library for building user interfaces.
*   **Backend:**
    *   [Django](https://www.djangoproject.com/) - A high-level Python web framework.
*   **Infrastructure & DevOps:**
    *   [Docker](https://www.docker.com/) - For containerizing the frontend and backend services.
    *   [Docker Compose](https://docs.docker.com/compose/) - For easy local development orchestration.
    *   [Kubernetes](https://kubernetes.io/) - For container orchestration in a cluster environment.
    *   [Jenkins](https://www.jenkins.io/) - The CI/CD pipeline is defined in the `Jenkinsfile` for automated builds and deployments.

---

## 🚀 Getting Started (Local Development)

Follow these instructions to get the project running on your local machine for development and testing purposes.

### Prerequisites

*   [Git](https://git-scm.com/)
*   [Docker](https://www.docker.com/products/docker-desktop)
*   [Docker Compose](https://docs.docker.com/compose/install/) (Included with Docker Desktop)

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd gene-predictor-app
    ```

2.  **Create environment files:**
    You need to create `.env` files for both the frontend and backend services. Example files are provided.

    *   **For the backend:**
        ```bash
        cp backend/.env.example backend/.env
        ```
        *(Note: You may need to create the `.env.example` file first with `SECRET_KEY=...` and `DEBUG=...`)*

    *   **For the frontend:**
        ```bash
        cp frontend/.env.example frontend/.env
        ```
        *(Note: You may need to create the `.env.example` file first with `VITE_API_URL=http://localhost:8000`)*

3.  **Build and run the containers using Docker Compose:**
    ```bash
    docker-compose up -d --build
    ```

4.  **Access the application:**
    *   Frontend UI: [**http://localhost:5173**](http://localhost:5173)
    *   Backend API: [**http://localhost:8000**](http://localhost:8000)

---

## ☸️ Kubernetes Deployment

These instructions explain how to deploy the application to a Kubernetes cluster.

### Prerequisites

*   A running Kubernetes cluster (e.g., the one enabled in Docker Desktop).
*   `kubectl` command-line tool configured to talk to your cluster.
*   A Docker Hub account and the Docker CLI.

### Deployment Steps

1.  **Log in to Docker Hub:**
    ```bash
    docker login
    ```

2.  **Build and push the Docker images:**
    Replace `joyobichie` with your Docker Hub username.
    ```bash
    # Build and push the backend image
    docker build -t joyobichie/gene-predictor-app-backend:latest ./backend
    docker push joyobichie/gene-predictor-app-backend:latest

    # Build and push the frontend image
    docker build -t joyobichie/gene-predictor-app-frontend:latest ./frontend
    docker push joyobichie/gene-predictor-app-frontend:latest
    ```

3.  **Apply the Kubernetes manifests:**
    The manifest files in the `deployment/` directory define all the necessary Kubernetes resources.
    ```bash
    kubectl apply -f deployment/
    ```

4.  **Check the status and access the application:**
    *   Wait for the pods to be in the `Running` state:
        ```bash
        kubectl get pods -w
        ```
    *   Get the service URL:
        ```bash
        kubectl get service frontend-service
        ```
    *   Access the app in your browser at the `EXTERNAL-IP` and `PORT` listed (e.g., [**http://localhost:5173**](http://localhost:5173)).





---

## 📂 Project Structure
