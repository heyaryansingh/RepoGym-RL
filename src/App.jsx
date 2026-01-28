import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Terminal, Shield, BarChart3, Cpu, Code2, PlayCircle,
  CheckCircle2, ChevronRight, X
} from 'lucide-react';

const demoData = [
  {
    title: "Task Initialization",
    desc: "Loading 'bugfix-simple' task into RG-721a container.",
    cmd: "repogym reset --task bugfix-simple",
    output: "Environment Ready. Source code synced.",
    metrics: { pass: 0, reward: 0.0 }
  },
  {
    title: "Baseline Evaluation",
    desc: "Running initial test suite to establish measurable baseline.",
    cmd: "agent.step(action='run_tests')",
    output: "test_strings.py::test_kebab_to_camel FAILED",
    metrics: { pass: 0, reward: -1.0 }
  },
  {
    title: "Automated Repair",
    desc: "Agent applies code improvement via 'write_file'.",
    cmd: "agent.step(action='write_file', content='...')",
    output: "File saved. Static analysis: Complexity ↓, MI ↑",
    metrics: { pass: 0, reward: -0.83 }
  },
  {
    title: "Success Verification",
    desc: "Final verification. Functional tests pass, completing episode.",
    cmd: "agent.step(action='run_tests')",
    output: "test_strings.py::test_kebab_to_camel PASSED",
    metrics: { pass: 1, reward: 1.175 }
  }
];

