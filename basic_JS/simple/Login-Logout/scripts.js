const app = document.getElementById("app");

// DB giả = localStorage
function getUsers() {
    return JSON.parse(localStorage.getItem("users")) || [];
}

function saveUsers(users) {
    localStorage.setItem("users", JSON.stringify(users));
}

function setCurrentUser(user) {
    localStorage.setItem("currentUser", user);
}

function getCurrentUser() {
    return localStorage.getItem("currentUser");
}

function logout() {
    localStorage.removeItem("currentUser");
    renderLogin();
}

/* ---------- LOGIN ---------- */
function renderLogin() {
    app.innerHTML = `
        <div class="login-box">
            <h2> Login</h2>
            <h5> Yahoo.copy </h5>
            <input id="user" placeholder="Username">
            <input id="pass" type="password" placeholder="Password">
            <button onclick="login()">Sign In</button>
            <div class="link" onclick="renderSignup()">Sign up</div>
        </div>
    `;
}

/* ---------- SIGN UP ---------- */
function renderSignup() {
    app.innerHTML = `
        <div class="login-box">
            <h2>Create Account</h2>
            <input id="user" placeholder="Username">
            <input id="pass" type="password" placeholder="Password">
            <button onclick="signup()">Register</button>
            <div class="link" onclick="renderLogin()">Back to Login</div>
        </div>
    `;
}

/* ---------- AFTER LOGIN ---------- */
function renderDashboard(username) {
    app.innerHTML = `
        <div class="login-box user-info">
            <h2>Welcome</h2>
            <p><b>${username}</b></p>
            <button class="signout" onclick="logout()">Sign Out</button>
        </div>
    `;
}

/* ---------- ACTIONS ---------- */
function signup() {
    const user = document.getElementById("user").value;
    const pass = document.getElementById("pass").value;

    if (!user || !pass) {
        alert("Please fill all fields");
        return;
    }

    const users = getUsers();
    users.push({ username: user, password: pass });
    saveUsers(users);

    alert("Sign up successful!");
    renderLogin();
}

function login() {
    const user = document.getElementById("user").value;
    const pass = document.getElementById("pass").value;

    const users = getUsers();
    const found = users.find(u => u.username === user && u.password === pass);

    if (!found) {
        alert("Invalid login");
        return;
    }

    setCurrentUser(user);
    renderDashboard(user);
}

/* ---------- INIT ---------- */
const current = getCurrentUser();
if (current) {
    renderDashboard(current);
} else {
    renderLogin();
}