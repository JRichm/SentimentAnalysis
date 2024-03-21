import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import SearchPage from "./pages/search"
import TestFormPage from "./pages/testForm"


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/search" element={<SearchPage />} />
        <Route path="/testForm" element={<TestFormPage />} />
      </Routes>
    </Router>
  )
}

export default App;
