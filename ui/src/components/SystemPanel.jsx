import React, { useEffect, useState } from 'react';
import { api } from '../services/api.js';

const SystemPanel = ({ className = '' }) => {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    api.get('/system/stats').then((response) => setStats(response.data)).catch(() => setStats(null));
  }, []);

  return (
    <section className={`panel bg-slate-900/60 rounded-xl p-4 border border-slate-800 ${className}`}>
      <h2 className="text-xl font-semibold mb-3">System Monitor</h2>
      {stats ? (
        <dl className="grid grid-cols-2 gap-3 text-sm">
          <div>
            <dt className="text-slate-400">Hostname</dt>
            <dd className="font-semibold">{stats.hostname}</dd>
          </div>
          <div>
            <dt className="text-slate-400">OS</dt>
            <dd className="font-semibold">{stats.os}</dd>
          </div>
          <div>
            <dt className="text-slate-400">CPU</dt>
            <dd className="font-semibold">{stats.cpu_percent}%</dd>
          </div>
          <div>
            <dt className="text-slate-400">Memory</dt>
            <dd className="font-semibold">{stats.memory_percent}%</dd>
          </div>
          <div>
            <dt className="text-slate-400">Disk</dt>
            <dd className="font-semibold">{stats.disk_percent}%</dd>
          </div>
        </dl>
      ) : (
        <p className="text-xs text-slate-500">System telemetry unavailable.</p>
      )}
    </section>
  );
};

export default SystemPanel;
