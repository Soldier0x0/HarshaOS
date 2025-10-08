import React, { useState } from 'react';
import { api } from '../services/api.js';

const NoahChat = ({ className = '' }) => {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('Ask Noah anything about your local data.');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const { data } = await api.post('/ai/chat', { prompt });
    setResponse(data.response);
  };

  return (
    <section className={`panel bg-slate-900/60 rounded-xl p-4 border border-slate-800 flex flex-col ${className}`}>
      <h2 className="text-xl font-semibold mb-2">Noah AI Companion</h2>
      <form onSubmit={handleSubmit} className="flex gap-2 mb-3">
        <input
          type="text"
          value={prompt}
          onChange={(event) => setPrompt(event.target.value)}
          placeholder="Summarise today's automation activity..."
          className="flex-1 rounded bg-slate-950/60 border border-slate-800 px-3 py-2 text-sm focus:outline-none focus:border-accent"
        />
        <button type="submit" className="px-3 py-2 text-sm rounded bg-accent text-slate-950">
          Send
        </button>
      </form>
      <div className="text-sm text-slate-200 bg-slate-950/40 rounded p-3 flex-1 overflow-y-auto">
        {response}
      </div>
    </section>
  );
};

export default NoahChat;
