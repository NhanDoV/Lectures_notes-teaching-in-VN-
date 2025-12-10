// Pure JS table with username/password toggle buttons
function createLoginTable() {
    const table = document.createElement('table');
    table.style.borderCollapse = 'collapse';
    table.style.width = '300px';
    table.style.margin = '50px auto';

    const thead = table.createTHead();
    const headerRow = thead.insertRow();
    headerRow.insertCell(0).textContent = 'User ID';
    headerRow.insertCell(1).textContent = 'Credentials';

    const users = [
        { id: 1, username: 'admin', password: '1234' },
        { id: 2, username: 'user1', password: 'pass1' },
        { id: 3, username: 'john', password: 'secret' },
        { id: 4, username: 'guest', password: '123' }
    ];

    users.forEach(user => {
        const row = table.insertRow();
        row.insertCell(0).textContent = `User ${user.id}`;

        const cell = row.insertCell(1);
        cell.textContent = user.username;
        cell.id = `cell-${user.id}`;

        row.querySelectorAll("td").forEach(td => {
            td.style.padding = "10px";
            td.style.border = "1px solid #ccc";
        });
    });

    const btnDiv = document.createElement('div');
    btnDiv.style.textAlign = 'center';
    btnDiv.style.marginTop = '20px';

    const usernameBtn = document.createElement('button');
    usernameBtn.textContent = 'Show Username';

    const passwordBtn = document.createElement('button');
    passwordBtn.textContent = 'Show Password';

    [usernameBtn, passwordBtn].forEach(btn => {
        btn.style.margin = '5px';
        btn.style.padding = '10px 20px';
        btn.style.border = 'none';
        btn.style.cursor = 'pointer';
    });

    usernameBtn.style.background = '#4CAF50';
    usernameBtn.style.color = 'white';

    passwordBtn.style.background = '#f44336';
    passwordBtn.style.color = 'white';

    function toggleView(showPass) {
        users.forEach(user => {
            const cell = document.getElementById(`cell-${user.id}`);
            cell.textContent = showPass ? user.password : user.username;
        });

        usernameBtn.textContent = 'Show Username';
        passwordBtn.textContent = 'Show Password';
    }

    usernameBtn.onclick = () => toggleView(false);
    passwordBtn.onclick = () => toggleView(true);

    document.body.appendChild(table);
    btnDiv.appendChild(usernameBtn);
    btnDiv.appendChild(passwordBtn);
    document.body.appendChild(btnDiv);
}

createLoginTable();