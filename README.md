# 🚀 CI-CD-Pipeline-Python

A modern approach to automate the development workflow — from writing code to deploying your application in production!

--- 

## 💡 What is CI/CD?

**CI/CD** = **Continuous Integration** + **Continuous Deployment (or Delivery)**

Automates:

- 🧪 Testing  
- 🛠️ Building  
- 🚀 Deploying  

Benefits:
✅ Faster releases  
✅ Code quality  
✅ Bug prevention  

---

## 🔄 CI Pipeline

**CI** runs automatically when you push code.

Steps:
1. Install dependencies
2. Run unit tests (`test_main.py` using `pytest`)

---

## 🚀 CD Pipeline (Optional)

We can extend it to deploy your container using:

- Render
- Heroku
- Railway
- AWS/GCP/Azure

---

## ⚙️ Tools Used

- **GitHub Actions** for CI/CD
- **Docker** for containerization
- **scikit-learn** for the ML pipeline
- **pytest** for testing

---

### 📈 Workflow Diagram

```mermaid
graph TD;
    A[Push Code to GitHub] --> B[Run GitHub Actions];
    B --> C[Run Unit Tests];
    C --> D[Build Docker Image];   
    D --> E[Deploy to Cloud Platform]; 
  
