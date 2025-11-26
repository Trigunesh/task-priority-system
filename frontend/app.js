let taskList = [];

// -------------------- ADD TASK --------------------
document.getElementById("add-btn").addEventListener("click", () => {
    const title = document.getElementById("title").value.trim();
    const due = document.getElementById("due").value;
    const hours = document.getElementById("hours").value;
    const importance = document.getElementById("importance").value;
    const deps = document.getElementById("deps").value.trim();

    if (!title || !due || !hours || !importance) {
        alert("Please fill all required fields!");
        return;
    }

    const task = {
        title: title,
        due_date: due,
        hours: parseInt(hours),
        importance: parseInt(importance),
        dependencies: deps ? deps.split(",").map(d => d.trim()) : []
    };

    taskList.push(task);
    renderTasks();

    // Clear inputs
    document.getElementById("title").value = "";
    document.getElementById("due").value = "";
    document.getElementById("hours").value = "";
    document.getElementById("importance").value = "";
    document.getElementById("deps").value = "";
});

// -------------------- BULK IMPORT --------------------
document.getElementById("bulk-btn").addEventListener("click", () => {
    try {
        const json = document.getElementById("bulk").value.trim();
        if (!json) return alert("Bulk JSON is empty!");

        const tasks = JSON.parse(json);

        if (!Array.isArray(tasks)) return alert("JSON must be an array!");

        tasks.forEach(t => {
            taskList.push({
                title: t.title,
                due_date: t.due_date,
                hours: t.hours,
                importance: t.importance,
                dependencies: t.dependencies || []
            });
        });

        renderTasks();
        alert("Imported successfully!");

    } catch (e) {
        alert("Invalid JSON format!");
    }
});

// -------------------- SEND TO BACKEND --------------------
document.getElementById("analyze-btn").addEventListener("click", async () => {
    if (taskList.length === 0) {
        alert("No tasks to analyze!");
        return;
    }

    const strategy = document.getElementById("strategy").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/api/tasks/analyze/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                tasks: taskList,
                strategy: strategy
            })
        });

        const data = await response.json();

        document.getElementById("result").textContent =
            JSON.stringify(data, null, 2);

    } catch (err) {
        alert("Server error. Check Django backend.");
        console.error(err);
    }
});

// -------------------- SHOW CURRENT TASK LIST --------------------
function renderTasks() {
    document.getElementById("result").textContent =
        JSON.stringify(taskList, null, 2);
}
