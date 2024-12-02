'use client';

import { useState, useEffect } from 'react';
import { Tool } from './types';
import ThemeToggle from '../components/ThemeToggle';

export default function Home() {
  const [tools, setTools] = useState<Tool[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedCategory, setSelectedCategory] = useState<string>('All');
  const [searchQuery, setSearchQuery] = useState('');

  const categories = [
    'All',
    'Website Builder',
    'App Builder',
    'E-commerce',
    'Automation',
    'Design',
    'AI Tools',
    'Productivity',
    'Business Tools',
    'Forms',
    'Specialized Tools',
    'Marketing'
  ];

  useEffect(() => {
    const fetchTools = async () => {
      try {
        setLoading(true);
        setError(null);
        const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'https://no-code-tools-backend.onrender.com';
        console.log('Fetching from:', `${apiUrl}/api/tools`);
        const response = await fetch(`${apiUrl}/api/tools`, {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }
        });
        if (!response.ok) {
          throw new Error(`Failed to fetch tools: ${response.status} ${response.statusText}`);
        }
        const data = await response.json();
        setTools(Array.isArray(data) ? data : []);
      } catch (err) {
        console.error('Error fetching tools:', err);
        setError(err instanceof Error ? err.message : 'Failed to load tools');
      } finally {
        setLoading(false);
      }
    };

    fetchTools();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900 mx-auto"></div>
          <p className="mt-4">Loading...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center text-red-600">
          <p>Error: {error}</p>
          <button 
            onClick={() => window.location.reload()} 
            className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Retry
          </button>
        </div>
      </div>
    );
  }

  const filteredTools = tools.filter(tool => {
    if (selectedCategory !== 'All' && tool.category !== selectedCategory) {
      return false;
    }
    if (searchQuery) {
      const query = searchQuery.toLowerCase();
      return (
        tool.name.toLowerCase().includes(query) ||
        tool.description.toLowerCase().includes(query) ||
        tool.category.toLowerCase().includes(query)
      );
    }
    return true;
  });

  return (
    <main className="min-h-screen p-8">
      <div className="max-w-7xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold">No-Code Tools Directory</h1>
          <ThemeToggle />
        </div>
        
        <div className="mb-8">
          <input
            type="text"
            placeholder="Search tools..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full p-2 border rounded dark:bg-gray-700 dark:border-gray-600"
          />
        </div>

        <div className="flex flex-wrap gap-2 mb-8">
          {categories.map((category) => (
            <button
              key={category}
              onClick={() => setSelectedCategory(category)}
              className={`px-4 py-2 rounded ${
                selectedCategory === category
                  ? 'bg-blue-500 text-white'
                  : 'bg-gray-200 dark:bg-gray-700'
              }`}
            >
              {category}
            </button>
          ))}
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredTools.map((tool) => (
            <div
              key={tool.id}
              className="border rounded-lg p-6 dark:bg-gray-800 dark:border-gray-700"
            >
              <h2 className="text-xl font-semibold mb-2">{tool.name}</h2>
              <p className="text-gray-600 dark:text-gray-300 mb-4">
                {tool.description}
              </p>
              <div className="flex justify-between items-center">
                <span className="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-100 px-3 py-1 rounded">
                  {tool.category}
                </span>
                <a
                  href={tool.website}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-500 hover:text-blue-600"
                >
                  Visit →
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
