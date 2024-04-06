
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
import { getAuth, signInWithEmailAndPassword} from "https://www.gstatic.com/firebasejs/10.7.2/firebase-auth.js";
import { getDatabase , set, ref} from "https://www.gstatic.com/firebasejs/10.7.2/firebase-database.js";

const firebaseConfig = {
  apiKey: "AIzaSyAcu3jr86mn8CMSuQfLNG7GFqG3DKYTjxs",
  authDomain: "login-and-signup-specnox.firebaseapp.com",
  projectId: "login-and-signup-specnox",
  storageBucket: "login-and-signup-specnox.appspot.com",
  messagingSenderId: "995897651175",
  databaseURL: "https://login-and-signup-specnox-default-rtdb.firebaseio.com/",
  appId: "1:995897651175:web:4b760ce31c2a946e4c1742",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const database = getDatabase(app);


const submit = document.getElementById("submit");
  
submit.addEventListener("click", function (event) {
  event.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  signInWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
      
    alert("Sign in")
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
      alert(errorMessage)
    });
});