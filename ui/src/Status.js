import { useEffect, useState } from "react";

function Status() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/status")
      .then(res => res.json())
      .then(result => setData(result));
  }, []);

  if (!data) return <p>Loading status...</p>;
  if (!data.success) return <p>{data.message}</p>;

  return (
    <div>
      <h3>Status</h3>

      <p>🟢 New files</p>
      <ul>
        {data.new.map(f => <li key={f}>{f}</li>)}
      </ul>

      <p>🟡 Modified files</p>
      <ul>
        {data.modified.map(f => <li key={f}>{f}</li>)}
      </ul>

      <p>🔴 Deleted files</p>
      <ul>
        {data.deleted.map(f => <li key={f}>{f}</li>)}
      </ul>
    </div>
  );
}

export default Status;