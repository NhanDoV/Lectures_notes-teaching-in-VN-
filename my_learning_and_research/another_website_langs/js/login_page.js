// Create the login page container
const body = document.body;
body.style.cssText = "display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f3f3f3; font-family: Arial, sans-serif;";

const container = document.createElement("div");
container.style.cssText = "background-color: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); text-align: center; width: 300px;";
body.appendChild(container);

// Title
const title = document.createElement("h1");
title.innerText = "Login";
container.appendChild(title);

// Username input
const usernameLabel = document.createElement("label");
usernameLabel.setAttribute("for", "username");
usernameLabel.innerText = "Username:";
container.appendChild(usernameLabel);

const usernameInput = document.createElement("input");
usernameInput.type = "text";
usernameInput.id = "username";
usernameInput.name = "username";
usernameInput.placeholder = "Enter your username";
usernameInput.style.cssText = "width: 100%; padding: 0.8rem; margin: 1rem 0; border: 1px solid #ccc; border-radius: 4px;";
container.appendChild(usernameInput);

// Password input
const passwordLabel = document.createElement("label");
passwordLabel.setAttribute("for", "password");
passwordLabel.innerText = "Password:";
container.appendChild(passwordLabel);

const passwordInput = document.createElement("input");
passwordInput.type = "password";
passwordInput.id = "password";
passwordInput.name = "password";
passwordInput.placeholder = "Enter your password";
passwordInput.style.cssText = "width: 100%; padding: 0.8rem; margin: 1rem 0; border: 1px solid #ccc; border-radius: 4px;";
container.appendChild(passwordInput);

// Login button
const loginButton = document.createElement("button");
loginButton.innerText = "Login";
loginButton.style.cssText = "background-color: #007bff; color: white; padding: 0.8rem 1.2rem; border: none; border-radius: 4px; cursor: pointer; width: 100%;";
container.appendChild(loginButton);

loginButton.addEventListener("click", () => {
  const username = usernameInput.value;
  const password = passwordInput.value;

  if (username && password) {
    alert(`Welcome, ${username}!`);
    showHomePage(username);
  } else {
    alert("Please enter both username and password.");
  }
});

// Home Page View
function showHomePage(username) {
  container.innerHTML = ""; // Clear the container

  const homeTitle = document.createElement("h1");
  homeTitle.innerText = "Welcome to the Home Page!";
  container.appendChild(homeTitle);

  const welcomeMessage = document.createElement("p");
  welcomeMessage.innerText = `You are successfully logged in as ${username}.`;
  container.appendChild(welcomeMessage);

  const logoutButton = document.createElement("a");
  logoutButton.innerText = "Logout";
  logoutButton.href = "#";
  logoutButton.style.cssText = "display: block; margin-top: 1rem; color: #007bff; text-decoration: none;";
  container.appendChild(logoutButton);

  logoutButton.addEventListener("click", () => {
    location.reload(); // Reload the page to show the login form
  });
}
