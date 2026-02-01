import { useState } from "react";

function Commit() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState("");

  function handleCommit() {
    fetch("http://localhost:8000/commit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          setResult("✅ Commit created");
          setMessage("");
        } else {
          setResult("❌ " + data.message);
        }
      });
  }

  return (
    <div>
      <h3>Commit</h3>

      <input
        type="text"
        placeholder="Commit message"
        value={message}
        onChange={e => setMessage(e.target.value)}
      />

      <button onClick={handleCommit} disabled={!message}>
        Commit
      </button>

      <p>{result}</p>
    </div>
  );
}

export default Commit;