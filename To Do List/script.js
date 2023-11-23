const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("List-container");
const addButton = document.getElementById("add-button");





addButton.addEventListener("click", addTask);

function addTask() { 
    const taskText = inputBox.value.trim();
    if (taskText === '') {
        alert("Please write something"); 
    } else {
        const li = document.createElement("li");
        li.textContent = taskText;
        
        // Add click event to mark/unmark as checked
        li.addEventListener("click", toggleTask);

        listContainer.appendChild(li);
        inputBox.value = '';

        const span = document.createElement("span");
        span.className = "span";
        span.innerHTML = "\u00d7";
        span.addEventListener("click", deleteTask);
        li.appendChild(span);
    }
}

function toggleTask(event) {
    const li = event.target;
    li.classList.toggle("checked");
}

function deleteTask(event) {
    const span = event.target;
    const li = span.parentElement;
    li.remove();
}