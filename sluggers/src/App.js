import './App.css';
import TeamManager from "./TeamManager";

function App() {
  return (
    <div className="App">
        <header>
            <h3>Mario Super Sluggers Team Builder</h3>
        </header>
        <main>
            <div className="graph-container">
                <p>Positive</p>
                <iframe title="positvie connections" src="/graph.html" scrolling="no"></iframe>
            </div>
            <div className="graph-container">
                <p>Negetive</p>
                <iframe title="negetive connections" src="/graph2.html" scrolling="no"></iframe>
            </div>
        </main>
        <TeamManager/>
    </div>
  );
}

export default App;
