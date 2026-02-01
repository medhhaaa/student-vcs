import { useState } from "react";
import Status from "./Status";
import Log from "./Log";
import Commit from "./Commit";
import Undo from "./Undo";

function App() {
  const [page, setPage] = useState("home");

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>Student VCS</h2>

      <button onClick={() => setPage("status")}>Status</button>
      <button onClick={() => setPage("log")}>Log</button>
      <button onClick={() => setPage("commit")}>Commit</button>
      <button onClick={() => setPage("undo")}>Undo</button>

      <hr />

      {page === "status" && <Status />}
      {page === "log" && <Log />}
      {page === "commit" && <Commit />}
      {page === "undo" && <Undo />}
      {page === "home" && <p>Select an option</p>}
    </div>
  );
}

export default App;