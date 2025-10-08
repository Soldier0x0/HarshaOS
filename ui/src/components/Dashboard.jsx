import React from 'react';

const Dashboard = ({ className = '' }) => (
  <section className={`panel bg-slate-900/60 rounded-xl p-4 border border-slate-800 ${className}`}>
    <h2 className="text-xl font-semibold mb-2">Overview</h2>
    <p className="text-sm text-slate-300">
      Welcome to HarshaOS v1.1. Connect your local services to see automation,
      notes, finance metrics and the Noah AI assistant in action.
    </p>
  </section>
);

export default Dashboard;
