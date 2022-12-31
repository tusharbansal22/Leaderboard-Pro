import React, { useState, useEffect } from "react";
import "./App.css";
import { Grid } from "@material-ui/core";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import { Navbar } from "./components/Navbar.js";
import { CodeforcesTable } from "./components/CodeforcesTable.js";
import { CodechefTable } from "./components/CodechefTable";
import { GithubTable } from "./components/GithubTable";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { OpenlakeTable } from "./components/OpenlakeTable";
import Login from "./components/Login";
import Register from "./components/Register";
import { LeetcodeTable } from "./components/LeetcodeTable";

const darkTheme = createTheme({
  palette: {
    mode: "dark",
  },
  components: {
    MuiCssBaseline: {
      styleOverrides: {
        body: {
          scrollbarColor: "#686868 #686868",
          "&::-webkit-scrollbar, & *::-webkit-scrollbar": {
            backgroundColor: "#424242",
          },
          "&::-webkit-scrollbar-thumb, & *::-webkit-scrollbar-thumb": {
            borderRadius: 20,
            backgroundColor: "#636363",
            minHeight: 15,
          },
          "&::-webkit-scrollbar-thumb:hover, & *::-webkit-scrollbar-thumb:hover": {
            backgroundColor: "#4F4F4F",
          },
          "&::-webkit-scrollbar-corner, & *::-webkit-scrollbar-corner": {
            backgroundColor: "#686868",
          },
        },
      },
    },
  },
})

const lightTheme = createTheme({
  palette: {
    mode: "light",
  },
  components: {
    MuiCssBaseline: {
      styleOverrides: {
        body: {
          scrollbarColor: "#C1C1C1 #C1C1C1",
          "&::-webkit-scrollbar, & *::-webkit-scrollbar": {
            backgroundColor: "#F1F1F1",
          },
          "&::-webkit-scrollbar-thumb, & *::-webkit-scrollbar-thumb": {
            borderRadius: 20,
            backgroundColor: "#C1C1C1",
            minHeight: 15,
          },
          "&::-webkit-scrollbar-thumb:hover, & *::-webkit-scrollbar-thumb:hover": {
            backgroundColor: "#B5B5B5",
          },
          "&::-webkit-scrollbar-corner, & *::-webkit-scrollbar-corner": {
            backgroundColor: "#C1C1C1",
          },
        },
      },
    }
  }
})
function App() {
  const [codechefUsers, setCodechefUsers] = useState([]);
  const [darkmode, setDarkmode] = useState(false)
  const [codeforcesUsers, setCodeforcesUsers] = useState([]);
  const [leetcodeUsers,setLeetcodeUsers]=useState([]);
  const [openlakeContributor, setOpenlakeContributor] = useState([]);
  const [githubUser, setGithubUser] = useState([]);
  const toggle = () =>{
    setDarkmode(!darkmode);
    const g=localStorage.getItem('dark-mode');
    if(g==="off")
    localStorage.setItem('dark-mode',"on");
    else
    localStorage.setItem('dark-mode',"off");

  }
  useEffect(() => {
    const dm=localStorage.getItem('dark-mode')
    if(dm!=null)
    {
      if(dm==="on")
      setDarkmode(true);
      else
      setDarkmode(false);
    }

  }, []);
  useEffect(() => {
    fetch("http://localhost:8000/codeforces/")
      .then((res) => res.json())
      .then((res) => {
        setCodeforcesUsers(res);
      });
  }, []);

  useEffect(() => {
    fetch("http://localhost:8000/codechef/")
      .then((res) => res.json())
      .then((res) => {
        setCodechefUsers(res);
      });
  }, []);

  useEffect(() => {
    fetch("http://localhost:8000/openlake/")
      .then((res) => res.json())
      .then((res) => {
        setOpenlakeContributor(res);
      });
  }, []);
  
    useEffect(() => {
    fetch("http://localhost:8000/github/")
      .then((res) => res.json())
      .then((res) => {
        setGithubUser(res);
      });
  }, []);

  return (
    <ThemeProvider theme={darkmode ? darkTheme:lightTheme}>
      <CssBaseline />
      <Router>
        <div className="App">
          <Navbar darkmode={darkmode} toggle={toggle}/>
          <Grid container>
            <Grid item xs={6}>
              <Switch>
                <Route path="/codeforces">
                  <CodeforcesTable darkmode={darkmode} codeforcesUsers={codeforcesUsers} />
                </Route>
                <Route path="/codechef">
                  <CodechefTable darkmode={darkmode} codechefUsers={codechefUsers} />
                </Route>
                <Route path="/openlake">
                  <OpenlakeTable darkmode={darkmode} openlakeContributor={openlakeContributor} />
                </Route>
                <Route path="/github">
                  <GithubTable darkmode={darkmode} githubUser={githubUser} />
                </Route>
                <Route path="/leetcode">
                  <LeetcodeTable darkmode={darkmode} leetcodeUsers={leetcodeUsers}/>
                </Route>
                <Route path="/login">
                  <Login darkmode={darkmode}/>
                </Route>
                <Route path="/register">
                  <Register darkmode={darkmode}/>
                </Route>
              </Switch>
            </Grid>
          </Grid>
        </div>
      </Router>
      </ThemeProvider>
  );
}
export default App;
