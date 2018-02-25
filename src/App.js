import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

// var Clarifai = require('clarifai');

// Clarifai.initialize({
//   'clientId': 'YOUR_CLIENT_ID',
//   'clientSecret': 'YOUR_CLIENT_SECRET’'
// });

// Clarifai.getTagsByUrl('https://samples.clarifai.com/wedding.jpg').then(
//   handleResponse,
//   handleError
// );

// class App extends Component {
//   render() {
//     return (
//       <div className="App">
//         <header className="App-header">
//           <img src={logo} className="App-logo" alt="logo" />
//           <h1 className="App-title">Welcome to React</h1>
//         </header>
//         <p className="App-intro">
//           To get started, edit <code>src/App.js</code> and save to reload.
//         </p>
//       </div>
//     );
//   }
// }




class App extends Component {
    render() {
      return (
        <div className="App">
          <header className="App-header">
            <h1 className="App-title">Welcome</h1>
          </header>
          <p className="App-intro">
          </p>
        </div>
      );
    }
  }

export default App;