const App = () => {
  const [showDemo, setShowDemo] = useState(false);
  const [demoStep, setDemoStep] = useState(0);

  return (
    <div className="app-root">
      {/* Hero Section */}
      <section className="hero">
        <div className="glow" style={{ top: '-10%', left: '-10%', background: 'var(--primary)' }} />
        <div className="glow" style={{ bottom: '-10%', right: '-10%', background: 'var(--secondary)' }} />

        <motion.div
          className="container flex flex-col items-center text-center"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <h1 className="gradient-text">RepoGym<span className="accent-text">-RL</span></h1>
          <p className="text-dim" style={{ maxWidth: '700px', margin: '24px 0 40px', fontSize: '1.25rem' }}>
            A high-fidelity, containerized reinforcement learning environment for local-first software engineering agent evaluation.
          </p>
          <div className="flex gap-md">
            <button className="btn btn-primary" onClick={() => setShowDemo(true)}>
              <PlayCircle size={20} /> Deploy Demo
            </button>
            <button className="btn btn-outline">
              <Code2 size={20} /> View Source
            </button>
          </div>

          <div className="console-mock glass">
            <div className="console-dots">
              <div className="dot" style={{ background: '#ff5f56' }} />
              <div className="dot" style={{ background: '#ffbd2e' }} />
              <div className="dot" style={{ background: '#27c93f' }} />
            </div>
            <div className="font-mono" style={{ fontSize: '0.9rem' }}>
              <p style={{ color: 'var(--secondary)' }}>$ repogym reset --task bugfix-simple</p>
              <p className="text-muted">Environment initialized. Container [rg-721a] running.</p>
              <p style={{ color: 'var(--primary)', marginTop: '8px' }}>$ agent.step(command="run_tests")</p>
              <p style={{ color: 'var(--accent)' }}>Result: 1 failed, 0 passed (Functional Reward: -1.0)</p>
            </div>
          </div>
        </motion.div>
      </section>

      {/* Features Section */}
      <section className="container">
        <h2 className="text-center" style={{ marginBottom: '60px' }}>The Core Stack</h2>
        <div className="grid grid-cols-3 gap-lg">
          <FeatureCard
            icon={<Shield color="var(--secondary)" />}
            title="Ironclad Isolation"
            desc="Every episode runs in a fresh Docker sandbox. No side effects, absolute reproducibility."
          />
          <FeatureCard
            icon={<Cpu color="var(--primary)" />}
            title="Rich Action Space"
            desc="Structured Pydantic tool calls for listing files, writing code, and execution."
          />
          <FeatureCard
            icon={<BarChart3 color="var(--accent)" />}
            title="Scientific Rewards"
            desc="Functional test deltas combined with Radon-based static analysis nudges."
          />
        </div>
      </section>

      {/* Process Section */}
      <section className="container" style={{ margin: '100px auto' }}>
        <div className="card grid grid-cols-2 gap-3xl items-center">
          <div>
            <h2 style={{ marginBottom: '24px' }}>Measure What Matters</h2>
            <p className="text-dim" style={{ marginBottom: '32px' }}>
              RepoGym-RL isn't just a wrapper. It's a precise instrument for measuring agent performance.
              We track complexity, maintainability, and functional pass-rates in real-time.
            </p>
            <div className="flex flex-col gap-md">
              <div className="flex items-center gap-sm">
                <CheckCircle2 color="#27c93f" size={20} /> <span>Radon Static Analysis</span>
              </div>
              <div className="flex items-center gap-sm">
                <CheckCircle2 color="#27c93f" size={20} /> <span>Pytest Delta Tracking</span>
              </div>
              <div className="flex items-center gap-sm">
                <CheckCircle2 color="#27c93f" size={20} /> <span>JSONL Telemetry</span>
              </div>
            </div>
          </div>
          <div className="glass flex flex-col justify-center" style={{ height: '300px', padding: '40px' }}>
            <div className="flex gap-sm items-end" style={{ height: '100%' }}>
              {[0.4, 0.6, 0.5, 0.8, 0.7, 0.9, 0.85, 1].map((h, i) => (
                <div
                  key={i}
                  className={`reward-bar ${i === 7 ? 'active animate-pulse' : ''}`}
                  style={{ height: `${h * 100}%` }}
                />
              ))}
            </div>
          </div>
        </div>
      </section>

      <footer className="container text-center text-muted" style={{ padding: '60px 0', borderTop: '1px solid var(--glass-border)' }}>
        RepoGym-RL &copy; 2026 • Advanced Agentic Evaluation
      </footer>

      {/* Interactive Demo Modal */}
      <AnimatePresence>
        {showDemo && (
          <motion.div
            className="modal-overlay"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          >
            <motion.div
              className="modal-content"
              initial={{ scale: 0.9, y: 20 }}
              animate={{ scale: 1, y: 0 }}
            >
              <div className="modal-header">
                <div>
                  <h3>Interactive Demo: <span className="accent-text">bugfix-simple</span></h3>
                  <p className="text-muted" style={{ fontSize: '0.8rem' }}>Step {demoStep + 1} of 4</p>
                </div>
                <button className="btn btn-outline" style={{ padding: '8px' }} onClick={() => setShowDemo(false)}>
                  <X size={20} />
                </button>
              </div>

              <div className="modal-body">
                <div className="modal-side flex flex-col gap-lg">
                  <div>
                    <h3 style={{ marginBottom: '12px' }}>{demoData[demoStep].title}</h3>
                    <p className="text-dim">{demoData[demoStep].desc}</p>
                  </div>

                  <div className="glass flex flex-col justify-center" style={{ height: '160px', padding: '24px' }}>
                    <div className="flex gap-xs items-end" style={{ height: '100%' }}>
                      {[0.3, 0.5, 0.4, 0.7, 0.6, 0.8, demoStep * 0.3].map((h, i) => (
                        <div key={i} className="reward-bar active" style={{ height: `${h * 100}%`, opacity: 0.3 + (i * 0.1) }} />
                      ))}
                    </div>
                  </div>

                  <div className="grid grid-cols-2 gap-md">
                    <div className="glass" style={{ padding: '16px' }}>
                      <p className="text-muted" style={{ fontSize: '0.7rem', marginBottom: '4px' }}>Tests Passed</p>
                      <p className="font-mono" style={{ fontSize: '1.5rem', color: 'var(--secondary)' }}>{demoData[demoStep].metrics.pass}/1</p>
                    </div>
                    <div className="glass" style={{ padding: '16px', textAlign: 'right' }}>
                      <p className="text-muted" style={{ fontSize: '0.7rem', marginBottom: '4px' }}>Reward Signal</p>
                      <p className="font-mono" style={{ fontSize: '1.5rem', color: demoData[demoStep].metrics.reward >= 0 ? '#27c93f' : 'var(--accent)' }}>
                        {demoData[demoStep].metrics.reward.toFixed(2)}
                      </p>
                    </div>
                  </div>
                </div>

                <div className="modal-main flex flex-col gap-lg">
                  <div className="flex flex-col gap-sm">
                    <p className="text-muted flex items-center gap-sm" style={{ fontSize: '0.75rem' }}><Terminal size={14} /> Console</p>
                    <div className="glass font-mono" style={{ padding: '16px', fontSize: '0.8rem', background: '#050505' }}>
                      <p style={{ color: 'var(--secondary)' }}>$ {demoData[demoStep].cmd}</p>
                      <p style={{ color: demoStep === 1 ? 'var(--accent)' : '#27c93f', marginTop: '4px' }}>{demoData[demoStep].output}</p>
                    </div>
                  </div>

                  <div className="flex flex-col gap-sm" style={{ flex: 1 }}>
                    <p className="text-muted flex items-center gap-sm" style={{ fontSize: '0.75rem' }}><Code2 size={14} /> string_utils.py</p>
                    <div className="glass font-mono" style={{ padding: '20px', fontSize: '0.75rem', background: '#050505', flex: 1 }}>
                      {demoStep < 2 ? (
                        <div style={{ color: 'rgba(255,255,255,0.4)' }}>
                          def kebab_to_camel(text):<br />
                          &nbsp;&nbsp;if not text: return ""<br />
                          &nbsp;&nbsp;parts = text.split("-")<br />
                          &nbsp;&nbsp;<span style={{ color: 'var(--accent)', background: 'rgba(244,63,94,0.1)', padding: '0 4px' }}># BUG: Incorrect join logic</span><br />
                          &nbsp;&nbsp;return "".join(p.capitalize() for p in parts)
                        </div>
                      ) : (
                        <div style={{ color: 'rgba(255,255,255,0.4)' }}>
                          def kebab_to_camel(text):<br />
                          &nbsp;&nbsp;if not text: return ""<br />
                          &nbsp;&nbsp;parts = text.split("-")<br />
                          &nbsp;&nbsp;<span style={{ color: '#27c93f', background: 'rgba(39,201,63,0.1)', padding: '0 4px' }}># FIXED: Slice first element</span><br />
                          &nbsp;&nbsp;return parts[0] + "".join(p.capitalize() for p in parts[1:])
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              </div>

              <div className="modal-footer">
                <div className="flex gap-sm">
                  {[0, 1, 2, 3].map(i => (
                    <div key={i} style={{ width: '40px', height: '3px', background: i <= demoStep ? 'var(--primary)' : 'rgba(255,255,255,0.1)', borderRadius: '2px' }} />
                  ))}
                </div>
                <div className="flex gap-md">
                  {demoStep > 0 && <button className="btn btn-outline" onClick={() => setDemoStep(s => s - 1)}>Back</button>}
                  <button
                    className="btn btn-primary"
                    onClick={() => demoStep < 3 ? setDemoStep(s => s + 1) : setShowDemo(false)}
                  >
                    {demoStep < 3 ? 'Next Step' : 'Close Demo'} <ChevronRight size={16} />
                  </button>
                </div>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

const FeatureCard = ({ icon, title, desc }) => (
  <div className="card">
    <div style={{ marginBottom: '20px', display: 'inline-flex', padding: '12px', background: 'rgba(255,255,255,0.03)', borderRadius: '12px' }}>
      {icon}
    </div>
    <h3 style={{ marginBottom: '12px' }}>{title}</h3>
    <p className="text-dim" style={{ fontSize: '0.9rem' }}>{desc}</p>
  </div>
);

export default App;
