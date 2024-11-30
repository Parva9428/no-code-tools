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
        const response = await fetch('/api/tools');
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

  const filteredTools = tools.filter(tool => {
    const matchesCategory = selectedCategory === 'All' || tool.category === selectedCategory;
    const matchesSearch = tool.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      tool.description.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  if (loading) {
    return (
      <main className="min-h-screen p-8">
        <div className="max-w-7xl mx-auto">
          <div className="flex justify-between items-center mb-8">
            <h1 className="text-4xl font-bold">No-Code Tools Directory</h1>
            <ThemeToggle />
          </div>
          <div className="text-center py-8">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900 mx-auto"></div>
            <p className="mt-4">Loading tools...</p>
          </div>
        </div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="min-h-screen p-8">
        <div className="max-w-7xl mx-auto">
          <div className="flex justify-between items-center mb-8">
            <h1 className="text-4xl font-bold">No-Code Tools Directory</h1>
            <ThemeToggle />
          </div>
          <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4" role="alert">
            <p className="font-bold">Error</p>
            <p>{error}</p>
          </div>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen p-8">
      <div className="max-w-7xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-4xl font-bold">No-Code Tools Directory</h1>
          <ThemeToggle />
        </div>

        <div className="mb-8 space-y-4">
          <input
            type="text"
            placeholder="Search tools..."
            className="w-full p-2 border rounded-lg dark:bg-gray-800 dark:border-gray-700"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          
          <div className="flex flex-wrap gap-2">
            {categories.map((category) => (
              <button
                key={category}
                onClick={() => setSelectedCategory(category)}
                className={`px-4 py-2 rounded-full ${
                  selectedCategory === category
                    ? 'bg-blue-500 text-white'
                    : 'bg-gray-200 dark:bg-gray-700'
                }`}
              >
                {category}
              </button>
            ))}
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredTools.map((tool, index) => (
            <div
              key={index}
              className="border rounded-lg p-6 hover:shadow-lg transition-shadow dark:bg-gray-800 dark:border-gray-700"
            >
              <h3 className="text-xl font-semibold mb-2">{tool.name}</h3>
              <p className="text-gray-600 dark:text-gray-300 mb-4">{tool.description}</p>
              <div className="flex justify-between items-center">
                <span className="bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-100 px-3 py-1 rounded-full text-sm">
                  {tool.category}
                </span>
                <a
                  href={tool.website}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-blue-500 hover:text-blue-600 dark:hover:text-blue-400"
                >
                  Visit Website →
                </a>
              </div>
            </div>
          ))}
        </div>

        {filteredTools.length === 0 && (
          <div className="text-center py-8">
            <p className="text-gray-500">No tools found matching your criteria.</p>
          </div>
        )}
      </div>
    </main>
  );
}
