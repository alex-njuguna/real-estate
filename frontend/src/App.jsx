import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./hocs/Layout";
import {
  About,
  Contact,
  Home,
  ListingDetail,
  Listings,
  Signin,
  Signup,
} from "./containers/Containers";
import { NotFound } from "./components/Components";

import "./sass/main.scss";

function App() {
  return (
    <>
      <BrowserRouter>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="about/" element={<About />} />
            <Route path="contact/" element={<Contact />} />
            <Route path="listings/" element={<Listings />} />
            <Route path="listings/:id" element={<ListingDetail />} />
            <Route path="signin/" element={<Signin />} />
            <Route path="signup/" element={<Signup />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </Layout>
      </BrowserRouter>
    </>
  );
}

export default App;
