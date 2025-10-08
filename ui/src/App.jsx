import React, { useEffect } from 'react';
import anime from 'animejs';
import Dashboard from './components/Dashboard.jsx';
import EmailPanel from './components/EmailPanel.jsx';
import NotesPanel from './components/NotesPanel.jsx';
import FinancePanel from './components/FinancePanel.jsx';
import SystemPanel from './components/SystemPanel.jsx';
import NoahChat from './components/NoahChat.jsx';
import Settings from './components/Settings.jsx';

const App = () => {
  useEffect(() => {
    anime({
      targets: '.panel',
      opacity: [0, 1],
      translateY: [12, 0],
      delay: anime.stagger(80),
      duration: 600,
      easing: 'easeOutQuad'
    });
  }, []);

  return (
    <div className="min-h-screen p-6 grid gap-4 grid-cols-12">
      <header className="col-span-12 flex justify-between items-center">
        <h1 className="text-3xl font-semibold">HarshaOS Dashboard</h1>
        <Settings />
      </header>
      <Dashboard className="col-span-12" />
      <EmailPanel className="col-span-4" />
      <NotesPanel className="col-span-4" />
      <FinancePanel className="col-span-4" />
      <SystemPanel className="col-span-6" />
      <NoahChat className="col-span-6" />
    </div>
  );
};

export default App;
