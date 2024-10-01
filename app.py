from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Project(BaseModel):
    id: int
    name: str
    description: str
    status: bool
    start_date: str # YYYY-MM-DD
    end_date: str # YYYY-MM-DD
    team_members: List[str]


projects = [
    Project(
        id=1,
        name="Inventory Management System",
        description="A system to manage stock levels, orders, and deliveries for a small business.",
        status=True,
        start_date="2023-01-10",
        end_date="2023-03-15",
        team_members=["Alice", "Bob", "Charlie"]
    ),
    Project(
        id=2,
        name="Weather Forecasting App",
        description="A web app that provides real-time weather data using public APIs.",
        status=False,
        start_date="2023-04-01",
        end_date="2023-07-30",
        team_members=["David", "Eve", "Frank"]
    ),
    Project(
        id=3,
        name="E-commerce Website",
        description="An online store for selling electronics, including a payment gateway integration.",
        status=True,
        start_date="2022-11-15",
        end_date="2023-02-28",
        team_members=["Grace", "Heidi", "Ivan"]
    ),
    Project(
        id=4,
        name="Library Management System",
        description="A digital system to keep track of book inventory, borrowing, and returning processes.",
        status=True,
        start_date="2022-09-05",
        end_date="2022-12-20",
        team_members=["Judy", "Kyle", "Liam"]
    ),
    Project(
        id=5,
        name="Social Media Analytics Tool",
        description="A tool to analyze social media trends and sentiments for a brand.",
        status=False,
        start_date="2023-05-10",
        end_date="2023-09-30",
        team_members=["Mike", "Nina", "Oscar"]
    ),
    Project(
        id=6,
        name="Online Learning Platform",
        description="A platform that offers courses with interactive quizzes and progress tracking.",
        status=True,
        start_date="2022-06-01",
        end_date="2022-12-01",
        team_members=["Paul", "Quinn", "Rita"]
    ),
    Project(
        id=7,
        name="Healthcare Appointment System",
        description="An app to schedule and manage patient appointments for a local clinic.",
        status=False,
        start_date="2023-03-10",
        end_date="2023-08-30",
        team_members=["Steve", "Tina", "Uma"]
    ),
    Project(
        id=8,
        name="IoT Smart Home System",
        description="A smart home system to control lights, thermostats, and security cameras via a mobile app.",
        status=True,
        start_date="2022-07-20",
        end_date="2022-10-25",
        team_members=["Victor", "Wendy", "Xander"]
    ),
    Project(
        id=9,
        name="Fitness Tracker App",
        description="A mobile app to track exercise routines, monitor health stats, and offer workout suggestions.",
        status=False,
        start_date="2023-01-15",
        end_date="2023-05-20",
        team_members=["Yvonne", "Zane", "Aaron"]
    ),
    Project(
        id=10,
        name="Personal Finance Tracker",
        description="A tool for users to manage their budget, track expenses, and set financial goals.",
        status=True,
        start_date="2022-03-01",
        end_date="2022-06-30",
        team_members=["Bianca", "Carl", "Donna"]
    )
]


@app.get("/projects", response_model=List[Project])
def get_projects():
    return projects

@app.post("/projects", response_model=Project)
def create_project(project: Project):
    projects.append(project)
    return project
