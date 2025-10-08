import React, { useEffect, useState } from 'react';
import { api } from '../services/api.js';

const FinancePanel = ({ className = '' }) => {
  const [summary, setSummary] = useState([]);

  useEffect(() => {
    api.get('/finance/summary').then((response) => setSummary(response.data)).catch(() => setSummary([]));
  }, []);

  return (
    <section className={`panel bg-slate-900/60 rounded-xl p-4 border border-slate-800 ${className}`}>
      <h2 className="text-xl font-semibold mb-2">Expense Summary</h2>
      <ul className="space-y-2 text-sm">
        {summary.map((item) => (
          <li key={item.category} className="flex justify-between bg-slate-950/40 rounded p-2">
            <span>{item.category}</span>
            <span className="font-semibold">${item.total.toFixed(2)}</span>
          </li>
        ))}
        {summary.length === 0 && <li className="text-xs text-slate-500">Import transactions to view analytics.</li>}
      </ul>
    </section>
  );
};

export default FinancePanel;
