from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
import os

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:5000",  # Development frontend
    "http://localhost:3000",  # Alternative development port
]

# Add production frontend URL if available
if os.getenv("FRONTEND_URL"):
    origins.append(os.getenv("FRONTEND_URL"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tool model
class ToolBase(BaseModel):
    name: str
    description: str
    category: str
    website: Optional[str] = None
    rating: Optional[float] = 0.0
    features: Optional[List[str]] = []

class Tool(ToolBase):
    id: int

# Tools database with reorganized categories
tools_db = [
    # Website Builders (Visual Development)
    {
        "id": 1,
        "name": "Wix",
        "description": "Complete website builder with drag-and-drop interface, hosting, and business solutions.",
        "category": "Website Builder",
        "website": "https://wix.com",
        "rating": 4.5,
        "features": ["Templates", "Blog", "E-commerce", "Custom Domain", "SEO Tools"]
    },
    {
        "id": 2,
        "name": "Webflow",
        "description": "Professional-grade website builder with advanced design capabilities and CMS.",
        "category": "Website Builder",
        "website": "https://webflow.com",
        "rating": 4.7,
        "features": ["CMS", "E-commerce", "Advanced Animations", "Custom Code", "Hosting"]
    },
    {
        "id": 3,
        "name": "Carrd",
        "description": "Simple one-page website builder, perfect for personal sites and landing pages.",
        "category": "Website Builder",
        "website": "https://carrd.co",
        "rating": 4.5,
        "features": ["Single Page Sites", "Forms", "Custom Domain", "Mobile Responsive"]
    },
    {
        "id": 4,
        "name": "Framer",
        "description": "Design-focused website builder with powerful animation capabilities.",
        "category": "Website Builder",
        "website": "https://framer.com",
        "rating": 4.6,
        "features": ["Animations", "Components", "Responsive Design", "Prototyping"]
    },
    {
        "id": 5,
        "name": "Strikingly",
        "description": "Mobile-optimized website builder for creating responsive single-page websites.",
        "category": "Website Builder",
        "website": "https://strikingly.com",
        "rating": 4.3,
        "features": ["Mobile First", "E-commerce", "Blog", "Simple Editor"]
    },

    # App Builders
    {
        "id": 6,
        "name": "Bubble",
        "description": "Powerful no-code platform for building web applications and marketplaces.",
        "category": "App Builder",
        "website": "https://bubble.io",
        "rating": 4.7,
        "features": ["Database", "API Connections", "User Authentication", "Payment Processing"]
    },
    {
        "id": 7,
        "name": "Adalo",
        "description": "Mobile app builder with native app capabilities and marketplace components.",
        "category": "App Builder",
        "website": "https://adalo.com",
        "rating": 4.3,
        "features": ["Native Apps", "Custom Components", "Database", "API Integration"]
    },
    {
        "id": 8,
        "name": "Glide",
        "description": "Turn spreadsheets into beautiful, easy-to-use mobile and web apps.",
        "category": "App Builder",
        "website": "https://glideapps.com",
        "rating": 4.4,
        "features": ["Spreadsheet Based", "Templates", "Quick Setup", "Progressive Web Apps"]
    },
    {
        "id": 9,
        "name": "Softr",
        "description": "Build web apps from Airtable data with ready-to-use building blocks.",
        "category": "App Builder",
        "website": "https://softr.io",
        "rating": 4.4,
        "features": ["Airtable Integration", "User Portal", "Membership Sites", "White Label"]
    },
    {
        "id": 10,
        "name": "Appsheet",
        "description": "Google's no-code platform for building mobile and web apps from spreadsheets.",
        "category": "App Builder",
        "website": "https://appsheet.com",
        "rating": 4.4,
        "features": ["Google Integration", "Offline Support", "Mobile Apps", "Automation"]
    },

    # E-commerce Platforms
    {
        "id": 11,
        "name": "Shopify",
        "description": "Complete e-commerce platform for online stores and retail point-of-sale systems.",
        "category": "E-commerce",
        "website": "https://shopify.com",
        "rating": 4.8,
        "features": ["Online Store", "POS", "Marketing Tools", "Inventory Management"]
    },
    {
        "id": 12,
        "name": "Gumroad",
        "description": "Simple platform for creators to sell digital products and subscriptions.",
        "category": "E-commerce",
        "website": "https://gumroad.com",
        "rating": 4.6,
        "features": ["Digital Products", "Subscriptions", "Landing Pages", "Email Marketing"]
    },

    # Automation & Integration
    {
        "id": 13,
        "name": "Zapier",
        "description": "Connect apps and automate workflows with easy-to-use integrations.",
        "category": "Automation",
        "website": "https://zapier.com",
        "rating": 4.8,
        "features": ["App Integration", "Workflow Automation", "Task Scheduling", "Filters"]
    },
    {
        "id": 14,
        "name": "Make (Integromat)",
        "description": "Visual automation platform with advanced features and detailed control.",
        "category": "Automation",
        "website": "https://make.com",
        "rating": 4.7,
        "features": ["Visual Workflows", "Real-time Execution", "Error Handling", "Complex Scenarios"]
    },
    {
        "id": 15,
        "name": "Pabbly",
        "description": "Business automation platform focusing on subscription billing and email marketing.",
        "category": "Automation",
        "website": "https://pabbly.com",
        "rating": 4.3,
        "features": ["Subscription Management", "Email Marketing", "Form Builder", "Workflow Automation"]
    },

    # Content & Design
    {
        "id": 16,
        "name": "Canva",
        "description": "Design platform for creating graphics, presentations, and marketing materials.",
        "category": "Design",
        "website": "https://canva.com",
        "rating": 4.8,
        "features": ["Templates", "Brand Kit", "Collaboration", "Content Planner"]
    },
    {
        "id": 17,
        "name": "Mailchimp",
        "description": "Marketing platform specializing in email campaigns and automation.",
        "category": "Marketing",
        "website": "https://mailchimp.com",
        "rating": 4.5,
        "features": ["Email Marketing", "Landing Pages", "Automation", "CRM"]
    },

    # AI Tools
    {
        "id": 18,
        "name": "Writesonic",
        "description": "AI writing tool for creating marketing copy and content.",
        "category": "AI Tools",
        "website": "https://writesonic.com",
        "rating": 4.5,
        "features": ["Content Generation", "Copy Writing", "Blog Posts", "Product Descriptions"]
    },
    {
        "id": 19,
        "name": "Jasper",
        "description": "Advanced AI writing assistant for various content types.",
        "category": "AI Tools",
        "website": "https://jasper.ai",
        "rating": 4.7,
        "features": ["Long-form Content", "Social Media", "Marketing Copy", "SEO Writing"]
    },

    # Productivity & Collaboration
    {
        "id": 20,
        "name": "Notion",
        "description": "All-in-one workspace for notes, documents, and team collaboration.",
        "category": "Productivity",
        "website": "https://notion.so",
        "rating": 4.9,
        "features": ["Notes", "Databases", "Wiki", "Project Management"]
    },
    {
        "id": 21,
        "name": "Airtable",
        "description": "Flexible platform combining spreadsheet and database capabilities.",
        "category": "Productivity",
        "website": "https://airtable.com",
        "rating": 4.6,
        "features": ["Database", "Collaboration", "Automations", "API"]
    },

    # Business Tools
    {
        "id": 22,
        "name": "Retool",
        "description": "Platform for building internal tools and business applications.",
        "category": "Business Tools",
        "website": "https://retool.com",
        "rating": 4.7,
        "features": ["Custom Dashboards", "Database Integration", "API Connection", "Workflow Automation"]
    },
    {
        "id": 23,
        "name": "Memberstack",
        "description": "Add membership and authentication features to any website.",
        "category": "Business Tools",
        "website": "https://memberstack.com",
        "rating": 4.5,
        "features": ["User Authentication", "Payments", "Member Management", "API Access"]
    },

    # Forms & Surveys
    {
        "id": 24,
        "name": "Typeform",
        "description": "Create engaging forms, surveys, and quizzes with conversational approach.",
        "category": "Forms",
        "website": "https://typeform.com",
        "rating": 4.6,
        "features": ["Conversational Forms", "Logic Jumps", "Analytics", "API Integration"]
    },
    {
        "id": 25,
        "name": "Tally",
        "description": "Simple and powerful form builder for all purposes.",
        "category": "Forms",
        "website": "https://tally.so",
        "rating": 4.7,
        "features": ["Easy Forms", "Conditional Logic", "File Upload", "Payments"]
    },

    # Specialized Tools
    {
        "id": 26,
        "name": "Voiceflow",
        "description": "Platform for designing voice apps and chatbot conversations.",
        "category": "Specialized Tools",
        "website": "https://voiceflow.com",
        "rating": 4.5,
        "features": ["Voice Apps", "Chatbots", "Conversation Design", "Integration"]
    },
    {
        "id": 27,
        "name": "Xano",
        "description": "Backend development platform for creating scalable APIs.",
        "category": "Specialized Tools",
        "website": "https://xano.com",
        "rating": 4.6,
        "features": ["API Builder", "Database", "Authentication", "Serverless"]
    },
    {
        "id": 28,
        "name": "Stripe",
        "description": "Payment processing platform with extensive integration options.",
        "category": "Specialized Tools",
        "website": "https://stripe.com",
        "rating": 4.9,
        "features": ["Payments", "Subscriptions", "Invoicing", "Fraud Prevention"]
    },
    {
        "id": 29,
        "name": "Bravo",
        "description": "Platform for building and scaling online marketplaces.",
        "category": "Specialized Tools",
        "website": "https://bravostudio.app",
        "rating": 4.4,
        "features": ["Marketplace Builder", "Mobile Apps", "Admin Dashboard", "Payment Processing"]
    },
    {
        "id": 30,
        "name": "Landbot",
        "description": "Platform for creating conversational chatbots.",
        "category": "Specialized Tools",
        "website": "https://landbot.io",
        "rating": 4.5,
        "features": ["Chatbot Builder", "WhatsApp Integration", "Lead Generation", "API Integration"]
    }
]

@app.get("/")
def read_root():
    return {"message": "Welcome to No-Code Tools API"}

@app.get("/api/tools", response_model=List[Tool])
def get_tools():
    return tools_db

@app.post("/api/tools", response_model=Tool)
def create_tool(tool: ToolBase):
    tool_id = len(tools_db) + 1
    new_tool = {**tool.dict(), "id": tool_id}
    tools_db.append(new_tool)
    return new_tool

@app.get("/api/tools/{tool_id}", response_model=Tool)
def get_tool(tool_id: int):
    for tool in tools_db:
        if tool["id"] == tool_id:
            return tool
    raise HTTPException(status_code=404, detail="Tool not found")

@app.get("/api/tools/category/{category}", response_model=List[Tool])
def get_tools_by_category(category: str):
    return [tool for tool in tools_db if tool["category"].lower() == category.lower()]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
