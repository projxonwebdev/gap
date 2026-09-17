import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ScrollToTop from './components/ScrollToTop';
import Layout from './components/Layout';
import Home from './pages/Home';
import Portfolio from './pages/Portfolio';
import Team from './pages/Team';
import MIP from './pages/MIP';
import Coaching from './pages/Coaching';
import Contact from './pages/Contact';
import WorkWithGap from './pages/WorkWithGap';

function App() {
  return (
    <Router>
      <ScrollToTop />
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="portfolio" element={<Portfolio />} />
          <Route path="team" element={<Team />} />
          <Route path="mip" element={<MIP />} />
          <Route path="coaching" element={<Coaching />} />
          <Route path="contact" element={<Contact />} />
          <Route path="work" element={<WorkWithGap />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
