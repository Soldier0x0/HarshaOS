import React, { useEffect, useState } from 'react';
import { api } from '../services/api.js';

const EmailPanel = ({ className = '' }) => {
  const [digest, setDigest] = useState([]);

  useEffect(() => {
    api.get('/mail/digest').then((response) => setDigest(response.data)).catch(() => setDigest([]));
  }, []);

  return (
    <section className={`panel bg-slate-900/60 rounded-xl p-4 border border-slate-800 ${className}`}>
      <header className="flex items-center justify-between mb-2">
        <h2 className="text-xl font-semibold">Email Digest</h2>
        <button
          type="button"
          className="px-3 py-1 text-xs rounded bg-accent text-slate-950"
          onClick={() => api.post('/mail/refresh')}
        >
          Refresh
        </button>
      </header>
      <div className="space-y-2 overflow-y-auto max-h-60 pr-2">
        {digest.map((item) => (
          <article key={item.subject} className="bg-slate-950/40 rounded p-2">
            <h3 className="text-sm font-semibold">{item.subject}</h3>
            <p className="text-xs text-slate-400">{item.sender}</p>
            <p className="text-xs mt-1">{item.summary}</p>
          </article>
        ))}
        {digest.length === 0 && <p className="text-xs text-slate-500">Connect email to populate digest.</p>}
      </div>
    </section>
  );
};

export default EmailPanel;
