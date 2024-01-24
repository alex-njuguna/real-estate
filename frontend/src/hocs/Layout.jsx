import { Navbar } from "../components/Components";

const Layout = (props) => {
  return (
    <div>
      <Navbar />
      {props.children}
    </div>
  );
};

export default Layout;
