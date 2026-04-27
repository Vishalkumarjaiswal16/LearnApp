import Students from "../components/Students";
import Courses from "../components/Courses";
import Progress from "../components/Progress";
import "../App.css";

function Dashboard() {
  return (
    <div className="dashboard-wrapper">
      <header className="dashboard-header-container">
        <h1 className="dashboard-title">Learning Dashboard <span className="emoji">🚀</span></h1>
        <p className="dashboard-subtitle">Monitor your students' progress, manage courses, and track performance all in one place!</p>
      </header>
      
      <div className="dashboard-content grid-layout">
        <div className="dashboard-column">
          <Students />
        </div>
        <div className="dashboard-column">
          <Courses />
        </div>
        <div className="dashboard-column full-width">
          <Progress />
        </div>
      </div>
    </div>
  );
}

export default Dashboard;