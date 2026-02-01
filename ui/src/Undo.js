import { useState } from "react";

function Undo() {
  const [result, setResult] = useState("");

  function handleUndo() {
    fetch("http://localhost:8000/undo", {
      method: "POST"
    })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          setResult("✅ Undo successful");
        } else {
          setResult("❌ " + data.message);
        }
      });
  }

  return (
    <div>
      <h3>Undo Last Commit</h3>

      <button onClick={handleUndo}>
        Undo
      </button>

      <p>{result}</p>
    </div>
  );
}

export default Undo;