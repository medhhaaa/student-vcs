import { useEffect, useState } from "react";

function Log() {
  const [log, setLog] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/log")
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          setLog(data.commits);
        }
      });
  }, []);

  return (
    <div>
      <h3>Commit History</h3>

      {log.map(c => (
        <div key={c.id} style={{ marginBottom: "10px" }}>
          <strong>{c.id}</strong>
          <div>{c.message}</div>
          <small>{c.timestamp}</small>
        </div>
      ))}
    </div>
  );
}

export default Log;