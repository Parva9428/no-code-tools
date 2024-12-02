export interface Tool {
  name: string;
  url: string;
  description: string;
  category: string;
}

export const tools: Tool[] = [
  // Website and App Builders
  {
    name: "Webflow",
    url: "https://webflow.com",
    description: "Build responsive websites visually with custom animations",
    category: "Website and App Builders"
  },
  {
    name: "Bubble",
    url: "https://bubble.io",
    description: "Create web apps with complex logic and database integrations",
    category: "Website and App Builders"
  },
  {
    name: "Glide",
    url: "https://www.glideapps.com",
    description: "Build mobile apps using Google Sheets as a backend",
    category: "Website and App Builders"
  },

  // Automation
  {
    name: "Zapier",
    url: "https://zapier.com",
    description: "Automate workflows between thousands of apps",
    category: "Automation"
  },
  {
    name: "Make (Integromat)",
    url: "https://www.make.com",
    description: "Visual platform for connecting apps and automating workflows",
    category: "Automation"
  },

  // AI and Machine Learning
  {
    name: "Runway",
    url: "https://runwayml.com",
    description: "Simplify creative AI workflows, including image and video generation",
    category: "AI and Machine Learning"
  },
  {
    name: "Levity",
    url: "https://www.levity.ai",
    description: "Automate tasks using AI-driven document, text, and image classification",
    category: "AI and Machine Learning"
  },

  // Database and Backend
  {
    name: "Airtable",
    url: "https://www.airtable.com",
    description: "Spreadsheet-database hybrid for organizing and managing data",
    category: "Database and Backend"
  },
  {
    name: "Xano",
    url: "https://www.xano.com",
    description: "Build scalable backends for apps with APIs and logic",
    category: "Database and Backend"
  },

  // E-commerce
  {
    name: "Shopify",
    url: "https://www.shopify.com",
    description: "Build e-commerce stores with payment processing",
    category: "E-commerce"
  },
  {
    name: "Gumroad",
    url: "https://www.gumroad.com",
    description: "Sell digital products and services with ease",
    category: "E-commerce"
  }
];
