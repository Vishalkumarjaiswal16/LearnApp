import { useEffect, useState } from "react";
import api from "../api";
import AddProgress from "./AddProgress";

function Progress() {
  const [progress, setProgress] = useState([]);

  const fetchProgress = () => {
    api.get("/progress")
      .then(res => setProgress(res.data.data));
  };

  useEffect(() => {
    fetchProgress();
  }, []);

  return (
    <div className="card">
      <AddProgress onProgressAdded={fetchProgress} />

      <h2 style={{ marginTop: '20px' }}>Progress</h2>
      <ul className="item-list">
        {progress.map((p, index) => (
          <li key={index}>
            <strong>{p.name}</strong> - {p.course_name} → {p.completion_percentage}%
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Progress;