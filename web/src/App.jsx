import React from 'react';
import { motion } from 'framer-motion';
import { Terminal, Shield, BarChart3, Cpu, Code2, PlayCircle, CheckCircle2 } from 'lucide-react';

const App = () => {
  return (
    <div className="bg-black text-white min-h-screen">
      {/* Hero Section */}
      <section className="relative flex flex-col items-center justify-center text-center overflow-hidden">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-purple-900/20 blur-[120px] rounded-full" />
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-cyan-900/20 blur-[120px] rounded-full" />

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h1 className="gradient-text">RepoGym<span className="accent-text">-RL</span></h1>
          <p className="max-w-2xl mx-auto mb-8 text-xl">
            A high-fidelity, containerized reinforcement learning environment for local-first software engineering agent evaluation.
          </p>
          <div className="flex gap-4 justify-center">
            <button className="btn-primary flex items-center gap-2">
              <PlayCircle size={20} /> Deploy Demo
            </button>
            <button className="glass px-6 py-3 rounded-lg flex items-center gap-2 border-white/10 hover:bg-white/5 transition-all">
              <Code2 size={20} /> View Docs
            </button>
          </div>
        </motion.div>

        {/* Console Demo Mockup */}
        <motion.div
          className="mt-20 glass w-full max-w-4xl p-6 text-left font-mono text-sm border-white/5 relative group"
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.4 }}
        >
          <div className="flex gap-2 mb-4 border-b border-white/5 pb-2">
            <div className="w-3 h-3 rounded-full bg-red-500/50" />
            <div className="w-3 h-3 rounded-full bg-yellow-500/50" />
            <div className="w-3 h-3 rounded-full bg-green-500/50" />
            <span className="ml-4 text-xs text-white/40">repogym shell --task bugfix-simple</span>
          </div>
          <div className="space-y-2">
            <p className="text-cyan-400">$ repogym reset --task bugfix-simple</p>
            <p className="text-white/60">Environment initialized. Container [rg-721a] running.</p>
            <p className="text-purple-400">$ agent.step(command="run_tests")</p>
            <p className="text-rose-400">Result: 1 failed, 0 passed (Functional Reward: -1.0)</p>
            <p className="text-green-400">_</p>
          </div>
          <div className="absolute -inset-0.5 bg-gradient-to-r from-purple-500 to-cyan-500 rounded-2xl opacity-0 group-hover:opacity-10 transition-opacity pointer-events-none" />
        </motion.div>
      </section>

      {/* Features Grid */}
      <section className="py-20">
        <h2 className="text-center mb-16">The Core Stack</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <FeatureCard
            icon={<Shield className="text-cyan-400" />}
            title="Ironclad Isolation"
            desc="Every episode runs in a fresh Docker sandbox. No side effects, absolute reproducibility."
          />
          <FeatureCard
            icon={<Cpu className="text-purple-400" />}
            title="Rich Action Space"
            desc="Structured Pydantic tool calls for listing files, writing code, and execution."
          />
          <FeatureCard
            icon={<BarChart3 className="text-rose-400" />}
            title="Scientific Rewards"
            desc="Functional test deltas combined with Radon-based static analysis nudges."
          />
        </div>
      </section>

      {/* Engineering Process */}
      <section className="bg-surface-color/50 rounded-[40px] py-16 px-8 mb-20">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
          <div>
            <h2 className="mb-6">Measure What Matters</h2>
            <p className="mb-8">
              RepoGym-RL isn't just a wrapper. It's a precise instrument for measuring agent performance.
              We track cyclomatic complexity, maintainability indexes, and test pass-rates in real-time.
            </p>
            <ul className="space-y-4">
              <li className="flex items-center gap-3"><CheckCircle2 className="text-green-500" size={18} /> Radon-based Static Analysis</li>
              <li className="flex items-center gap-3"><CheckCircle2 className="text-green-500" size={18} /> Pytest Delta Tracking</li>
              <li className="flex items-center gap-3"><CheckCircle2 className="text-green-500" size={18} /> JSONL Trajectory Telemetry</li>
            </ul>
          </div>
          <div className="glass p-8 border-white/5 aspect-video flex flex-col justify-center">
            <div className="h-2 w-3/4 bg-white/10 rounded mb-4" />
            <div className="h-2 w-1/2 bg-white/5 rounded mb-8" />
            <div className="flex justify-between items-end gap-2">
              <div className="w-1/6 bg-cyan-500/50 rounded-t h-20" />
              <div className="w-1/6 bg-purple-500/50 rounded-t h-32" />
              <div className="w-1/6 bg-cyan-500/50 rounded-t h-24" />
              <div className="w-1/6 bg-purple-500/80 rounded-t h-48 animate-pulse" />
              <div className="w-1/6 bg-rose-500/40 rounded-t h-16" />
              <div className="w-1/6 bg-cyan-500/60 rounded-t h-28" />
            </div>
            <p className="text-xs text-center mt-4 text-white/30">Live Reward Signal Breakdown</p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-white/5 py-12 text-center text-sm text-white/20">
        RepoGym-RL &copy; 2025 • Designed for Advanced Agentic Evaluation
      </footer>
    </div>
  );
};

const FeatureCard = ({ icon, title, desc }) => (
  <div className="glass p-8 border-white/5 hover:border-white/10 transition-all hover:translate-y-[-4px]">
    <div className="mb-4 inline-block p-3 rounded-xl bg-white/5">{icon}</div>
    <h3 className="text-xl font-bold mb-2">{title}</h3>
    <p className="text-sm">{desc}</p>
  </div>
);

export default App;
