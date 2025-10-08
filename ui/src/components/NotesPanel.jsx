import React, { useEffect, useState } from 'react';
import { api } from '../services/api.js';

const NotesPanel = ({ className = '' }) => {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    api.get('/notes/list').then((response) => setNotes(response.data)).catch(() => setNotes([]));
  }, []);

  return (
    <section className={`panel bg-slate-900/60 rounded-xl p-4 border border-slate-800 ${className}`}>
      <h2 className="text-xl font-semibold mb-2">Notes Vault</h2>
      <ul className="space-y-2 text-sm">
        {notes.map((note) => (
          <li key={note.path} className="bg-slate-950/40 rounded p-2">
            <p className="font-semibold">{note.title}</p>
            <p className="text-xs text-slate-400">{note.summary}</p>
          </li>
        ))}
        {notes.length === 0 && <li className="text-xs text-slate-500">Add markdown files to the notes directory.</li>}
      </ul>
    </section>
  );
};

export default NotesPanel;
