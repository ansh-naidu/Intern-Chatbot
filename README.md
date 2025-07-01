# 🚀 Intern-Chatbot  
A smart chatbot system to assist interns with training resources, progress tracking, and engagement through gamification and recommendations.

---

## 📌 Step-by-Step Implementation Plan

---

### 🗂️ Phase 1: Resource Upload & Data Structuring
-  **1.1** Gather and categorize all intern training resources (PDFs, Docs, Video links)  
-  **1.2** Store metadata in a database:  
  `Module Name`, `Description`, `Resource Links`  
-  **1.3** Build API Endpoints:  
  - `GET /get_modules`  
  - `GET /get_module_details/{id}`  

---

### 💬 Phase 2: Chatbot Development (Knowledge-based + FAQ)
- 🔧 **2.1** Set up FastAPI backend with chat endpoint: `POST /ask`  
- 🧠 **2.2** Integrate OpenAI GPT API or Azure OpenAI  
- 📚 **2.3** Inject knowledge from:  
  - Intern FAQs  
  - Resource Map  
- 💻 **2.4** *(Optional)* Build Slack or Teams bot for interaction  

---

### 📈 Phase 3: Intern Progress Tracker
- 📊 **3.1** Create DB tables: `Interns`, `Progress_Tracking`, `Completed_Modules`  
- 🛠️ **3.2** Develop APIs:  
  - `POST /update_progress`  
  - `GET /get_progress/{intern_id}`  
- 🖥️ **3.3** Display intern progress on frontend dashboard  

---

### 📝 Phase 4: Automated Feedback / Questionnaire System
- 🔁 **4.1** Auto-trigger feedback forms post-module completion  
- 📋 **4.2** Design quizzes using **Google Forms** or **Typeform**  
- 💾 **4.3** Store responses in the database  
- 🧪 **4.4** Run **sentiment analysis** on text responses  

---

### 🎯 Phase 5: AI-Based Learning Recommendation Engine
- 🧩 **5.1** Define rule-based logic for recommendations  
- 🌐 **5.2** API Endpoint: `GET /recommendation/{intern_id}`  
- 📱 **5.3** Show personalized recommendations on dashboard or chatbot  

---

### 🏆 Phase 6: Gamification Layer
- 🪙 **6.1** Add `points` column to `Progress_Tracking`  
- ➕ **6.2** Increment points on module completion  
- 🧿 **6.3** Display badges/points on the UI  
- 🧮 **6.4** *(Optional)* Leaderboard API: `GET /leaderboard`  

---

### 🧠 Phase 7: Chatbot Context Memory
- 🗂️ **7.1** Store last user query + bot response in DB  
- 🧠 **7.2** Enhance chatbot to be context-aware  
- 🔁 **7.3** Enable flow like: `"What's my next task?"`  

---

### 📊 Phase 8: Manager Dashboard (Monitoring & Analytics)
- 🧑‍💼 **8.1** Dashboard: intern list, % progress, feedback sentiment  
- 🛠️ **8.2** Backend API: `GET /manager_dashboard/{manager_id}`  
- 📈 **8.3** Add visual charts using **Plotly** / **Streamlit**  

---

### 📬 Phase 9: Auto-Generated Weekly Reporting
- 🐍 **9.1** Python script to query progress + feedback data  
- 🧾 **9.2** Format into HTML reports using **Jinja2**  
- ✉️ **9.3** Send via **SMTP Email** or **Slack Webhook**  
- ⏱️ **9.4** Schedule with **Cron** or **APScheduler**  

---

### 📦 Phase 10: Dockerize & Deploy (Demo Ready)
- 🐳 **10.1** Create Dockerfile for FastAPI backend  
- 🧪 **10.2** Run locally or deploy on **AWS EC2 (Free Tier)**  
- ✅ **10.3** Perform QA and prepare demo walkthrough  

---

## 🔧 Tech Stack
- **Backend:** FastAPI, SQLite/PostgreSQL  
- **Frontend:** Streamlit / React (Optional)  
- **AI/LLM:** OpenAI GPT / Azure OpenAI  
- **DevOps:** Docker, AWS EC2  
- **Monitoring:** Plotly, Cron, APScheduler  
- **Forms & Feedback:** Google Forms, Typeform  
- **Misc:** Jinja2, Slack API

---

