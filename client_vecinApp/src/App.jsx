import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Login } from './pages/Login';
import { PanelAdmin } from './pages/PanelAdmin';
import { PanelResident } from './pages/PanelResident';
import { Register } from './pages/Register';
function App() {
  return (
   <BrowserRouter>
    <Routes>
      <Route path="/" element={<h1>Home Page</h1>} />
      <Route path="/about" element={<h1>About Page</h1>} />
      <Route path="/register" element={<Register />} />
      <Route path="/login" element={<Login />} />
      <Route path="/admin" element={<PanelAdmin />} />
      <Route path="/resident" element={<PanelResident />} />
    </Routes>
   </BrowserRouter>
  );
}

export default App;