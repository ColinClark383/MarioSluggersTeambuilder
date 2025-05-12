import { useState } from "react";

const TeamManager = () => {
  const [player1team, setPlayer1Team] = useState(Array(9).fill("empty"));
  const [player2team, setPlayer2Team] = useState(Array(9).fill("empty"));
  const [inputs, setInputs] = useState(Array(18).fill(""));
  const [error, setError] = useState("");

  const clearCells = () => {
    const table = document.getElementById("choiceTable");
    const rows = table.querySelectorAll("tbody tr");
    // Reset all cells to white
    rows.forEach(row => {
    row.querySelectorAll("td").forEach(cell => {
        cell.style.backgroundColor = 'white';
    });
    });
  }

  // Function to clear teams
  const clearTeams = () => {
    setPlayer1Team(Array(9).fill("empty"));
    setPlayer2Team(Array(9).fill("empty"));
    setInputs(Array(18).fill(""));
    clearCells();
    setError("");
  };

  // Function to handle input changes
  const handleInputChange = (index, value) => {
    const newInputs = [...inputs];
    newInputs[index] = value;
    setInputs(newInputs);

    if (index < 9) {
      const newTeam1 = [...player1team];
      newTeam1[index] = value || "empty";
      setPlayer1Team(newTeam1);
    } else {
      const newTeam2 = [...player2team];
      newTeam2[index - 9] = value || "empty";
      setPlayer2Team(newTeam2);
    }
  };

  // Function to highlight table cells
  const highlightTable = (dataArray) => {
    const table = document.getElementById("choiceTable");
    const rows = table.querySelectorAll("tbody tr");

      clearCells();
    // Highlight specific cells
    dataArray.forEach((index) => {
      const rowIndex = Math.floor(index / 9) + 1;
      const colIndex = (index % 9);
      const row = rows[rowIndex];
      const cell = row.querySelectorAll("td")[colIndex];
      cell.style.backgroundColor = 'red';
    });
  };

  // Function to send character roster to the backend
const validateTeams = () => {
    const roster = {
      player1team,
      player2team,
    };
  
    fetch('http://127.0.0.1:5000/api/roster', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(roster), // Send the roster as JSON
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        const dataArray = data["data"]
            highlightTable(dataArray)
            if(dataArray.length !== 0){
                setError("Invalid team selection!\nCheck for duplicate names and incorrect player names.");
            }
            else{
                setError("Teams are valid!")
            }
      })
      .catch((error) => {
        console.error('Error sending roster:', error);
      });
  };
  

  return (
    <div>
      <table id="choiceTable">
        <tbody>
            <tr>
                <td/>
                {[...Array(9)].map((_, turnIndex) => ( 
                    <th>Pick {turnIndex+1}</th>
                ))}
            </tr>
          {[...Array(2)].map((_, teamIndex) => (
            <tr key={teamIndex}> Player {teamIndex + 1}
              {[...Array(9)].map((_, pickIndex) => {
                const index = teamIndex * 9 + pickIndex;
                return (
                  <td key={index}>
                    <input
                      type="text"
                      value={inputs[index]}
                      onChange={(e) => handleInputChange(index, e.target.value)}
                    />
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
      <div className="buttons">
      <button id="clear-button" onClick={clearTeams}>Clear Teams</button>
      <button onClick={validateTeams}>Validate Teams</button>
      <p className="error check">{error}</p>
      </div>
      
    </div>
  );
};

export default TeamManager;
