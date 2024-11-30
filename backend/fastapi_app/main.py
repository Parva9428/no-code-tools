from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Pydantic models
class ToolBase(BaseModel):
    name: str
    description: str
    category: str
    website: Optional[str] = None
    rating: Optional[float] = 0.0

class Tool(ToolBase):
    id: int

# Temporary in-memory storage
tools_db = [
    {
        "id": 1,
        "name": "Bubble",
        "description": "Visual programming tool for creating web applications without code. Build any web app and host it with Bubble.",
        "category": "Web Development",
        "website": "https://bubble.io",
        "rating": 4.5
    },
    {
        "id": 2,
        "name": "Webflow",
        "description": "Design, build, and launch responsive websites visually. Create professional websites without coding.",
        "category": "Web Design",
        "website": "https://webflow.com",
        "rating": 4.7
    },
    {
        "id": 3,
        "name": "Airtable",
        "description": "Part spreadsheet, part database, and entirely flexible. Build collaborative apps with Airtable.",
        "category": "Database",
        "website": "https://airtable.com",
        "rating": 4.6
    },
    {
        "id": 4,
        "name": "Zapier",
        "description": "Connect your apps and automate workflows. Move info between your web apps automatically.",
        "category": "Automation",
        "website": "https://zapier.com",
        "rating": 4.8
    },
    {
        "id": 5,
        "name": "Notion",
        "description": "All-in-one workspace for notes, docs, wikis, and project management. Customize it exactly how you need it.",
        "category": "Productivity",
        "website": "https://notion.so",
        "rating": 4.9
    },
    {
        "id": 6,
        "name": "Figma",
        "description": "Collaborative interface design tool that lets you create, prototype, and design systems together.",
        "category": "Design",
        "website": "https://figma.com",
        "rating": 4.9
    },
    {
        "id": 7,
        "name": "Make (Integromat)",
        "description": "Visual platform for designing, building, and automating anything from simple tasks to complex workflows.",
        "category": "Automation",
        "website": "https://make.com",
        "rating": 4.7
    },
    {
        "id": 8,
        "name": "Retool",
        "description": "Build internal tools, admin panels, and dashboards with a drag-and-drop interface.",
        "category": "Internal Tools",
        "website": "https://retool.com",
        "rating": 4.6
    },
    {
        "id": 9,
        "name": "Glide",
        "description": "Create mobile apps from Google Sheets without coding. Perfect for simple business apps.",
        "category": "Mobile Development",
        "website": "https://glideapps.com",
        "rating": 4.5
    },
    {
        "id": 10,
        "name": "Softr",
        "description": "Build web apps from Airtable databases. Create client portals, internal tools, and member directories.",
        "category": "Web Development",
        "website": "https://softr.io",
        "rating": 4.4
    },
    {
        "id": 11,
        "name": "Carrd",
        "description": "Simple, free, fully responsive one-page sites for pretty much anything.",
        "category": "Web Design",
        "website": "https://carrd.co",
        "rating": 4.8
    },
    {
        "id": 12,
        "name": "Memberstack",
        "description": "Add membership and gated content functionality to any website without coding.",
        "category": "Authentication",
        "website": "https://memberstack.com",
        "rating": 4.5
    },
    {
        "id": 13,
        "name": "Typeform",
        "description": "Create beautiful, conversational forms and surveys with advanced logic and integrations.",
        "category": "Forms",
        "website": "https://typeform.com",
        "rating": 4.7
    },
    {
        "id": 14,
        "name": "Mailchimp",
        "description": "All-in-one marketing platform for email campaigns, landing pages, and automation.",
        "category": "Marketing",
        "website": "https://mailchimp.com",
        "rating": 4.6
    },
    {
        "id": 15,
        "name": "Shopify",
        "description": "Complete e-commerce platform to start, grow, and manage a business with no coding required.",
        "category": "E-commerce",
        "website": "https://shopify.com",
        "rating": 4.8
    }
]
tool_id_counter = 16

@app.get("/")
async def read_root():
    return {"message": "Welcome to No-Code Tools Directory API"}

@app.get("/api/tools", response_model=List[Tool])
async def get_tools():
    return tools_db

@app.post("/api/tools", response_model=Tool)
async def create_tool(tool: ToolBase):
    global tool_id_counter
    new_tool = Tool(
        id=tool_id_counter,
        **tool.dict()
    )
    tools_db.append(new_tool.dict())
    tool_id_counter += 1
    return new_tool

@app.get("/api/tools/{tool_id}", response_model=Tool)
async def get_tool(tool_id: int):
    tool = next((tool for tool in tools_db if tool["id"] == tool_id), None)
    if tool is None:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool

@app.get("/api/tools/category/{category}", response_model=List[Tool])
async def get_tools_by_category(category: str):
    return [tool for tool in tools_db if tool["category"].lower() == category.lower()]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
